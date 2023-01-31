from bs4 import BeautifulSoup as bs

with open('index.html', 'r') as file:
    content = file.read()
    # print(content)

    soup = bs(content, 'html.parser')

    # tags_h3 = soup.find_all('h3')

    # for tag in tags_h3:
    #     print(tag.text.strip())

    cards = soup.find_all('div', class_='card')
    for card in cards:
        h1 = card.h1.text.strip().split('/')[0].split('$')[1]
        ul = card.ul.find_all('li')

        print(f"\nPrice: {h1}")

        i = 1
        for li in ul:
            print(f"{i}) {li.text.strip()}")
            i += 1
