# Main configuration file

# Mandatory Variables
API_ID = 25492855 # Replace with your actual Telegram API ID
API_HASH = "61876db014de51a4ace6b169608be4f1"  # Replace with your actual Telegram API Hash
BOT_TOKEN = "7421749280:AAHWxAJHsJ02tt-jul0HijBqHA0QKCqSprc"  # Replace with your actual Bot Token
OWNER_ID = "6359874284"  # Replace with your actual Owner ID
# Database
DATABASE_URL = "mongodb+srv://Yash_607:Yash_607@cluster0.r3s9sbo.mongodb.net/?retryWrites=true&w=majority"  # Replace with your actual database URL

AUTH_CHAT = "-1002262464799" # Replace with your actual auth chat ID. You can use multiple IDs separated by ( space ).
LOGS_CHAT = -1002241609467 # Replace with your actual logs chat ID
POST_CHAT = -1002241609467 # Replace with your actual post chat ID

ADMIN_USERNAME = "hgbotz" # Replace with your admin username
ADMIN_PASSWORD = "hgbotzz" # Replace with your admin password


SITE_SECRET = "abcdefghijk" # Replace with your site secret key
TMDB_API_KEY = "ec8c79cb7ce985249d2c690a90752c94" # Replace with your TMDB API key

# Optional Variables

# If you want to use multiple bot tokens, uncomment the MULTI_TOKENS dictionary and add your tokens. this aditional bots will speed up the process of downloading and streaming files.
MULTI_TOKENS = {
    # 1: "BOT_TOKEN_1_HERE",
    # 2: "BOT_TOKEN_2_HERE",
    # Add more tokens as needed
}
DELETE_AFTER_MINUTES = 10 # Set the number of minutes after which files will be deleted from user message
POST_UPDATES = True # Set to True if you want to post updates in the post chat
USE_CAPTION = False # Set to True if you want to use captions for posts instead of file names.

# Port configuration
import os
PORT = int(os.environ.get("PORT", 6519))
















# (Don't touch this unless you know what you're doing)
SUDO_USERS = [int(x) for x in (OWNER_ID).split()]
AUTH_CHATS = [int(x) for x in (AUTH_CHAT).split()]
