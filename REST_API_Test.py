import requests

url = 'http://jsonplaceholder.typicode.com/photos'

#### GET
response = requests.get(url)
#print(response.json())

### POST
jsonPayload = {'albumId':1, 'title':'test', 'url':'nothing.com', 'thumbnailUrl':'nothing.com'}
new_response = requests.post(url, json=jsonPayload)
print(new_response.json())

#### PUT