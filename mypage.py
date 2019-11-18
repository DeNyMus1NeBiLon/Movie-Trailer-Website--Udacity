import webbrowser


class Movie():
    def __init__(self, movie_title, m_story_l, poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = m_story_l
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        print(self.trailer)
        webbrowser.open(self.trailer)
