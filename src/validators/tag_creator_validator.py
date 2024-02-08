from cerberus import Validator
from src.errors.error_types.htttp_unprocessable_entity import HttpUnprocessableEntityyError

def tag_creator_validator(request: any) -> None:
    body_validator = Validator({
        "product_code": {"type": "string", "required": True, "empty": False}
    })
    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityyError(body_validator.errors)
