import requests
import shutil

API_URL = 'https://github.com/muhammete1/deneme'
API_KEY = 'bunu simdilik bosver'

headers = {'UserAPI-Key': API_KEY}

response = requests.get(
    '{}/static/test.py'.format(API_URL), headers=headers
)
url = '{}/static/test.py'.format(API_URL)


def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename


download_file(url)