
import requests
import json
import configparser
from utilities.configurations import *



response = requests.get(getConfig()['API']['endpoint']+'/Library/GetBook.php', 
                        params={'AuthorName':'Rahul Shetty'},)

json_response = response.json()
#print(json_response)
print(json_response[0]['isbn'])

print(response.status_code)
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'


#retrieve the book details  with  ISBN RGHCC
for actualbook in json_response:
    if actualbook['isbn'] == 'RGHCC':
        print("Book Found:", actualbook)
        break
else:
    print("Book not found!")

expectedbook = {
    "book_name": "Learn API Automation with RestAssured",
    "isbn": "RGHCC",
    "aisle": "12239"
}



print("Actual Book:", actualbook)
print("Expected Book:", expectedbook)
#assert actualbook == expectedbook

json_response = response.json()
print("All ISBN numbers returned by API:")

for book in json_response:
    print(book["isbn"])