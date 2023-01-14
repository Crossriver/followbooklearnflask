from flask import Flask, render_template
from flask import make_response
from flask import redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('extendsdemo.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/user/<name>')
def user(name):
    # name=None
    # name=['a','b','v','d']
    return render_template('user2.html', name=name)


@app.route('/test/ee')
def newresp():
    response = make_response('<h2> hello world2 <h2>')
    response.set_cookie('answer', '42')
    return response


@app.route('/fff')
def index2():
    return redirect('http://www.baidu.com')


if __name__ == '__main__':
    app.run(debug=True)
