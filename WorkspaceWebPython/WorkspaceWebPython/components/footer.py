import reflex as rx
import datetime 
import WorkspaceWebPython.styles.styles as styles
from WorkspaceWebPython.styles.colors import Color as Color
from WorkspaceWebPython.styles.colors import TextColor as TextColor 

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo_2.png",
            width="120px",
            height="auto" ),
        rx.text(
            f"2024-{datetime.date.today().year} Mi Ruta San Juan Del Rio.", 
            font_size=styles.Size.MEDIUM.value,
            color=TextColor.TEXT_NAVBAR_2.value
        ),
        rx.link(
                "Universidad Tecnologica de San Juan del Rio.",
                href="https://www.utsjr.edu.mx/index.php", 
                font_size=styles.Size.MEDIUM.value,
                margin_bottom=styles.Size.BIG.value,
                margin_top="0px !important",
                is_external=True,
                color=TextColor.HEADER.value
                
        ),
        align_items="center",
        justify_content="center",
        margin_bottom = styles.Size.BIG.value,
        padding_bottom = styles.Size.BIG.value,
        color=TextColor.FOOTER.value
    )