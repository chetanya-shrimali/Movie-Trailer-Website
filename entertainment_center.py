import fresh_tomatoes
import media

# movies start here
# media.Movie(title, description, image_url, youtube_trailer_url)
whiplash = media.Movie('Whiplash',
                       "A young and talented drummer attending a prestigious music academy finds himself under the wing of the most respected professor at the school, one who does not hold back on abuse towards his students. The two form an odd relationship as the student wants to achieve greatness, and the professor pushes him.",
                       "https://i.jeded.com/i/whiplash.34229.jpg",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

american_beauty = media.Movie('American Beauty',
                              "A sexually frustrated suburban father has a mid-life crisis after becoming infatuated with his daughter's best friend.",
                              "https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_poster.jpg",
                              "https://www.youtube.com/watch?v=3ycmmJ6rxA8")

forest_gump = media.Movie('Forest Gump',
                          "While not intelligent, Forrest Gump has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY1200_CR139,0,630,1200_AL_.jpg",
                          "https://www.youtube.com/watch?v=uPIEn0M8su0")

shawshank_redemption = media.Movie('Shawshank Redemption',
                                   "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

batman_dark_knight = media.Movie('Batman Dark Knight',
                                 "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                                 "https://www.youtube.com/watch?v=EXeTwQWrcwY")

school_of_rock = media.Movie('School Of Rock',
                             "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.",
                             "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# list of movies
movies_list = [whiplash, american_beauty, forest_gump, shawshank_redemption, batman_dark_knight, school_of_rock]

# function takes the list as parameter and outputs the webpage.
fresh_tomatoes.open_movies_page(movies_list)

# prints the documentation of the Movie class in media file
print(media.Movie.__doc__)
