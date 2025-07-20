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

# Say there was a BeReal API (not public yet, sadly 😢), your app could say:

# “API, show me Haniya’s BeReal from today.”

# And the API would send back:

{
  "username": "haniyak",
  "image": "https://bereal.com/haniyak/2025-07-20.jpg",
  "caption": "at work 💻"
}
