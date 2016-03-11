# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import inspect
import json
import pickle

from custom_exceptions import UserExitException
from models import BaseItem
from utils import get_input_function

__author__ = 'sobolevn'


class BaseCommand(object):
    def __init__(self, command):
        self._command = command

    @property
    def command(self):
        return self._command

    @staticmethod
    def label():
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        raise NotImplemented()


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():

        def class_filter(klass):
            return inspect.isclass(klass) \
                   and klass.__module__ == BaseItem.__module__ \
                   and issubclass(klass, BaseItem) \
                   and klass is not BaseItem

        classes = inspect.getmembers(
                sys.modules[BaseItem.__module__],
                class_filter
        )
        return dict(classes)

    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{}: {}'.format(index, name))

        input_function = get_input_function()
        selection = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                break
            except ValueError:
                print('Bad input, try again.')

        selected_key = list(classes.keys())[selection]
        selected_class = classes[selected_key]
        print('Selected: {}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct()

        objects.append(new_object)
        print('Added {}'.format(str(new_object)))
        print()
        return 1


class DoneCommand(BaseCommand):
    def __init__(self, command):
        super(DoneCommand, self).__init__(command)
        self.com_status = True

    @staticmethod
    def label():
        return 'done'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))

        input_function = get_input_function()

        selection = None

        while True:
            try:
                selection = int(input_function('\nSelect Item to complete: '))
                break
            except ValueError:
                print('Bad input, try again.')

        objects[selection].status = self.com_status

        print('Change status {} to {} \n\
         '.format(str(objects[selection]), str(objects[selection].status)))


class UndoneCommand (DoneCommand):
    def __init__(self, command):
        super(DoneCommand, self).__init__(command)
        self.com_status = False

    @staticmethod
    def label():
        return 'undone'


class SortCommand(BaseCommand):
    @staticmethod
    def label():
        return 'sort'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        input_function = get_input_function()
        sorting = None

        while True:
            try:
                sorting = int(input_function('Select criteria of sorting:\n\
1 - by status\n\
2 - by type\n'))
                break
            except ValueError:
                print('Bad input, try again.')

        if sorting == 1:
            objects.sort(key=lambda x: x.status)
        elif sorting == 2:
            objects.sort()

        print('Result of sorting:')
        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class SaveCommand(BaseCommand):
    @staticmethod
    def label():
        return 'save'

    def perform(self, objects, *args, **kwargs):
        with open(b"job_list.obj", 'wb') as job_list_w:
            pickle.dump(objects, job_list_w)

        print ('All jobs saved in file job_list.obj')

    # def perform(self, objects, *args, **kwargs):
    #     with open('job_list.txt', 'w') as f:
    #         for s in objects:
    #             f.write(str(s) + '\n')


class LoadCommand(BaseCommand):
    @staticmethod
    def label():
        return 'load'

    def perform(self, objects, *args, **kwargs):
        try:
            job_list_r = open("job_list.obj", 'rb')
            temp = pickle.load(job_list_r)
            for s in temp:
                objects.append(s)
            job_list_r.close()

            print ('Tasks list after loading:')
            for index, obj in enumerate(objects):
                print('{}: {}'.format(index, str(obj)))
        except IOError:
            print('No file to load!')


class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')
