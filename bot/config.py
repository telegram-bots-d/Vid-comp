
#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("27981265", cast=int)
    API_HASH = config("e2e52a1550b8dea246b64617a768eee2")
    BOT_TOKEN = config("6835393349:AAFMfsfQ9ctPb4Cml1HIDMbAj73pEJfOxX4")
    DEV = 1664850827
    OWNER = config("OWNER")
    ffmpegcode = ["-map 0 -c:v libx264 -pix_fmt yuv420p -crf 30 -preset veryfast -s 856x480 -c:a aac -b:a 50k -c:s copy"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
