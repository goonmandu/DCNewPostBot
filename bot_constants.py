from enum import Enum


class GalleryType(Enum):
    MINI = 1
    MINOR = 2
    MAIN = 3


class UnknownGalleryTypeException(Exception):
    def __init__(self, attempted_enum: GalleryType, message: str = "Unrecognized GalleryEnum"):
        self.attempted_enum = attempted_enum
        self.message = message
        super().__init__(self, attempted_enum)


""" --- SUPER IMPORTANT BOT STUFF HERE! --- """
# The ID of the channel you want the bot to link new posts in
TARGET_CHANNEL_ID = 1081673033376350260

# The name of the gallery as shown in the URL
GALLERY_NAME = "new_world"

# The type of the gallery
GALLERY_TYPE = GalleryType.MINOR

# Seconds between new post checks
REFRESH_TIME = 60

# Seconds between new post links within ONE check cycle
NEW_LINK_DELAY = 0.4
""" ---  END SUPER IMPORTANT BOT STUFF  --- """
