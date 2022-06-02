import requests

URLAPI = 'https://kladr-api.ru/api.php'
lit = []
response = requests.get(f'{URLAPI}?query=наримано&contentType=street&cityId=1&regionId=1')
r = response.json()
print(r)
for i in range(1, 48):
    if r['result'][i]['typeShort'] == 'ул':
        lit.append(r['result'][i]['okato'])
        lit.append(r['result'][i]['name'])
print(len(lit))
print(lit)
