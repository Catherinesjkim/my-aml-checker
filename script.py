import pandas as pd

# Load the CSV file
file_path = 'synthetic_credit_card_transactions.csv'
df = pd.read_csv(file_path)
# df == DataFrame, a data structure used by the pandas library to store tabular data like a spreadsheet of DB table
# df now holds the contents of that file in a structured, table-like format

# Filter transactions where amount is over $10,000
flagged_df = df[df['amount'] > 10000] 

# Save only the flagged transactions to a new CSV
output_path = 'flagged_transactions_only.csv'
flagged_df.to_csv(output_path, index=False)

# Print summary
print(f"{len(flagged_df)} transactions flagged and saved to '{output_path}'.")

