
#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1664850827
    OWNER = config("OWNER")
    ffmpegcode = ["-map 0 -c:v libx264 -pix_fmt yuv420p -crf 30 -preset veryfast -s 856x480 -c:a aac -b:a 50k -c:s copy"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/329c7304f471e7f5cd369.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
