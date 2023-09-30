import requests

url = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=b0b382f54ddd2d12ef04e66c631b5d62&format=json&nojsoncallback=1&auth_token=72157720895550131-35095ef56d8a8550&api_sig=fc34a9fb2c3547d3663cd7c537e30caf"

response = requests.get(url)
data = response.json()

print(data)