"""USERS END POINTS"""
from flask import Blueprint, request
from sqlalchemy import exc
from src.common.exceptions import ApiError
import src.common.response as response
from src.app.user.services.user_services import UserService

USER_API = Blueprint('users', __name__)

@USER_API.route('/users', methods=['GET'])
def get_many():
    """
    Get many / all users
    """
    try:
        return UserService().get_many()
    except (ApiError, ValueError, TypeError, exc.SQLAlchemyError) as error:
        return response(error)