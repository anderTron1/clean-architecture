from typing import Dict, List
from src.domain.user_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UserRepositoryInterface
from src.domain.models.users import Users

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UserRepositoryInterface) -> None:
        self.__user_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name)
        users = self.__search_user(first_name)
        response = self.__firmat_response(users)

        return response
    @classmethod
    def __validate_name(cls,first_name: str) -> None:
        if not first_name.isalpha():
            raise ValueError("Nome invalido para a busca")
        if len(first_name) > 18:
            raise ValueError("Nome muito grande para a busca")

    def __search_user(self, first_name: str) -> List[Users]:
        users = self.__user_repository.select_user(first_name)
        if users == []:
            raise ValueError("Usuario nao encontrado")
        return users

    @classmethod
    def __firmat_response(cls, users: List) -> Dict:
        attributes = []
        for user in users:
            attributes.append({
                "first_name": user.first_name,
                "age": user.age 
            })
        response = {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }
        return response