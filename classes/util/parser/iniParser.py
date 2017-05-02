import configparser, sys, os



class iniParser:

    __cfg__=None
    __file__="../../config/config.ini"

    def __init__(self):
        if os.path.exists(self.__file__) is True:
            self.__cfg__ = configparser.ConfigParser()
            self.__cfg__.read(self.__file__)
        else:
            raise Exception("%s file does not exist. \n" % self.__file__)

    def setFile(self, file):
        self.__file__=file

    def get(self, section, option):
        return self.__cfg__.get(section, option)

    def getBoolean(self,section, option):
        return self.__cfg__.getboolean(section, option)

    def getInt(self, section, option):
        return self.__cfg__.getint(section, option)

if __name__ == '__main__':
    cfg = iniParser()
    print(cfg.get("DB",'host'))
    print(cfg.getBoolean('DB','verbose'))
    print(cfg.getInt('DB', 'port'))
    #print(cfg.getInt('DB', 'name'))

    print(cfg.get("PATH",'home'))
