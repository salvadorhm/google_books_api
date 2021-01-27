import requests
import json

result = requests.get("https://www.googleapis.com/books/v1/volumes?q=sinsajo")

book = result.json()

items = book["items"]

encoded = json.dumps(items)
decoded = json.loads(encoded)

print(decoded[0]["volumeInfo"]["infoLink"])