from project2_Flask import app, forms
from flask import request, render_template


@app.route('/',methods=['GET','POST'])
def search():
    my_form = forms.NewsForm(request.form)

    if request.method == "POST":
        first_name = request.form["first_name"]
        genre = request.form['genre']
        movie_name = request.form['movie_name']

        response = [first_name, genre, movie_name, forms.generateDataFromAPI(movie_name)]

        return render_template('results.html',response=response, form=my_form)

    return render_template('search.html', form=my_form)

@app.route('/greeting')
def greeting():
    first_name = "Luis"
    last_name = "Alberto"
    return "I am {0} {1}.".format(first_name,last_name)