#3/31/2016
#Dishan Rajapaksha

import webbrowser

#Parent Class
class Video:
    def __init__(self, title, description, trailer, image, duration):
        self.Title = title
        self.Description = description
        self.Trailer = trailer
        self.Poster = image
        self.Duration = duration
        
    #Function to show the trailer    
    def showTrailer(self):
        webbrowser.open(self.movieTrailer)

#Child Class
class Movie(Video):
    def __init__(self, title, description, trailer, image, duration, categories, director, date):
        Video.__init__(self, title, description, trailer, image, duration)
        self.Categories = categories
        self.Director = director
        self.Date = date
        
                

