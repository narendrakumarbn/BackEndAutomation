from payload import *
import requests
import json 
from utilities.configurations import *
from utilities.resources import *

getConfig()
url = getConfig()['API']['endpoint']+ApiResources.addBook
headers = {"Content-Type": 'application/json'}
addBook_response = requests.post(url, 
                        json=AddBookPayload(),
                        headers=headers,
)

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']

##delete the book 

url = getConfig()['API']['endpoint']+ApiResources.deleteBook
response_deleteBook = requests.delete(url, json={
            "ID" : bookId},
            headers=headers,
)

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()
print(res_json)
assert res_json == {'msg': 'book is successfully deleted'}