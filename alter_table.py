import psycopg2
import csv
from tqdm import tqdm

conn = psycopg2.connect(host="172.18.207.27", dbname="cases", user="dmartynov", password="LKhjkljklkwJBJjkw%499lekc$68")
cur = conn.cursor()
#table_name = 'test'


statreg6 = [1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	67,	74,	78,	79,	95,	105,	113,	116,	117,	118,	119,	120]
for i in statreg6:
    cur.execute("""
        ALTER TABLE statregistr.statregistr6 RENAME COLUMN "{}" TO pole_{};
        """.format(i,i))
    conn.commit()
    #print(cur)