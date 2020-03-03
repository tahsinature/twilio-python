from os import environ
from dotenv import load_dotenv
from cerberus import Validator

load_dotenv()

v = Validator()
v.allow_unknown = True

env_schema = {
    "TWILIO_ACCOUNT_SID": {
        "type": "string",
        "required": True
    },
    "TWILIO_AUTH_TOKEN": {
        "type": "string",
        "required": True
    },
    "TWILIO_PHONE_NUMBER": {
        "type": "string",
        "required": True
    }
}

env_vars = {
    "TWILIO_ACCOUNT_SID": environ.get("TWILIO_ACCOUNT_SID"),
    "TWILIO_AUTH_TOKEN": environ.get("TWILIO_AUTH_TOKEN"),
    "TWILIO_PHONE_NUMBER": environ.get("TWILIO_PHONE_NUMBER")
}


def check_env():
    is_env_valid = v.validate(env_vars, env_schema)
    if is_env_valid is not True:
        raise EnvironmentError('required vars not present')
