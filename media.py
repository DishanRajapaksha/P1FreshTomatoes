# 3/31/2016
# Dishan Rajapaksha

import webbrowser

# Parent Class
class Video:
    """
    Initializes the Video class with following attributes
    Title, Description, Trailer link, Image location url and duration
    Parent class for the Movie class
    """
    def __init__(self, title, description, trailer, image, duration):
        self.Title = title
        self.Description = description
        self.Trailer = trailer
        self.Poster = image
        self.Duration = duration

    # Function to show the trailer
    def showTrailer(self):
        """
        Opens a new web browser window with the link given for the video trailer
        Needs webbrowser import to work
        """
        webbrowser.open(self.movieTrailer)

# Child Class
class Movie(Video):
    """
    This inherites video class with following added attributes.
    Movie categories if any, Director and the release date.
    """
    def __init__(self, title, description, trailer, image, duration, categories, director, date):
        Video.__init__(self, title, description, trailer, image, duration)
        self.Categories = categories
        self.Director = director
        self.Date = date
