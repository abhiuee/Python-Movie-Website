class Movie():
    '''Class with four data members: title, storyline, poster image and
    youtube url. fresh_tomatoes.py works on this class data structure'''
    def __init__(self, title, storyline, poster_image, trailer):
        '''Constructor to initialize the class instance with the
        title, storyline, poster_image and trailer'''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer        
        
    
