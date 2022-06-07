# api.py
import logging
from jsonschema import validate

from register.reqest import Client
from register.models import ResponseModel

logger = logging.getLogger("api")

class REQUEST:
    def __init__(self, url):
        self.url = url
        self.client = Client()


    def POST(self, body: dict, schema: dict, point: str):
        response = self.client.custom_request("POST", f"{self.url}{point}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def PUT(self, body: dict, point: str):
        response = self.client.custom_request("PUT", f"{self.url}{point}", json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def GET(self, body: dict, point: str):
        response = self.client.custom_request("GET", f"{self.url}{point}", json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def PATCH(self, body: dict, point: str):
        response = self.client.custom_request("PATCH", f"{self.url}{point}", json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())