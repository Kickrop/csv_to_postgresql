import psycopg2
import csv
#import private
import os
from tqdm import tqdm

# main_ru
conn = psycopg2.connect(host='127.0.0.1', dbname='postgres', user='postgres', password='68417399')
cur = conn.cursor()

#specify postgres schema
schema = 'rospatent'#'rospatent' #'stat_customs'   #'fronts'statregistr

#table name in postgres
table_name = '_1_patstat_rospatent_assignees'  # 'cleaned_fronts_aug2019'

#file that contains data to insert into postgres
file_name = '_1_patstat_rospatent_assignees' + '.csv'
file_delimiter = ';'

#path to data file
# 'H:/Работа2/27.05.19.Статрегистр/БД от росстата 28.08.19' #'H:/Работа2/30.01.2019.Для Сагиевой/04.2019.РасчетЭкспорта' #'H:/Fronts/08_2019/front_files'
path = 'C:/YandexDisk/data/patstat_20191115'

os.chdir(path)

#utf 8 with bom
encode = 'utf-8'  # utf-8-sig
def create_table_with_csvheader():
    #make shure headers inside csv file doesn't have spaces
    with open(file_name, 'r', encoding=encode) as f:
        csv_reader = csv.reader(f, delimiter=file_delimiter)
        csv_header = next(csv_reader)
        header_to_insert = ''
        for i in csv_header:      
            header_to_insert = header_to_insert+ (i + ' text,')#(i + ' text NOT NULL,') #(i + ' varchar(255),') #
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
    with open(file_name, 'r', encoding=encode) as f:
        cur.copy_expert(f"""COPY {schema}.{table_name} FROM STDIN WITH CSV HEADER DELIMITER as '{file_delimiter}'""", f)
    conn.commit()
    f.close()
    print('Inserted successfully')

def drop_table():
    cur.execute(f"""
    DROP TABLE IF EXISTS {schema}.{table_name}""")
    conn.commit()
    print(f"{table_name} droped")

#drop_table()
create_table_with_csvheader()
insert_into_table()
