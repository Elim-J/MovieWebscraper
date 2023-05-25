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

# for title in movie_titles:
#     print(title)

# Create a ranking system on most 'dangerous' based off words
# names first and then rank so that you can search by name to assign rank
grief_dict = {'Kill':'1', 'Revenge':'2', 'Blood':'3', 'Dead':'4', 'Blade':'5', 'War':'6', 'Gun':'7', 'Die':'8'}
movie_rank = {}
# prints keys
# for x in grief_dict:
#     print(x)
#     print(grief_dict.get(x))

# prints values
# for x in grief_dict.values():
#     print(x)

# prints key and values
# for x,y in grief_dict.items():
#     print(x,y)
for movie in movie_titles:
    for x in grief_dict:
        if(movie.find(x) != -1):
            movie_rank.update({movie:grief_dict.get(x)})

for x,y in movie_rank.items():
    print(x,y)
# loop through movie_titles and compare them to dictionary
# if movie_titles are in map, insert into new map with their rank
# str.find(sub_str) if -1 then it is not in 
# I need to loop through names... and then see if they are present in movie names. Will take O(n) time...