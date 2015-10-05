# The file is the main file which needs to be run to create the html page.
# This file allows adding movies and then calls the open_movies_page function
# to create html'''

# Import relevant class and functions
import media
import fresh_tomatoes

# Create sample movie objects
toystory = media.Movie("Toy Story",
                       "Toys come to life",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

pk = media.Movie("PK",
                 "Alien confused about god",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/2/2d/PK_Theatrical_Poster.jpg/220px-PK_Theatrical_Poster.jpg",
                 "https://www.youtube.com/watch?v=82ZEDGPCkT8")


# List all the movie objects into movies list
# Note that the open_movies_page
movies = [toystory, avatar, pk]

# Call the open_movies_page function to create HTML page
fresh_tomatoes.open_movies_page(movies)
