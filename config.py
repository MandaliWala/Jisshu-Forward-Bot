import os

class Config:
    API_ID = os.environ.get("API_ID", "25163484")
    API_HASH = os.environ.get("API_HASH", "145bcbc424d1c1ffe04f3e607ea55c9a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7062533535:AAGwGXeYVJXvWuoTyAi6ZETTbL26NXjL9zQ") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://fowardbot:fowardbot@cluster0.qjwunlh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '6302921275').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
