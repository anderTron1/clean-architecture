from typing import Dict
from src.domain.user_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UserRepositoryInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UserRepositoryInterface) -> None:
        self.__user_repository = users_repository

    def find(self, first_name: str) -> Dict:
        pass