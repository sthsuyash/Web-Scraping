import requests
from bs4 import BeautifulSoup

# input the github username
name = input(f"Enter github username: ")
# modify the url according to the username
url = f"https://github.com/{name}?tab=repositories"
# get the response from the url
response = requests.get(url)

'''
Check if the request is successful or not
'''
# if response.status_code == 200:
#     print("Success!")
# else:
#     print("Error!")

if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")

    repos_container = soup.find_all(
        "li", class_="col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source"
    )
    # print(repos_container)
    print()
    i = 0
    for repos in repos_container:
        try:
            i += 1
            repo_name = repos.find("a").text.strip()
            repo_link = "https://github.com" + repos.find("a")["href"]
            repo_desc = repos.find("p").text.strip()
            repo_lang = repos.find("span", class_="ml-0 mr-3").text.strip()
            print(
                f"{i}) Name: {repo_name}\nLink: {repo_link}\nDescription: {repo_desc}\nLanguage: {repo_lang}\n")
        except:
            pass

else:
    print("Username not found!")
