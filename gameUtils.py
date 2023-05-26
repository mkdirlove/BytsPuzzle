import yaml
def readConfigFile():
    with open(r'config.yaml') as file:
        configFile = yaml.load(file, Loader=yaml.FullLoader)

    return configFile

def writeConfigFile(data):
    with open(r'config.yaml', 'w') as file:
        yaml.dump(data, file)

def gameLevel(level: str, name: str):
    level = level.lower()
    currLevel: int

    if level == 'easy':
        currLevel = 1
    elif level == 'normal':
        currLevel = 2
    elif level == 'hard':
        currLevel = 3
    elif level == 'expert':
        currLevel = 4

    configFile = readConfigFile()
    words_count = configFile['levels'][currLevel]['words']

    configFile['player']['level'] = currLevel
    configFile['player']['name'] = str(name)
    configFile['player']['score'] = 0
    configFile['words_count'] = int(words_count)

    writeConfigFile(configFile)

    return currLevel
