from bs4 import BeautifulSoup as bs

with open('index.html', 'r') as file:
    content = file.read()
    # print(content)

    soup = bs(content, 'html.parser')

    container = soup.find_all('div', class_='visit-container')
    for items in container:
        places = items.text.strip()
        print(f"Places: {places}")
