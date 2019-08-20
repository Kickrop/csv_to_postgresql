import psycopg2
import csv
import private
import os
from tqdm import tqdm

conn = psycopg2.connect(host=private.sr_host, dbname=private.sr_dbname, user=private.sr_user, password=private.sr_password)
cur = conn.cursor()

#specify data base schema
schema = 'fronts'
table_name = 'cleaned_data_2'
file_name = 'cleaned_data' + '.csv'
file_delimiter = ','

path = 'H:\Fronts\jan2019\correction(aug19)'

os.chdir(path)

def create_table_with_csvheader():
    with open(file_name, 'r') as f:
        csv_reader = csv.reader(f, delimiter=file_delimiter)
        csv_header = next(csv_reader)
        header_to_insert = ''
        for i in csv_header:      
            header_to_insert = header_to_insert+ (i + ' text NOT NULL,')
        header_to_insert = header_to_insert[0:-1]
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {schema}.{table_name}(
        {header_to_insert}
        )
        """)
        conn.commit()
        print(f"{table_name} created successfully")
    f.close()

def insert_into_table():
    print('Insert may take some time...')
    with open(file_name, 'r') as f:
        #csv_reader = csv.reader(f, delimiter=file_delimiter)
        cur.copy_expert(f'COPY {schema}.{table_name} FROM STDIN WITH CSV HEADER', f) #sep=file_delimiter
    conn.commit()
    f.close()
    print('Inserted successfully')

create_table_with_csvheader()
insert_into_table()