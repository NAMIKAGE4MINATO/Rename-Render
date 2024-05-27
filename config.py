# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24071070")

API_HASH = os.environ.get("API_HASH", "44a7e62442af188acde8d759f9b9df8d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7090705063:AAHT9QTYMO4mMRWa2YbVF6qfmJlziFBpxQg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Botz) 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "ms844237")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://ms844237:VJCjWOMAcA1a23pF@cluster0.h3srjth.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5693811797').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
