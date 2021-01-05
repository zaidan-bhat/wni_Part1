import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'longitude'= 139.75 , 'latitude'= 35.69 , 'date_time':2020091908})

print(r.json())