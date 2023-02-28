from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import (
    URL_LINK, CUSTOM_URL_LINK, SHORT_MAX_LEN,
    REQUIRED_FIELD, INVALID_URL_STR, INCORRECT_STRING_LENGTH,
    VALID_PATTERN_FOR_SHORT, INVALID_CHARACTERS, SUMBIT, LINK_CHAR_LIMIT)


class URLMapForm(FlaskForm):
    original_link = StringField(
        label=URL_LINK,
        validators=[
            DataRequired(message=REQUIRED_FIELD),
            URL(message=INVALID_URL_STR),
            Length(
                max=LINK_CHAR_LIMIT,
                message=INCORRECT_STRING_LENGTH.format(
                    limit=LINK_CHAR_LIMIT)
            )
        ]
    )
    custom_id = StringField(
        label=CUSTOM_URL_LINK,
        validators=[
            Length(
                max=SHORT_MAX_LEN,
                message=INCORRECT_STRING_LENGTH.format(
                    limit=SHORT_MAX_LEN)),
            Regexp(
                regex=VALID_PATTERN_FOR_SHORT,
                message=INVALID_CHARACTERS),
            Optional(strip_whitespace=True)
        ]
    )
    submit = SubmitField(SUMBIT)
