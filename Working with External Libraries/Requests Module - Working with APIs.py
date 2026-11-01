# The requests library simplifies making HTTP requests. This is essential for interacting with web APIs (Application Programming Interfaces).
# refer the official request module docs

# https://requests.readthedocs.io/en/latest/


'''
import requests

url = "https://api.github.com/users/octocat"  # Example API endpoint
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data["name"])  # Access data from the JSON
else:
    print(f"Error: {response.status_code}")

# Making a POST request (for sending data to an API):
# data = {"key": "value"}
# response = requests.post(url, json=data)  # Sends data as JSON

# Other HTTP methods: put(), delete(), etc.

'''
import requests

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r = requests.get('https://api.github.com/user')
# r.status_code
print(r.text)