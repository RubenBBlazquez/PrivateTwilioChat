from chat.route.chat_route import chat_api
from login.route.login_routes import login_api
from flask import Flask, redirect

app = Flask(__name__, static_url_path='/static')

app.register_blueprint(chat_api)
app.register_blueprint(login_api)
app.route('/login')


@app.route('/')
def flask_init():
    return redirect('/login/')


if __name__ == '__main__':
    app.run()
