import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UserRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensietive test")
def test_insert_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 34

    users_respository = UserRepository()
    users_respository.insert_user(
        first_name=mocked_first_name,
        last_name=mocked_last_name,
        age=mocked_age)

    sql = (
        f"SELECT * FROM users  WHERE first_name='{mocked_first_name}' "
        f"AND last_name='{mocked_last_name}' AND age={mocked_age}"
    )

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registry.id}
    '''))
    connection.commit()

@pytest.mark.skip(reason="Sensietive test")
def test_select_user():
    mocked_first_name = "first2"
    mocked_last_name = "last2"
    mocked_age = 44

    sql = (
        f"INSERT INTO users (first_name, last_name, age) "
        f"values ('{mocked_first_name}', '{mocked_last_name}', {mocked_age})"
    )
    connection.execute(text(sql))
    connection.commit()

    users_repository = UserRepository()
    response = users_repository.select_user(first_name=mocked_first_name)

    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age

    connection.execute(text(f'''
        DELETE FROM users WHERE first_name = '{mocked_first_name}'
    '''))
    connection.commit()