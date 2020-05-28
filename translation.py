import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(input_file, output_file, source_lang, to_lang):
    with open(input_file, 'r', encoding='utf-8') as source:
        with open(output_file, 'a', encoding='utf-8') as receiving:
            data = source.read()
            params = dict(key=API_KEY, text=data, lang=source_lang + '-{}'.format(to_lang))
            response = requests.get(URL, params=params)
            json_ = response.json()
            receiving.write(''.join(json_['text']))
    return(output_file)

if __name__ == '__main__':
    translate_it('DE.txt', 'translated.txt', 'de', 'ru')
