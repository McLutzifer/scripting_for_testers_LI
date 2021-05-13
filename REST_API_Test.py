import requests

url = 'http://jsonplaceholder.typicode.com/photos'

#### GET
response = requests.get(url)
#print(response.json())

### POST
jsonPayload = {'albumId':1, 'title':'test', 'url':'nothing.com', 'thumbnailUrl':'nothing.com'}
post_response = requests.post(url, json=jsonPayload)
#print(post_response.json())

#### PUT
new_url = 'http://jsonplaceholder.typicode.com/photos/100'
put_response = requests.put(new_url, json=jsonPayload)
#print(put_response.json())

### DELETE
delete_response = requests.delete(new_url)
print(delete_response.json())
