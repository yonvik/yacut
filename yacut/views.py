from http import HTTPStatus

from flask import abort, flash, redirect, render_template

from . import app
from .constants import ERROR_REPEAT_NAME
from .error_handlers import ModelValidationError
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form), 200
    input_long = form.original_link.data
    input_short = form.custom_id.data
    if input_short and URLMap.get(input_short):
        flash(ERROR_REPEAT_NAME.format(
            short_link=input_short))
        return render_template('index.html', form=form)
    try:
        url_map = URLMap.create_on_validation(input_long, input_short)
        return (
            render_template(
                'index.html',
                form=form,
                shortcut=url_map.fully_qualified_short_link),
            HTTPStatus.OK)
    except (ModelValidationError, ValueError) as error:
        flash(error.message)
        return render_template('index.html', form=form)


@app.route('/<string:shortcut>')
def redirect_to_full_link(shortcut):
    link_pair = URLMap.get(shortcut)
    if link_pair:
        return redirect(link_pair.original)
    abort(404)
