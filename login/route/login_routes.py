from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

login_api = Blueprint('login', __name__, url_prefix='/login')


@login_api.route('/', methods=('POST', 'GET'))
def get_chat_messages():
    print(request.method == 'POST')
    return render_template('login_template.html')
