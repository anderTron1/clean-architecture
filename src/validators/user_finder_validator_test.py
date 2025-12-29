from .user_finder_validator import user_finder_validator
class MockRequest:
    def __init__(self):
        self.args = None

def test_user_finder_validator():
    query = MockRequest()
    query.args = {
        "first_name": "123"
    }
    user_finder_validator(query)