'''
Main Application and routing logic for TwitOff
'''

from decouple import config
from flask import Flask, request, render_template, redirect, url_for
from .models import DB, User


def create_app():
    '''
        Create and configure an instance of the Flask application.
    '''

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['ENV'] = config('ENV') #TODO change before deploy 'debug'

    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('index.html', title='Home', users=users)

    # @app.route('/user', methods=['POST'])
    # @app.route('/user/<name>', methods=['GET'])
    # def user(name=None):
    #     message= ''
    #     name = name or request.values['user_name']

    #     try:
    #         if request.method == 'POST':
    #             # add_or_update_user(name)

    #             message = 'User {} successfully added!'.format(name)
    #         tweets = User.query.filter(User.name == name).one().tweets
    #     except Exception as e:
    #         message = 'Error adding{}'

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('index.html', title='DB Reset!', users=[])

    return app

