from requests_html import HTMLSession

s = HTMLSession()
url = 'https://au.rollingstone.com/100-greatest-movies-of-all-time/page/2/'

r = s.get(url)

list = r.html.find('h3.c-list__title')
movie_titles = []
for element in list:
    movie_titles.append(element.text)

for title in movie_titles:
    print(title)