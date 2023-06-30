import requests as requests

base_url = 'https://czbe.qa.webcluesstaging.com/api/v1/'


class api_call:
    def api_login(self):
        global token
        resp = requests.post(f"{base_url}auth/login", json={
            "email": "admin1@admin.com",
            "password": "admin@123456",
            "checked": "true"}, headers=self._get_header())
        assert resp.status_code == 201, print("pass")
        token = resp.json().get('token')

    def get_role_list(self):
        resp = requests.get(base_url + 'roles', headers=self._get_header(Authorization=f'Bearer {token}'))
        print(resp.json())

    def _get_header(self, **kwargs):
        header = {'Content-type': "application/json"}
        header.update(**kwargs)
        print(header)
        return header


api_call().api_login()
api_call().get_role_list()
