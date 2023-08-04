"""User Service class"""
import logging
from http import HTTPStatus as http_status
import src.common.response as response


logger = logging.getLogger(name=__name__)
class UserService:
    """User Service class
    """
    
    def __init__(self) -> None:
        logger.debug("User service class constructor is called")
        pass
    
    def get_many(self):
        logger.debug("Called get_many from the controller ")
        users = {
            {
                'id': 12,
                'first_name': 'Gopi Krishna',
                'last_name': 'm',
                'email': 'fromgopi@tendermilk.com'
            }
        }
        return response.success(http_status.OK, 'users', users, meta=None)