import requests
import get_hashes
import translation

YD_API_KEY = 'OAuth AgAAAAALEsDgAADLW46LfP_vYEcnmHJjisMe4Yk'

def get_key():
    YD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    headers = {
        'Authorization': YD_API_KEY,
    }
    params = {
        'path': 'translation.txt'
    }
    response = requests.get(YD_URL, headers = headers, params=params).json()
    return(response['href'])

def yd_upload(up_link, file):
    md = get_hashes.get_md5(file)
    sha = get_hashes.get_sha(file)
    URL = up_link
    headers = {
        'Authorization': YD_API_KEY,
        'Transfer - Encoding': 'chunked',
        'Etag': md,
        'Sha256': sha,
        'Content-Type': 'text/html; charset=UTF-8'
    }
    params = {
        'path': 'translation.txt',
    }
    with open (file, encoding='utf-8') as up_file:
        content = up_file.read().encode('utf-8')
        requests.put(URL, data = content, headers=headers, params=params)



def main():
    yd_upload(get_key(), translation.translate_it('DE.txt', 'translated.txt', 'de', 'ru'))

main()
