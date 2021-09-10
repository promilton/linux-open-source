import json


class JSON(object):

    EXTENSION = ['.json', ]

    def __init__(self):

        pass

    @staticmethod
    def read(file_):

        with open(file_, 'r') as fp:
            print(json.load(fp))

    @staticmethod
    def write(dict_):

        with open('sample.json', 'w') as file_:
            json.dump(dict_, file_)


# obj = JSON()
# obj.write({'Milton': 'Male', 'Lax': 'Female'})
# obj.read('sample.json')