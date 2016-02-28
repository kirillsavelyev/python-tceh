# -*- coding: utf-8 -*-

from utils import get_input_function

__author__ = 'sobolevn'


class Storage(object):
    obj = None

    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.status = False

    def __repr__(self):
        return self.__class__

    # def __getitem__(self, item):
    #     return self.__dict__

    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToDoItem(BaseItem):
    def __str__(self):
        return '{} ToDo: {}'.format('+' if self.status else '-', self.heading)

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        return ToDoItem(heading)


class ToBuyItem(BaseItem):
    def __init__(self, heading, price):
        super(ToBuyItem, self).__init__(heading)
        self.price = price

    def __str__(self):
        return '{} ToBuy: {} for {}\
'.format('+' if self.status else '-', self.heading, self.price)

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price)


class ToReadItem(BaseItem):
    def __init__(self, heading, link, due_date):
        super(ToReadItem, self).__init__(heading)
        self.link = link
        self.due_date = due_date

    def __str__(self):
        return '{} ToRead: {} {} {}\
'.format('+' if self.status else '-', self.heading, self.link, self.due_date)

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        link = input_function('Input link: ')
        due_date = input_function('Input due date: ')
        return ToReadItem(heading, link, due_date)
