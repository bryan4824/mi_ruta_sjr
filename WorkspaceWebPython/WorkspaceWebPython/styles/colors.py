import reflex as rx
from enum import Enum

class Color(Enum):
    PRIMARY = "#FFA673"
    SECONDARY = "#FFE3BB"
    BACKGROUND = "linear-gradient(to right, #A3DC9A, #4CCD99)"#"#03A6A1"#"#F8B259"
    CONTENT= "#FFF9BD"
    

class TextColor(Enum):
    HEADER ="#343842" 
    BODY = "#0E1A25"
    FOOTER = "#A3ABB2"
    TEXT_NAVBAR_1 = "#4CCD99"
    TEXT_NAVBAR_2 = "#007F73"

class Sombra(Enum):
    SOMBRA = style= {
            "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",  # Aquí la sombra
            "position": "sticky",
            "top": "0",
            "zIndex": "1000"
        }