# remember requests is a 3rd party module, you will need to install it
# create a python virtual environment and then install dependencies from requirements.txt file
# how to create python virtual environment windows: `python -m venv venv` mac/linux: `python3 -m venv venv`
# activate python virtual environment windows `:.\venv\Scripts\activate` mac/linux: `source venv/bin/activate`
# install dependencies from requirements.txt `pip install -r requirements.txt`
import requests
response = requests.get("https://www.google.com")
print(response.text)