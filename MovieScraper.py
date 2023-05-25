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

def assign_rank(dict):
   for movie in movie_titles:
    for x in grief_dict:
        if(movie.find(x) != -1):  #if not equal to -1, then the string is in the movie
            movie_rank.update({movie:grief_dict.get(x)})

  
movie_titles = []
grief_dict = {'Kill':'1', 'Revenge':'2', 'Blood':'3', 'Dead':'4', 'Blade':'5', 'War':'6', 'Gun':'7', 'Die':'8'}
movie_rank = {}
       
for i in range(9):
    list = get_title_element(i)
    parse_title_element(list)

assign_rank(movie_rank)

for x,y in movie_rank.items():
        print(x,y)


