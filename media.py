import webbrowser


class Movie:
    """ This class is used to define various functions of movies like __init__() and show_trailer()"""

    # function initializes the given parameters
    def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url

    # opens the link provided in web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
