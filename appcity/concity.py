import requests

TOCKEN = 'Sfbhzr9syitatZ9RKKBSSNkbQiaTBkyz'
URLAPI = 'https://kladr-api.ru/api.php'
lit = []
a = ord('а')
for i in range(a, a + 32):
    if chr(i) == "й" or chr(i) == "ь" or chr(i) == "ы" or chr(i) == "ъ" or chr(i) == "э":
        continue
    ert = ''.join([chr(i)])
    # print(''.join([chr(i)]))
    response = requests.get(f'{URLAPI}?query={ert}&contentType=city')
    r = response.json()
    # print(r)
    for i in range(1, 400):
        if r['result'][i]['typeShort'] == 'г':
            lit.append(r['result'][i]['name'])
print(len(lit))
# print(lit)
from itertools import groupby

x = lit

new = [el for el, _ in groupby(x)]
print(new)
print(len(new))
import psycopg2

con = psycopg2.connect(
    database="msdb",
    user="postgres",
    password="Sashkachuk04)",
    host="127.0.0.1",
    port="5432"
)
cur = con.cursor()

for r in new:
    r = ("'" + r + "'")
    cur.execute(f'INSERT INTO appcity_city(name) '
                f'VALUES({r}) ')
    print(r)
con.commit()
con.close()
