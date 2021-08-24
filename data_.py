import datetime
import os

class Data(object):
    '''
    Collect log selection inputs and get all logs

    '''
    parent_path = 'C:/Users/Milton Savarimuthu/PycharmProjects/'


    def __init__(self, timeframe: datetime = None, package: str = None, comparison: bool = True):
        '''
        Iniatialize the object

        '''
        self.timeframe = timeframe
        self.package = package
        self.comparison = comparison

    def find_logs(self):
        '''
        Find the logs path based on given timeframe and package

        '''
        pass

    def is_directory_exist(self, path):
        '''
        :param path: validate if exist
        :return: bool

        '''
        return os.path.isdir(path)