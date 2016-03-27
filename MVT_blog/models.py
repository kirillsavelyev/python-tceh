# -*- coding: utf-8 -*-

import datetime
import json


class Storage(object):
    obj = None
    items = None
    posts_buffer = {}

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj

    @classmethod
    def dump_to_json_file(cls):
        cls.posts_buffer['items'] = []
        with open('/media/ska/ESD-USB/Python/Repository/MVT_blog/posts_dump.json', 'w') as json_file:
            for item in cls.items:
                cls.posts_buffer['items'].append(item.__dict__)
            json.dump(cls.posts_buffer, json_file)

    @classmethod
    def load_from_json_file(cls):
        try:
            Storage.__new__(cls)
            with open('/media/ska/ESD-USB/Python/Repository/MVT_blog/posts_dump.json') as json_file:
                json_data = json.load(json_file, )
            if json_data:
                for post in json_data['items']:
                    item = BlogPostModel(post, True)
                    cls.items.append(item)
        except IOError:
            print('No json file!')
        except ValueError:
            print ('Error load json!')


class BlogPostModel(object):
    def __init__(self, form_data, loading_items=False):
        self.text = form_data['text']
        self.name = form_data['name']
        self.title = form_data['title']
        if loading_items:
            self.date = form_data['date']
        else:
            self.date = datetime.datetime.now().strftime('%Y.%m.%d - %H:%M')
