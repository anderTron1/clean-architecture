#pylint: disable=use-implicit-booleaness-not-comparison
#pylint: disable=broad-exception-caught
#pylint: disable=wrong-import-order
from .user_finder import UserFinder
from src.infra.db.tests.users_repository import UserRepositorySpy

def test_find():
    first_name = 'meunome'

    repo = UserRepositorySpy()
    user_finder = UserFinder(repo)
    response = user_finder.find(first_name)

    print(response)
    print()
    assert repo.select_user_attributes["first_name"] == first_name
    assert response["type"] == "Users"
    assert response["count"] == 5
    assert response["attributes"] != []

def test_find_error_in_valid_name():
    first_name = "meuNome123"

    repo = UserRepositorySpy()
    use_finder = UserFinder(repo)
    try:
        use_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome invalido para a busca"

def test_find_error_in_to_long_name():
    first_name = "meuNomelaksjflsldkflskdflkelasdfasdf"

    repo = UserRepositorySpy()
    use_finder = UserFinder(repo)
    try:
        use_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome muito grande para a busca"

def test_find_error_user_not_found():
    class UsersRepositoryError(UserRepositorySpy):
        def select_user(self, first_name: str):
            return []
    first_name = "meuNome"

    repo = UsersRepositoryError()
    use_finder = UserFinder(repo)
    try:
        use_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Usuario nao encontrado"