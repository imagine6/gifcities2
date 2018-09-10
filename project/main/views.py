# project/main/views.py


from flask import render_template, Blueprint, redirect, url_for, jsonify
from .forms import SearchForm
import json

main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/', methods=('GET', 'POST'))
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return search_results(form.searchterm.data)

    return render_template('main/index.html', form=form)


@main_blueprint.route("/results")
def search_results(search_query):
    search_results = query_API(search_query)
    return render_template('main/results.html', results=search_results, query=search_query)

def query_API(searchterm):
    tenor_apikey = "YOUR API KEY"
    return None
