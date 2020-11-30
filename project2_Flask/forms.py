from flask_wtf import FlaskForm
from project2_Flask import main_functions
from wtforms import StringField, IntegerField, SelectField, RadioField
import requests


class NewsForm(FlaskForm):
    first_name = StringField("First Name")
    panther_id = IntegerField("Panther ID")
    genre = RadioField("Movie Genre",
                       choices=[('horror', 'Horror'),
                                ('action', 'Action'),
                                ('drama', 'Drama')])
    movie_name = SelectField("Movie Options",
                        choices=[('pulp fiction', 'Pulp Fiction'),
                                ('parasite', "Parasite"),
                                ('slumdog millionaire', "Slumdog Millionaire")])


def generateDataFromAPI(movie_name):
    my_key_dict = main_functions.read_from_file("project2_Flask/JSON_Documents/api_keys.json")
    my_key = my_key_dict["my_ny_key"]
    url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=" + movie_name + "&api-key=" + my_key

    response = requests.get(url).json()

    main_functions.save_to_file(response, "project2_Flask/JSON_Documents/response.json")

    response_dict = main_functions.read_from_file("project2_Flask/JSON_Documents/response.json")

    # from the response dictionary you need to filter the data requested by the user

    return response_dict["results"]
