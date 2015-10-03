import media
import fresh_tomatoes

toystory = media.Movie("Toy Story", "Toys come to life",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

pk = media.Movie("PK", "Alien confused about god",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/2/2d/PK_Theatrical_Poster.jpg/220px-PK_Theatrical_Poster.jpg",
                 "https://www.youtube.com/watch?v=82ZEDGPCkT8")
#avatar.show_trailer()

movies = [toystory, avatar, pk]
fresh_tomatoes.open_movies_page(movies)
