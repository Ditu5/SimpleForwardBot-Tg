import os, re, time

id_pattern = re.compile(r'^.\d+$')


class Config:
    # Client Config              
    API_ID = int(os.environ.get("API_ID", "21288218")) # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd") # ⚠️ Required       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6021415198:AAGJ5z8r-bBK9iXzvymHHoKywAW-TDEPzCY") # ⚠️ Required
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")

    # Database Config 
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://FORWARD:FORWARD@cluster0.k1omlka.mongodb.net/?retryWrites=true&w=majority") # ⚠️ Required
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")

    # other configs 
    OWNER_ID = int(os.environ.get("OWNER_ID", "6065594762")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001971176803")) # ⚠️ Required
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001946118544")) # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002133789998') # ⚠️ Required
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    USERDATA = os.environ.get('USERDATA', 'USER_DATA')
    BOT_UPTIME  = time.time()
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None 
    BOT_USERNAME = os.environ.get('BOT_USERNAME', "") # No need if you don't want to auto forward when bot restarted
    SESSION = os.environ.get('SESSION', 'BQCzZBLHpkhk6r1S4VxPhZJPJyi9HtV75PSBe3ihxkul_a0r9FQITX3pS8Rh1K-raXtTR6FUciqeR0YS-rlN6n_E0LrdUIpdr06QdMzACPc39kaZBYd_S3savQauBl7lxoqheKvmtID7dDtS-1b7lMd9LJqK56jYxtYZuP6e8sebRwGL3pa8rklqK_2-eVif6Da6A6LTQ-fqCpZlnFSBze9GCBNvyuGiNHx_ou9yBFMC8Lp7BGmF1H25FuC_B5RQxItjmmbRHjee050msNVNz0axVBZUloG0TcZT_t7C79ElemfRLxxwZYOouHiFKNWt_Dte51B-U3QdswJCxagf9aaeAAAAAWmJoYoA')

    # Web Support 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True)) # for web support on/off
    PORT = os.environ.get("PORT","8080")


