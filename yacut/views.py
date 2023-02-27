from random import sample
from http import HTTPStatus

from flask import abort, flash, redirect, render_template

from . import app, db
from .constants import (
    DUPLICATE_SHORT_LINK,
    COMPLITE_LINK,
    CHARACTERS_SET,
    RANDOM_LINK_LENGTH
)
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    random_link = ''.join(sample(CHARACTERS_SET, RANDOM_LINK_LENGTH))
    while URLMap.query.filter_by(original=random_link).first():
        return get_unique_short_id()
    else:
        return random_link


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        input_long, input_short = form.original_link.data, form.custom_id.data
        if input_short and URLMap.query.filter_by(short=input_short).first():
            flash(DUPLICATE_SHORT_LINK.format(
                short_link=input_short, end='!'))
            return render_template('index.html', form=form)
        url_map = URLMap(
            original=input_long,
            short=input_short or get_unique_short_id()
        )
        db.session.add(url_map)
        db.session.commit()
        flash(COMPLITE_LINK)
        return (
            render_template(
                'index.html', form=form, shortcut=url_map.short),
            HTTPStatus.OK)
    return render_template('index.html', form=form), 200


@app.route('/<string:shortcut>')
def redirect_to_full_link(shortcut):
    link_pair = URLMap.query.filter_by(short=shortcut).first()
    if link_pair:
        return redirect(link_pair.original)
    else:
        abort(404)
