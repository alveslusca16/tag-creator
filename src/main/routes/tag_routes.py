import time
from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

from src.errors.error_handler import handler_errors

from src.validators.tag_creator_validator import tag_creator_validator
from src.drivers.send_email import read_first_image_name
from src.drivers.send_email import send_email

tag_routes_bp = Blueprint('tag_routes', __name__)

@tag_routes_bp.route('/create_tag', methods = ["POST"])
def create_tags():
    response = None
    try:
        tag_creator_validator(request)
        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body = request.json)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as exception:
        response = handler_errors(exception)
    time.sleep(1)
    image_name = read_first_image_name()
    send_email(image_name)
    return jsonify(response.body), response.status_code
