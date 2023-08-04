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
        data = [
            {
                'id': 12,
                'first_name': 'Gopi Krishna',
                'last_name': 'm',
                'email': 'fromgopi@tendermilk.com'
            },
            {
                'id': 42,
                'first_name': 'Rama Krishna',
                'last_name': 'm',
                'email': 'fromrama@tendermilk.com'
            }
        ]
        return response.success(http_status.OK, 'users', data, meta=None)