import reflex as rx
import WorkspaceWebPython.styles.styles as styles
from WorkspaceWebPython.styles.colors import TextColor as TextColor 
from WorkspaceWebPython.styles.colors import Color as Color

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        #rx.span(title, font_weight="bold", color="blue"),#there is a ishu here 
        rx.text(
            title, 
            font_weight="bold",
            color=Color.PRIMARY.value, 
            as_="span"
            ),
       f" {body}", 
       font_size=styles.Size.MEDIUM.value,
       
    )
