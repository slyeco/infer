import pandas as pd
import json
import os
import argparse

def process_data(file_path, label):
    with open(file_path, 'r') as f:
        data = json.load(f)
        
    # Extracting necessary information
    columns = {col['key']: i for i, col in enumerate(data['data']['dataColumns'])}
    data_points = pd.DataFrame(data['data']['specimenDataPoints'], columns=[col['key'] for col in data['data']['dataColumns']])
    
    # Filter out the rows with cycle_step_index 0 and get the initial data
    initial_data = data_points[data_points['cycle_step_index'] == 0]
    initial_data = initial_data[['cycle_id', 'temperature', 'relative_humidity', 'pressure', 'resistance_gassensor']]
    initial_data.columns = ['cycleID', 'Temperature', 'Humidity', 'Pressure', 'Resistance0']
    initial_data['label'] = label
    
    # Pivot to get the resistance values for each step_index 1-9
    resistance_data = data_points[data_points['cycle_step_index'] > 0]
    resistance_pivot = resistance_data.pivot(index='cycle_id', columns='cycle_step_index', values='resistance_gassensor')
    
    # Rename the columns
    resistance_pivot.columns = [f'Resistance{int(col)}' for col in resistance_pivot.columns]
    resistance_pivot.reset_index(inplace=True)
    resistance_pivot.rename(columns={'cycle_id': 'cycleID'}, inplace=True)
    
    # Merge the initial data with the resistance values
    final_df = pd.merge(initial_data, resistance_pivot, on='cycleID', how='left')
    
    return final_df

def process_files(input_path, output_file, label):
    if os.path.isdir(input_path):
        all_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
    else:
        all_files = [input_path]

    final_df = pd.DataFrame()
    for file in all_files:
        df = process_data(file, label)
        final_df = pd.concat([final_df, df], ignore_index=True)

    final_df.to_csv(output_file, index=False)
    print(f"Data has been written to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process JSON data files and output to CSV')
    parser.add_argument('input_path', type=str, help='Input folder or file path')
    parser.add_argument('output_file', type=str, help='Output CSV file name')
    parser.add_argument('label', type=str, help='Label to add to the data')

    args = parser.parse_args()
    process_files(args.input_path, args.output_file, args.label)
