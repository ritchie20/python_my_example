#flask-babel = extention to multi-language sites
#flask-wtf = extention to work fith forms


from flask import render_template, url_for, flash, redirect, request
from flask.ext.babel import gettext
from app import app, babel
from .datos import Dato
from .forms import EditForm
from config import LANGUAGES

@app.route('/')

@app.route('/index')
def index():
    user = {'nickname': 'Oscar'}
    posts = [
        {
            'author': {'nickname': 'Jhon'},
            'body': 'Beautiful day in portland'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)


@app.route('/datos')
def datos():
    data = Dato()
    return render_template('datos.html',
                            data=data)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    if form.validate_on_submit():
        valor1 = form.texto1.data
        valor2 = form.texto2.data
        archivo = open('texto.txt', 'w')
        archivo.write(valor1)
        archivo.close()
        flash(gettext('this is a flash test, text saved'))
        return redirect(url_for('index'))
    else:
        form.texto1.data = 'Test nick'
        form.texto2.data = 'Test text'
    return render_template('edit.html', form=form)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

