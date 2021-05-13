import requests

url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
#print(response.json())

jsonPayload = {'albumId':1, 'title':'test', 'url':'nothing.com', 'thumbnailUrl':'nothing.com'}
new_response = requests.post(url, json=jsonPayload)
print(response.json())