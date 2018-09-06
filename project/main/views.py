# project/main/views.py


from flask import render_template, Blueprint
from .forms import GIFform


main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/', methods=('GET', 'POST'))
def search():
    search = GIFform()
    if search.validate_on_submit():
        return search_results(search.searchterm.data)

    return render_template('main/index.html', form=search)


@main_blueprint.route("/results")
def search_results(results):

    return render_template("main/results.html")


def get_GIFs(searchterm):
    pass


