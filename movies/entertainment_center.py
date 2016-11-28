# tmdbsimple is a wrapper, written in Python, for The Movie Database (TMDb) API v3
import tmdbsimple as tmdb                                  
import media, fresh_tomatoes

# user api key from TMDb
tmdb.API_KEY = 'e4a20f8979adce5bcba4445a50531435'

# session id authenticating access to TMDb information
SESSION_ID = "619a5728f300e20b74f246b9d55f0d5e1c553259"     
                                                            
# create an Account instance from tmdbsimple module
user = tmdb.Account(SESSION_ID) 

# retrieve basic information for an account
user.info() 

# rerieve the list of favorite movies for an account as a dictionary
movie_dict = user.favorite_movies()

# get a list of the movies in movie_dict with only movie data
movie_list = movie_dict['results']

# create empty list to pass to the fresh_tomatoes method
fresh_tomato_movie_list = []

# constant path for images on the TMDb website
POSTER_IMAGE_PATH = "https://image.tmdb.org/t/p/original"

# constant path for trailers on YouTube
YOUTUBE_PATH = "https://www.youtube.com/watch?v="

# loop through movies in the movie list
for item in movie_list:
    # extract a list of trailers for associated movie identified by id
    trailer_list = tmdb.Movies(item['id']).videos()['results']  
    # extract key to append to YouTube constant                                                                                    
    trailer_key = trailer_list[0]['key']
    # extract title, plot, poster image url & youtube trailer url for Movie class from media
    fresh_tomato_movie_list.append(media.Movie(item['title'],
                                               POSTER_IMAGE_PATH+item['poster_path'],
                                               YOUTUBE_PATH+trailer_key))



fresh_tomatoes.open_movies_page(fresh_tomato_movie_list)

