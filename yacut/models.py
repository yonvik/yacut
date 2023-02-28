import re
from datetime import datetime
from random import sample
from urllib.parse import urlparse

from flask import url_for

from . import db
from .constants import (
    LINK_CHAR_LIMIT, SHORT_MAX_LEN, RANDOM_ITERATION, RANDOM_LINK_LENGTH,
    CHARACTERS_SET, OUT_COMBINATIONS, INVALID_URL_FORMAT, VALID_PATTERN_FOR_SHORT,
    INVALID_SHORT_LINK, DUPLICATE_SHORT_LINK
)
from .error_handlers import ModelValidationError


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(LINK_CHAR_LIMIT), nullable=False)
    short = db.Column(db.String(SHORT_MAX_LEN), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @staticmethod
    def get(custom_id):
        return URLMap.query.filter_by(short=custom_id).first()

    @staticmethod
    def get_unique_short_id():
        for _ in range(RANDOM_ITERATION):
            random_link = ''.join(
                sample(CHARACTERS_SET, RANDOM_LINK_LENGTH))
            if URLMap.get(random_link) is None:
                return random_link
        raise ModelValidationError(OUT_COMBINATIONS)

    @staticmethod
    def create_on_validation(url, custom_id=None, validate=False):
        if validate:
            if not len(url) <= LINK_CHAR_LIMIT:
                raise ValueError(INVALID_URL_FORMAT.format(url=url))
        url_parts = urlparse(url)
        if not (url_parts.netloc and url_parts.scheme in ('http', 'https')):
            raise ModelValidationError(INVALID_URL_FORMAT.format(url=url))
        if not custom_id:
            custom_id = URLMap.get_unique_short_id()
        elif validate:
            if len(custom_id) > SHORT_MAX_LEN:
                raise ModelValidationError(INVALID_SHORT_LINK)
            if not re.match(VALID_PATTERN_FOR_SHORT, custom_id):
                raise ModelValidationError(INVALID_SHORT_LINK)
        if URLMap.get(custom_id):
            raise ModelValidationError(DUPLICATE_SHORT_LINK.format(
                short_link=custom_id))
        urlmap = URLMap(original=url, short=custom_id)
        db.session.add(urlmap)
        db.session.commit()
        return urlmap

    @property
    def fully_qualified_short_link(self):
        return url_for(
            'redirect_to_full_link',
            shortcut=self.short, _external=True)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=self.fully_qualified_short_link
        )
