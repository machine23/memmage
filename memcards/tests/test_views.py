from django.test import TestCase


class TestIndex(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        assert resp.status_code == 200
        html = resp.content.decode('utf8')
        assert html.startswith('<!doctype html>')
        assert html.endswith('</html>')
        assert '<h1>Welcome</h1>' in html
