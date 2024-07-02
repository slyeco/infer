import pandas as pd
import glob
import os

# Path della cartella Dataset
dataset_path = 'Dataset'

# Lista di tutti i file CSV nella cartella Dataset
csv_files = glob.glob(os.path.join(dataset_path, '*.csv'))

# Funzione per determinare il valore della colonna in base all'ora
def determine_value(timestamp):
    time = pd.to_datetime(timestamp).time()
    if time >= pd.to_datetime('14:00:00').time() and time <= pd.to_datetime('17:00:00').time():
        return 'air'
    elif time >= pd.to_datetime('17:20:00').time() and time <= pd.to_datetime('21:20:00').time():
        return 'fire'
    elif time >= pd.to_datetime('22:30:00').time() and time <= pd.to_datetime('23:30:00').time():
        return 'air'
    return None

# Lista per contenere i DataFrame
dfs = []

for file in csv_files:
    # Leggi il CSV
    df = pd.read_csv(file)
    
    # Estrai il codice del sensore dal nome del file
    sensor_code = os.path.basename(file).split('_')[2]
    tree_name = f"Tree{sensor_code[-2:]}"
    
    # Determina il valore della nuova colonna in base al timestamp
    df['_time'] = pd.to_datetime(df['_time'])  # Assumendo che ci sia una colonna '_time' nei CSV
    df['value'] = df['_time'].apply(determine_value)
    
    # Filtra i dati non necessari
    df = df[df['value'].notna()]
    
    # Aggiungi la colonna del nome del sensore
    df['sensor_name'] = tree_name
    
    # Aggiungi il DataFrame alla lista
    dfs.append(df)

# Unisci tutti i DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Salva il DataFrame unito in un nuovo file CSV
merged_df.to_csv('merged_dataset.csv', index=False)

print("File unito creato con successo: merged_dataset.csv")
