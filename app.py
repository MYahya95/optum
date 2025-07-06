import json
import os
import pandas as pd
from pandas import json_normalize
import sqlalchemy
from sqlalchemy import create_engine, text

def main():

    # Create sql engine
    engine = create_engine("sqlite+pysqlite:///optum_data.db", echo=True, future=True)

    # Create filepath to dataset
    file_names = os.listdir('data/')
    for file_name in file_names:
            file=file_name.removesuffix(".json")

            # Read in FHIR json files
            if file_name.endswith('c6.json'): # Adjust ending to specify files
                with open('data/'+file_name) as f:
                    fhir_data = json.load(f)
            
                # List all resources in each entry within the FHIR data
                resources = [entry['resource'] for entry in fhir_data['entry']]
            
                # Normalize semi-structured JSON data into a flat table
                df = pd.json_normalize(resources)
            
                # Save to an excel workbook
                if os.path.exists('optum_data.xlsx'):
                    with pd.ExcelWriter('optum_data.xlsx',
                                        mode='a', if_sheet_exists='replace') as writer: 
                # Worksheet titles shouldn't contain more than 31 characters
                        df.to_excel(writer, sheet_name=file[:30])
                else: df.to_excel("optum_data.xlsx", sheet_name=file[:30], index=False)
                
                # Create sql table for each file
                df_sql = df
                df_sql = df_sql.map(str)
                try:
                    df_sql.to_sql(file+'_Table', engine)
                # Rebuild the table if it already exists
                except ValueError:
                    print("Sql table already exists")
                    with engine.begin() as conn:
                        conn.execute(text(f"DROP TABLE `{file+'_Table'}`"))
                    df_sql.to_sql(file+'_Table', engine)
                    conn.close()

    engine.dispose()

    print('FHIR data has been converted to xlsx and sql')

if __name__=="__main__":
    main()