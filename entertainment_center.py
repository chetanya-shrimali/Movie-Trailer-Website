import fresh_tomatoes
import media

# movies start here
# media.Movie(title, description, image_url, youtube_trailer_url)
whiplash = media.Movie('Whiplash',
                       "A young and talented drummer attending a prestigious "
                       "music academy finds himself under the "
                       "wing of the most respected professor at the school, "
                       "one who does not hold back on abuse "
                       "towards his students. The two form an odd "
                       "relationship as the student wants to achieve "
                       "greatness, and the professor pushes him.",
                       "https://i.jeded.com/i/whiplash.34229.jpg",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

american_beauty = media.Movie('American Beauty',
                              "A sexually frustrated suburban father has a "
                              "mid-life crisis after becoming infatuated "
                              "with his daughter's best friend.",
                              "https://upload.wikimedia.org/wikipedia/en/b/b6"
                              "/American_Beauty_poster.jpg",
                              "https://www.youtube.com/watch?v=3ycmmJ6rxA8")

forest_gump = media.Movie('Forest Gump',
                          "While not intelligent, Forrest Gump has "
                          "accidentally been present at many historic "
                          "moments, but his true love, Jenny Curran, eludes "
                          "him.",
                          "https://en.wikipedia.org/wiki/Forrest_Gump#/media"
                          "/File:Forrest_Gump_poster.jpg",
                          "https://www.youtube.com/watch?v=uPIEn0M8su0")

shawshank_redemption = media.Movie('Shawshank Redemption',
                                   "Two imprisoned men bond over a number of "
                                   "years, finding solace and eventual "
                                   "redemption through acts of"
                                   " common decency.",
                                   "https://upload.wikimedia.org/wikipedia/en"
                                   "/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco"
                                   )

batman_dark_knight = media.Movie('Batman Dark Knight',
                                 "When the menace known as the Joker emerges "
                                 "from his mysterious past, he wreaks "
                                 "havoc and chaos on the people of Gotham, "
                                 "the Dark Knight must accept one of the "
                                 "greatest psychological and physical tests "
                                 "of his ability to fight injustice.",
                                 "https://upload.wikimedia.org/wikipedia/en/8"
                                 "/8a/Dark_Knight.jpg",
                                 "https://www.youtube.com/watch?v=EXeTwQWrcwY")

school_of_rock = media.Movie('School Of Rock',
                             "After being kicked out of a rock band, Dewey "
                             "Finn becomes a substitute teacher of a "
                             "strict elementary private school, only to try "
                             "and turn it into a rock band.",
                             "https://en.wikipedia.org/wiki/School_of_Rock"
                             "#/media/File:School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# list of movies
movies_list = [whiplash, american_beauty, forest_gump, shawshank_redemption,
               batman_dark_knight, school_of_rock]

# function takes the list as parameter and outputs the webpage.
fresh_tomatoes.open_movies_page(movies_list)

# prints the documentation of the Movie class in media file
print(media.Movie.__doc__)
