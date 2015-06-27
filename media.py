import webbrowser
import urllib
import json

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        connection = urllib.urlopen("http://www.omdbapi.com/?t="+movie_title)
        output = connection.read()
        parsed_output = json.loads(output)
        self.runtime = parsed_output['Runtime']
        self.metascore = parsed_output['Metascore']

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


