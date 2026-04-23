# remember requests is a 3rd party module, you will need to install it
# create a python virtual environment and then install dependencies from requirements.txt file
import requests
response = requests.get("https://www.google.com")
print(response.text)