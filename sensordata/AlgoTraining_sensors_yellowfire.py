import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Caricare il dataset
file_path = 'merged_dataset_sensors_yellowfire.csv'  # Modifica con il percorso del tuo file
data = pd.read_csv(file_path, delimiter=';')

# Verifica delle colonne del file CSV
print("Nomi delle colonne del file CSV:", data.columns)

# Generazione delle colonne log10(si)
for i in range(10):
    if f's{i}' in data.columns:
        data[f'log_s{i}'] = np.log10(data[f's{i}'] + 1)  # +1 per evitare log10(0)
    else:
        raise KeyError(f"Colonna 's{i}' non trovata nel dataset")

# Generazione delle colonne D0, D1, ..., D8
for i in range(9):
    data[f'D{i}'] = data[f'log_s{i+1}'] - data[f'log_s{i}']

# Codifica delle etichette di classe in numeri
label_encoder = LabelEncoder()
data['value_encoded'] = label_encoder.fit_transform(data['value'])

# Verifica dei valori unici dopo la codifica
print("Valori unici nella colonna 'value_encoded':", data['value_encoded'].unique())

# Creare il dataset per l'addestramento
features = [f'D{i}' for i in range(9)]
X = data[features]
y = data['value_encoded']

# Dividere il dataset in train e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Addestrare il modello Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
print("Random Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))

# Addestrare il modello XGBoost
xgb_model = XGBClassifier(random_state=42)
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)
print("XGBoost Classification Report:")
print(classification_report(y_test, y_pred_xgb))
print("XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))

# Salvare il nuovo dataset in formato .xlsx
data.to_excel('new_dataset.xlsx', index=False)
print("File salvato come 'new_dataset.xlsx'")
