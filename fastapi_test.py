import requests

# This sends a request to the Cat Facts API
response = requests.get("https://catfact.ninja/fact")

# This prints the cat fact from the response
print(response.json()["fact"])


import requests

# Ask the joke API for a random joke
response = requests.get("https://official-joke-api.appspot.com/random_joke")

# Turn the response into something we can read
joke = response.json()

# Show the setup and punchline
print(joke["setup"])
print(joke["punchline"])
