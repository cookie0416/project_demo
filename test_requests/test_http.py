import requests


class TestHttp:
    def test_get(self):
        r = requests.get('https://ceshiren.com/')
        print(r)

    def test_get_query(self):
        url = "http://httpbin.org/get"
        r = requests.get(url)
        print(r.url)

    def test_get_login(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        assert data['topics'][0]['user']['login'] == 'guolong123'
