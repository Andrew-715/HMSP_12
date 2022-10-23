from flask import Blueprint, render_template, request
from Homework_Skypro.Homework_12.functions import *


showing_blueprint = Blueprint('showing_blueprint', __name__, template_folder='templates', url_prefix='/')

@showing_blueprint.route('/')
def photo_page():
    return render_template('index.html')


@showing_blueprint.route('/search')
def search_page():
    substr = request.args.get('s')
    posts = search_post(substr)
    return render_template('post_list', posts=posts, substr=substr)
