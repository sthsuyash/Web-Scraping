import requests
from bs4 import BeautifulSoup

url = "https://imdb.to/3CzG7te"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

all_data = soup.find_all("div", class_="lister-item mode-advanced")

titles_and_runtimes = []

for data in all_data:
    title = data.h3.a.text
    runtime = data.find("span", class_="runtime").text
    titles_and_runtimes.append((title, runtime))

for title, runtime in titles_and_runtimes:
    print(f"Title: {title}\nRuntime: {runtime}\n")
