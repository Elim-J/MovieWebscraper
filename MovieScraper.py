from requests_html import HTMLSession

s = HTMLSession()

def get_title_element(page):
    movie_titles = []
    url = f'https://au.rollingstone.com/100-greatest-movies-of-all-time/page/{page}/' 
    r = s.get(url)
    # Return list of movie titles       
    list = r.html.find('h3.c-list__title')
    return list

def parse_title_element(list):
    for element in list:
        movie_titles.append(element.text.strip())

        
movie_titles = []

for i in range(9):
    list = get_title_element(i)
    parse_title_element(list)

for title in movie_titles:
    print(title)