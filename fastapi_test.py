import requests

# This sends a request to the Cat Facts API
response = requests.get("https://catfact.ninja/fact")

# This prints the cat fact from the response
print(response.json()["fact"])
