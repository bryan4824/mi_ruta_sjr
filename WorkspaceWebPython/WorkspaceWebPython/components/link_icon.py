import reflex as rx
import WorkspaceWebPython.styles.styles as styles
from WorkspaceWebPython.styles.colors import TextColor as TextColor 

def links_icon(url:str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="hospital"
        ),
        href=url,
        is_external=True,
        color=TextColor.BODY.value
    )
