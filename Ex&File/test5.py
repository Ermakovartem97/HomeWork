import requests
import json


res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
table = json.loads(res.text)

valutes = table['Valute']
nameVal = valutes.keys()
print(valutes.values())
myTab = []
for name in nameVal:
    myTab.append([valutes[name]['CharCode'], valutes[name]['Name'], valutes[name]['Value']])
print(myTab)
