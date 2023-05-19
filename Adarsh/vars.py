# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID','16536417'))
    API_HASH = str(getenv('API_HASH','f6e58a549da642d7b765744a2f82c6d9'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','5585418491:AAES4IWhJjqKzjHLfjTD0DiW03G5TpL3S6g'))
    name = str(getenv('SESSION_NAME', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1001611644647'))
    PORT = int(getenv('PORT', 80))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "921365334").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN','43.205.124.122')) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL','mongodb+srv://robo123:robo123@cluster0.g0w5r.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL','The_silent_teams'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
