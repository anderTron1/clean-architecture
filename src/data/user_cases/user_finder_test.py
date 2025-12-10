from .user_finder import UserFinder
from src.infra.db.repositories.users_repository import UserRepository

def test_find():
    repo = UserRepository()
    user_finder = UserFinder(repo)