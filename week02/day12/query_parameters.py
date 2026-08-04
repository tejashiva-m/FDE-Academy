import requests

params = {
    "userId": 1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

posts = response.json()

print(len(posts))

for post in posts[:5]:
    print(post["title"])

    