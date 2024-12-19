# Command to create a directory where the data will be stored: " $env:STORE_DIRECTORY="$PWD\DATA" "
# Command to download all trades for month 1, year 2024: " python download-trade.py -y 2024 -m 1 -t spot "

import pandas as pd
import numpy as np
import zipfile
import os

# Paths
base_directory = 'DATA/data/spot/monthly/trades/'

# Dictionary to save the data as: Trade-Name: (Mean, Standard Deviation)
results = {}

for currency_pair in os.listdir(base_directory):
    currency_path = os.path.join(base_directory, currency_pair)
    
    # Check if it is a valid directory
    if os.path.isdir(currency_path):
        for zip_file in os.listdir(currency_path):
            if zip_file.endswith('.zip'):
                zip_file_path = os.path.join(currency_path, zip_file)
                print(f"Opening Zip file: {zip_file_path}")
                # Read the CSVs
                with zipfile.ZipFile(zip_file_path, 'r') as z:
                    csv_file_name = zip_file.replace('.zip', '.csv')  # CSV file's name is the same as the zip
                    if csv_file_name in z.namelist():
                        with z.open(csv_file_name) as f:
                            data = pd.read_csv(f, header = None)

                        # Rename the columns within the file following the correct format specified by Binance
                        data.columns = [
                            "trade_id",          
                            "price",            
                            "quantity",          
                            "quote_quantity",    
                            "timestamp",         
                            "is_buyer_maker",   
                            "is_best_match"  
                        ]

                        # Prices column (cast into float)
                        prices = data['price'].astype(float)

                        mean = np.mean(prices)
                        standard_deviation = np.std(prices)
                        # Saving data
                        results[currency_pair] = (mean, standard_deviation)

# Print results
for currency, (mean, stddev) in results.items():
    print(f"Currency Pair: {currency}, Mean (mu): {mean}, Standard Deviation (sigma): {stddev}")
   