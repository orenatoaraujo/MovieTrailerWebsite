class Movie():
    """
    This class provides a way to store movie related information
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Instance a new movie with the follow information title,
        post image url and trailer youtube url
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
