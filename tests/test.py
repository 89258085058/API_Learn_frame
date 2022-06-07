from register.api import REQUEST
from register.models import RegisterUser
from schemas.registration import valid_schema

URL = "https://stores-tests-api.herokuapp.com"

REGISTER_USER = '/register'

class TestRegistration:

    def test_registration(self):
        body = RegisterUser.random()
        response = REQUEST(url=URL).POST(body=body, point=REGISTER_USER, schema=valid_schema)
        assert response.status == 201
        assert response.response.get('message') == 'User created successfully.'
        assert response.response.get('uuid')

    def test_registration_put(self):
        body = RegisterUser.random()
        response = REQUEST(url=URL).PUT(body=body, point=REGISTER_USER)
        assert response.status == 405
        assert response.response.get('message') == 'The method is not allowed for the requested URL.'

    def test_registration_get(self):
        body = RegisterUser.random()
        response = REQUEST(url=URL).GET(body=body, point=REGISTER_USER)
        assert response.status == 405
        assert response.response.get('message') == 'The method is not allowed for the requested URL.'

    def test_registration_patch(self):
        body = RegisterUser.random()
        response = REQUEST(url=URL).PATCH(body=body, point=REGISTER_USER)
        assert response.status == 405
        assert response.response.get('message') == 'The method is not allowed for the requested URL.'


