from flask import Flask, render_template, session, url_for, flash
from flask import make_response
from flask import redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('what is your namex?', validators=[DataRequired()])
    submit = SubmitField('Submitx')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('looks like you have changed you name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
        # name = form.name.data
        # form.name.data = ''
    return render_template('indexx.html', form=form, name=session.get('name'))
    # return render_template('indexx.html', form=form, name=name)
    # return '<h1>Hello,Tiaoo!</h1>'
    # return render_template('indexx.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404x.html'), 404


@app.route('/user/<name>')
def user(name):
    # name=None
    # name=['a','b','v','d']
    # return render_template('user2.html', name=name)
    # return '<h1>Hello,{}!</h1>'.format(name)
    return render_template('userx.html', name=name)


@app.route('/test/ee')
def newresp():
    response = make_response('<h2> hello world2 <h2>')
    response.set_cookie('answer', '42')
    return response


@app.route('/fff')
def index2():
    return redirect('http://www.baidu.com')


if __name__ == '__main__':
    # 默认打开调试模式
    app.run(debug=True)
