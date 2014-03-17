import ConfigParser

Config = ConfigParser.ConfigParser()

def initConfig(configFileName = "config.conf"):
    Config.read(configFileName)

initConfig()