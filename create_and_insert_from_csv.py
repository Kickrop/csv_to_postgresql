import psycopg2
import csv
import private
import os
from tqdm import tqdm

conn = psycopg2.connect(host=private.sr_host, dbname='cases', user=private.sr_user, password=private.sr_password)
cur = conn.cursor()

#specify postgres schema
schema = 'stat_customs'  #'fronts'

#table name in postgres
table_name = 'spr_tnvd' #'cleaned_fronts_aug2019'

#file that contains data to insert into postgres
file_name = 'sp_THBED1_edit' + '.csv'
file_delimiter = ';'

#path to data file
path = 'H:/Работа2/30.01.2019.Для Сагиевой/04.2019.РасчетЭкспорта' #'H:/Fronts/08_2019/front_files' 

os.chdir(path)

def create_table_with_csvheader():
    #make shure headers inside csv file doesn't have spaces
    with open(file_name, 'r', encoding="utf8") as f:
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
    with open(file_name, 'r', encoding="utf8") as f:
        #csv_reader = csv.reader(f, delimiter=file_delimiter)
        cur.copy_expert(f"""COPY {schema}.{table_name} FROM STDIN WITH CSV HEADER DELIMITER as '{file_delimiter}'""", f)
    conn.commit()
    f.close()
    print('Inserted successfully')

create_table_with_csvheader()
insert_into_table()