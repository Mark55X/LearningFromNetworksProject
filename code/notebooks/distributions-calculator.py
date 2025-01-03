# Command to create a directory where the data will be stored: " $env:STORE_DIRECTORY="$PWD\TRADES_DATA" "
# Command to download all trades for month 1, year 2024: " python download-trade.py -y 2024 -m 1 -t spot "

import pandas as pd
import numpy as np
import zipfile
import os
import networkx as nx

# Paths
base_directory = 'TRADES_DATA/data/spot/monthly/trades/'

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

cryptoNames = [
    "ADA", "ADX", "AMB", "AST", "BAT", "BLZ", "BNB", "BNT", "BTC", "DASH",
    "ELF", "ENJ", "EOS", "ETC", "ETH", "FUN", "GAS", "ICX", "IOST", "IOTA",
    "KMD", "KNC", "LINK", "LOOM", "LRC", "LSK", "LTC", "MANA", "MTL", "NEO",
    "NULS", "OAX", "ONT", "PIVX", "POWR", "QTUM", "REQ", "RLC", "SNT", 
    "STEEM", "STORJ", "SYS", "THETA", "TRX", "TUSD", "VIB", "WAN", "WAVES", 
    "XLM", "XMR", "XRP", "ZEC", "ZEN", "ZIL", "ZRX"
]

G = nx.DiGraph()
G.add_nodes_from(cryptoNames)

for currency_pair, (mean, standard_deviation) in results.items():
    # Crypto name extraction
    from_currency = None
    to_currency = None

    # Search for the two crypto names
    for name in cryptoNames:
        if currency_pair.startswith(name):
            from_currency = name
            to_currency = currency_pair[len(from_currency):]
            break
     
    # Check if the names are valid
    if from_currency and to_currency in cryptoNames:
        G.add_edge(from_currency, to_currency, weight = f"{mean}_{standard_deviation}")
        #G.add_edge(from_currency, to_currency, weight = mean)

# Saving the graph into a XML file 
nx.write_graphml(G, "crypto_graph.graphml")
