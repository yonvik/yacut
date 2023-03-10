from http import HTTPStatus

from flask import request, jsonify

from . import app
from .constants import EMPTY_REQUEST, FIELDS_MISSING, MISSING_ID
from .error_handlers import InvalidAPIUsage, ModelValidationError
from .models import URLMap


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_full_link(short_id):
    link = URLMap.get(short_id)
    if not link:
        raise InvalidAPIUsage(MISSING_ID, 404)
    return jsonify({'url': link.original})


@app.route('/api/id/', methods=['POST'])
def create_shortcut():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(EMPTY_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsage(FIELDS_MISSING.format(field='url'))
    try:
        return (
            jsonify(
                URLMap.create_on_validation(
                    data['url'], data.get('custom_id'), True
                ).to_dict()
            ),
            HTTPStatus.CREATED
        )
    except ModelValidationError as error:
        raise InvalidAPIUsage(message=error.message)
