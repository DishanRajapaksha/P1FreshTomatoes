#3/31/2016
#Dishan Rajapaksha

import media
import freshTomatoes

#Movie details
#Title, Description, Trailer link, Poser Image, Duration, Categories, Director and Releaser date

HP=media.Movie( "Harry Potter",
                "Rescued from the outrageous neglect of his aunt and uncle, a young boy with a great destiny proves his worth while attending Hogwarts School of Witchcraft and Wizardry.",
                "https://www.youtube.com/watch?v=PbdM1db3JbY",
                "http://ia.media-imdb.com/images/M/MV5BMTYwNTM5NDkzNV5BMl5BanBnXkFtZTYwODQ4MzY5._V1__SX1857_SY917_.jpg",
                "2h 32min",
                "Adventure, Family, Fantasy",
                "Chris Columbus",
                "16 November 2001 (UK)")
                
Martian=media.Movie("The Martian",
                    "During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. ",
                    "https://www.youtube.com/watch?v=Ue4PCI0NamI",
                    "http://ia.media-imdb.com/images/M/MV5BMTczMjc5NDExMF5BMl5BanBnXkFtZTcwNjkwNTY0Nw@@._V1__SX887_SY879_.jpg",
                    "1h 47min",
                    "Drama",
                    "Ridley Scott",
                    "30 September 2015 (UK)")
                    
OB=media.Movie("October Baby",
                "A college freshman's world is rocked when she learns she is the adopted survivor of a failed abortion",
                "https://www.youtube.com/watch?v=G7oTLVevO5g",
                "http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1__SX887_SY879_.jpg",
                "2h 24min",
                "Adventure, Drama, Sci-Fi",
                "Jon Erwin",
                "12 April 2013 (Spain)")

#Adding movies to an array to be passed                
movies = [HP,Martian,OB]

#Executing the openMoviesPage
freshTomatoes.openMoviesPage(movies)
