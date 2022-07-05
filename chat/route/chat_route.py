from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

chat_api = Blueprint('chat', __name__, url_prefix='/chat')


@chat_api.route('/', methods=('GET', 'POST'))
def get_chat_messages():
    print(request.method == 'POST')
    return render_template('chat_template.html')
