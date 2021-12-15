import configparser

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        return config.get('common info', 'baseUrl')

    @staticmethod
    def getUsername():
        return config.get('common info', 'username')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')
