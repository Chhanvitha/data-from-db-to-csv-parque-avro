import pandas as pd
from sqlalchemy import create_engine
import fastavro
import os

def fetch_and_export_data():
    #Connecting to PostgreSQL
    engine = create_engine('postgresql://youruser:yourpassword@localhost:5432/yourdatabase')

    tables_to_export = ['users', 'orders']  # Replace with your actual table names

    for table_name in tables_to_export:
        print(f"Exporting table: {table_name}")

        df = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)

        os.makedirs("exports", exist_ok=True)

        df.to_csv(f"exports/{table_name}.csv", index=False)

        df.to_parquet(f"exports/{table_name}.parquet", index=False)

        records = df.to_dict(orient='records')
        schema = {
            "type": "record",
            "name": f"{table_name}_record",
            "fields": [{"name": col, "type": "string"} for col in df.columns]
        }

        with open(f"exports/{table_name}.avro", "wb") as out:
            fastavro.writer(out, schema, records)

        print(f"✅ {table_name} exported to CSV, Parquet, and Avro.")

    print("All tables exported successfully.")
