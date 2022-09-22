from configparser import ConfigParser

config = ConfigParser()
config.read("../ConfigurationData/conf.ini")


def readConfig(section, key):
    return config.get(section, key)


def writeConfig(sesction,key,newvalue):
    config.set(sesction, key, newvalue)
    with open('../ConfigurationData/conf.ini', 'w') as configfile:
        config.write(configfile)


if readConfig("config","is_create_test_run") == "1":
    print("dada")