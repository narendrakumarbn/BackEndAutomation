import requests
from utilities.configurations import *


url = "https://api.github.com/user"
github_response = requests.get(url,verify=False ,auth=("narendrkumarbn", getPassword()))  #verify=False if we found any issue SSL certification
print(github_response.status_code)
