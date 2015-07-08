"""This module containts all movie data.

All data is hardcoded in each move entry. It then creates a list of all the
movies and calls the open_movies_page method to display them.
"""
import fresh_tomatoes
import media


goodfellas = media.Movie("Goodfellas", "Henry Hill and his friends work their \
way up through the mob hierarchy", "http://wallpapers111.com/wp-content/\
uploads/2015/03/goodfellas-wallpaper-hd.jpg", "https://youtu.be/YH-7he92XfI")

shawshank_redemption = media.Movie("The Shawshank Redemption", "Two \
imprisoned men bond over a number of years, finding solace and eventual \
redemption through acts of common decency", "http://upload.wikimedia.org/\
wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", "https://youtu.be/\
6hB3S9bIaco")

royal_tenenbaums = media.Movie("The Royal Tenenbaums", "An estranged family \
of former child prodigies reunites when their father announces he is \
terminally ill", "http://upload.wikimedia.org/wikipedia/en/3/3b/\
The_Tenenbaums.jpg", "https://youtu.be/HaMfV72q40U")

mama_tambien = media.Movie("Y Tu Mama También", "In Mexico, two teenage boys \
and an attractive older woman embark on a road trip and learn a thing or two \
about life, friendship, sex, and each other", "https://upload.wikimedia.org/\
wikipedia/en/6/63/Y_tu_mamá_también_poster.png", "https://youtu.be/\
3Qg6n7V3kO4")

sideways = media.Movie("Sideways", "Two men reaching middle age with not much \
to show but disappointment, embark on a week long road trip through \
California's wine country, just as one is about to take a trip \
down the aisle", "http://upload.wikimedia.org/wikipedia/en/f/ff/\
Sideways_poster.JPG", "https://youtu.be/YS9ocP6FNvM")

wolf_of_wallstreet = media.Movie("The Wolf Of Wall Street", "Based on the \
true story of Jordan Belfort, from his rise to a wealthy stock-broker living \
the high life to his fall involving crime, corruption and the federal \
government", "http://upload.wikimedia.org/wikipedia/en/1/1f/\
WallStreet2013poster.jpg", "https://youtu.be/iszwuX1AK6A")

movies = [goodfellas, wolf_of_wallstreet, sideways, royal_tenenbaums,
          shawshank_redemption, mama_tambien]
fresh_tomatoes.open_movies_page(movies)
