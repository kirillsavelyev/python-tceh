# -*- coding: utf-8 -*-

import requests

def get_habrahabr():
    r = requests.get('http://habrahabr.ru')
    print(r.status_code)
    print(r.headers)
    print(r.content)


def find_pet_by_tag(tag):
    params = {'tags': tag}
    headers = {
        'Accept': 'application/xml'
        # 'Accept': 'application/json'
    }
    url = 'https://habrahabr.ru/users/imperituroard/'
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code, r.headers)
    # print(r.content)

    # s = 'http://petstore.swagger.io/v2/pet/89?tags=string&filter=sad'


if __name__ == '__main__':
    get_habrahabr()
    # find_pet_by_tag('string')