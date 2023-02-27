from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import (
    URL_LINK, CUSTOM_URL_LINK, SHORT_MAX_LEN,
    REQUIRED_FIELD, INVALID_URL_STR, INCORRECT_STRING_LENGTH,
    REGULAR, INVALID_CHARACTERS, SUMBIT)


class URLMapForm(FlaskForm):
    original_link = StringField(
        label=URL_LINK,
        validators=[
            DataRequired(message=REQUIRED_FIELD),
            URL(message=INVALID_URL_STR)
        ]
    )
    custom_id = StringField(
        label=CUSTOM_URL_LINK,
        validators=[
            Length(
                min=1,
                max=SHORT_MAX_LEN,
                message=INCORRECT_STRING_LENGTH.format(
                    limit=SHORT_MAX_LEN)),
            Regexp(
                regex=REGULAR,
                message=INVALID_CHARACTERS),
            Optional(strip_whitespace=True)
        ]
    )
    submit = SubmitField(SUMBIT)
