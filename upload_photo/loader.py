import logging
from flask import Blueprint, render_template, request
from Homework_Skypro.Homework_12.functions import *

upload_blueprint = Blueprint('upload_blueprint', __name__, template_folder='templates', url_prefix='/')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@upload_blueprint.route('/post')
def create_post():
    return render_template('post_form.html')


@upload_blueprint.route('/post', methods=['POST'])
def upload_post():
    picture = request.files.get('picture')
    content = request.form.get('content')
    picture_url = save_picture(picture)

    if not picture_url:
        logging.info(f'{picture_url}: не изображение!')
        return 'Это не изображение!'

    add_post({'pic': picture_url, 'content': content})

    return render_template('post_uploaded.html', picture_url=picture_url, content=content)