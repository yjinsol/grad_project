import requests
from requests_file import FileAdapter

def get_url_contents(url):
    s = None
    try:
        s = requests.Session()
        if url.lower().startswith('file://'):
            s.mount('file://', FileAdapter())
            resp = s.get(url)
        else:
            resp = s.get(url)
        return resp.status_code, resp.text
    finally:
        if s is not None:
            s.close()


def test_02():
    url = 'file:///etc/hosts'
    sc, fc = get_url_contents(url)
    print('url="%s"\nsc=%s\nfc=<%s>' % (url, sc, fc))

    url = 'http://localhost:8000/setup.py'
    sc, fc = get_url_contents(url)
    print('url="%s"\nsc=%s\nfc=<%s>' % (url, sc, fc))

if __name__ == '__main__':
    test_02()