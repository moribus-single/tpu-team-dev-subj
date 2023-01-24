import requests


class Request:
    def get_request(self, resource):
        response = requests.get(resource)
        return response
