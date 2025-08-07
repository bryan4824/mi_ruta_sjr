import reflex as rx
import WorkspaceWebPython.styles.styles as styles
from WorkspaceWebPython.styles.styles import Size
from WorkspaceWebPython.styles.fonts import Font

def links_button(title: str, body : str, url:str) -> rx.Component:
    
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="bus",
                    width="2.5em",#styles.Size.BIG.value,
                    height="2.5em"#styles.Size.DEFAULT.value
                    #align_items="center",
                    #justify_content="center"
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing= Size.SPACING_TEXT_BUTTON.value,
                    align_items="start",
                    margin= styles.Size.ZERO.value
                    
                ),
                align_items="center" #mis modifi
            ),
            width="100%"#mis modifi
     ),
     href=url,
     is_external=True,
     width="100%"
        
    )
    