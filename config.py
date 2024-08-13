# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "25163484")
    API_HASH = environ.get("API_HASH", "145bcbc424d1c1ffe04f3e607ea55c9a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7062533535:AAGwGXeYVJXvWuoTyAi6ZETTbL26NXjL9zQ") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6302921275').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://fowardbot:fowardbot@cluster0.qjwunlh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL',"-1002137528664")
# FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
