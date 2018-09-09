# project/main/views.py


from flask import render_template, Blueprint, redirect, url_for, jsonify
from .forms import SearchForm


main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/', methods=('GET', 'POST'))
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return search_results(form.searchterm.data)

    return render_template('main/index.html', form=form)


@main_blueprint.route("/results")
def search_results(results):

    return query_API(results)


def query_API(searchterm):
    tenor_api_key = "YOUR API KEY"
    return jsonify({"Searchterm": searchterm})