#!/usr/bin/env python
# coding: utf-8
import shutil
import os


class Requester:
    '''
    Какой-то класс, который умеет делать запросы
     к удаленному серверу
    '''
    def get(self, host, port, filename):
        return "Fail"

    def post(self, host, port, filename, data):
        return False


class RemoteFileReader(Requester):
    '''
    Класс для работы с файлами на удаленном сервере
    '''
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def read_file(self, filename):
        return super().get(self._host, self._port, filename)

    def write_file(self, filename, data):
        return super().post(self._host, self._port, filename, data)


class OrdinaryFileWorker(RemoteFileReader):
    '''
    Класс, который работает как с локальными
     так и с удаленными файлами
    '''
    def transfer_to_remote(self, filename):
        with open(filename, "r") as f:
            super().write_file(filename, f.readlines())

    def transfer_to_local(self, filename):
        with open(filename, "w") as f:
            f.write(super().read_file(filename))


class MockOrdinaryFileWorker(OrdinaryFileWorker):
        def __init__(self):
            self.path_test = "./homeworks/homework_03/test_dir/"
            self.path_tmpf = "./tmpf/"
            try:
                os.mkdir(self.path_tmpf)
            except:
                pass

        def transfer_to_local(self, filename):
            with open('{0}{1}{2}'.format(self.path_test, filename, '.tmp'), 'r') as fromfile:
                with open(self.path_tmpf + filename, 'w') as tof1ile:
                    tof1ile.writelines(fromfile.read())

        def transfer_to_remote(self, filename):
            with open(self.path_test + filename, 'r') as fromfile:
                with open('{0}{1}{2}'.format(self.path_tmpf, filename, '.tmp'), 'w') as tof1ile:
                    tof1ile.writelines(fromfile.read())

        def __del__(self):
            if os.path.exists(self.path_tmpf):
                shutil.rmtree(self.path_tmpf)


class LLNode:
    def __init__(self, value, next_node):
        """
        Entity (or node) for doubly linked list
        :param value: object
        :param next_node: LLEntity
        """
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return "value: {}; next_node: ({})".format(self.value, self.next_node)
