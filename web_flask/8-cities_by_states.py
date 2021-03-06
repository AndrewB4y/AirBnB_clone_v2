#!/usr/bin/python3

""" 7-states_list module """

from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def rm_curr_SQLAlchemy(error):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def disp_states():
    """ display a HTML page with all the states stored """
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.route('/cities_by_states', strict_slashes=False)
def disp_state_cities():
    """
    Display a HTML page with all the states stored
    along with all the cities in those named states
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())

if __name__ == '__main__':
    app.run(debug=True)
