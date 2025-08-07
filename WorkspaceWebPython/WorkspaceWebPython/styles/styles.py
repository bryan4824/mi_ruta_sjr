import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor

MAX_WIDTH= "540px"

#Sizes 
class Size(Enum):
    ZERO = "0em"
    SMALL = ".5em"
    MEDIUM = ".9em"
    DEFAULT = "1em"
    MEDIUM_BIG_DEFAULT = "1.5em"
    BIG = "2em"
    SPACING_TEXT_BUTTON = "1"

#
BASE_STYLE = {
    #"background_color" : Color.BACKGROUND.value,
    "background" : Color.BACKGROUND.value,
    rx.button:{
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color" : Color.CONTENT.value,
        "_hover" : {
            "background_color" : Color.SECONDARY.value
        }
    },
    rx.link:{
        "text_decoration":"none",
        "_hover": {}
    }
}
title_style= dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)
button_title_style = dict(
    font_size=Size.MEDIUM_BIG_DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)




