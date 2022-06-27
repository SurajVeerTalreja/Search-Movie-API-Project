import requests
import os

movie_name = input("Write a movie title you're searching for. ")

parameters = {
    "apikey": os.environ.get("API_KEY"),
    "s": f"{movie_name}",
}

response = requests.get(url="http://www.omdbapi.com", params=parameters)
response.raise_for_status()

movie_database = response.json()["Search"]
print("\nSearch results for you given title are:\n")
for movie in movie_database:
    print(movie["Title"], end=", ")
    print(f"Movie's Poster Link: {movie['Poster']}")
