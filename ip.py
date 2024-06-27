"""
Author: devanshu shresth
Date: 27/6/2024
"""

import pandas as pd
from tabulate import tabulate

# Load the Excel file
file_path = 'C:/Users/hp/Downloads/p_address.xlsx'  # path where your excel file is stored
df = pd.read_excel(file_path, engine='openpyxl')

# IP addresses are in a column named 'ip_address', adjust as needed
ip_counts = df['ip_address'].value_counts()

# Filter IP addresses that appear more than 5 times (adjust as needed)
repeated_ips = ip_counts[ip_counts > 5].index.tolist()

# Print or further process the repeated IPs
print("IP addresses repeated more than 5 times:", repeated_ips)

# If you want to extract rows with these IP addresses
repeated_rows = df[df['ip_address'].isin(repeated_ips)]

# Print rows with repeated IPs in tabular format
print("\nRows with repeated IPs (Tabular Format):")
print(tabulate(repeated_rows, headers='keys', tablefmt='psql'))

# Save these rows to a new Excel file
repeated_rows.to_excel('repeated_ips.xlsx', index=False, engine='openpyxl')
