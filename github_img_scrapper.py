import requests
from bs4 import BeautifulSoup as bs

github_user = input('Enter Github user: ')

while len(github_user) == 0:
    print('please enter a valid username')
    github_user = input('Enter Github user: ')

github_url = 'https://github.com/' + github_user

res = requests.get(github_url)
soup = bs(res.content, 'html.parser')
profile_img = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_img)


