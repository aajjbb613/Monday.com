#TO READ FROM MONDAY

import requests
import json

apiKey = "XXX"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

#query = 'query{ boards (ids: 695791534){items{name id column_values{title id value}}}}'
#query = 'query{ boards (ids: 711201285){items{name id}}}'
query = 'query{ boards (ids: 711201285){items(ids: 1392408871){name column_values{title id value text}}}}'
#query = 'query{ boards (ids: 695791534){items{name column_values(ids:status1){value text}}}}'
data = {'query' : query}

#711201285 = Mattamy Homes
#695791534 = Minto
#718348165 = Caivan
#1190887252 = Urbandale

r = requests.post(url=apiUrl, json=data, headers=headers) # make request
x = r.json()
print(x)
