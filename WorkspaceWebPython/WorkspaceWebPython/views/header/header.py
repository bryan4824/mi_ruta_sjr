import reflex as rx
from WorkspaceWebPython.components.link_icon import links_icon
from WorkspaceWebPython.components.info_text import info_text
import WorkspaceWebPython.styles.styles as styles 
from WorkspaceWebPython.styles.colors import Color as Color
from WorkspaceWebPython.styles.colors import TextColor as TextColor 
from WorkspaceWebPython.styles.fonts import Font

def header() -> rx.Component:
    return rx.vstack(

        rx.hstack(
            rx.avatar( 
                name="Mi ruta SJR.",
                padding="2px",
                src="/logo.png",
                border_color= styles.Color.CONTENT.value,
                size="5"),
            rx.vstack(
                rx.heading("Mi ruta SJR", 
                           size="5", 
                           weight="bold", 
                           color=TextColor.HEADER.value,
                           font_family=Font.TITULO.value
            ),
                            rx.hstack(
                                links_icon("https://google.com"),
                                links_icon("https://google.com"),
                                links_icon("https://google.com"),
                                links_icon("https://google.com"),
                                width="100%"
                            ),
                #rx.text("Hola bienvenido, me da gusto que estes aqui!!", size="4"),
                align_items="start"
            ),
        ),
        rx.text(
            "Explora San Juan del Río con facilidad. ",
            "Haz clic en cualquiera de las rutas disponibles para descubrir el recorrido del autobús, ",
            "las paradas principales y puntos de interés a lo largo del trayecto en San Juan del Río, Querétaro.", 
                size="3",
                color=TextColor.BODY.value,
                font_family=Font.TEXT_INSTRUCTIONS.value),
        spacing="5",
        align_items="start"
        
        #rx.flex(
            
         #       info_text("Hola bienvenido", ",me da gusto que estes aqui!!"),
          #      rx.spacer(),
           #     width="100%",
            #)"""
    )
       