import reflex as rx
import WorkspaceWebPython.styles.styles as styles     
from WorkspaceWebPython.styles.colors import Color as Color      
from WorkspaceWebPython.styles.colors import TextColor as TextColor                     
from WorkspaceWebPython.styles.colors import Sombra as Sombra 

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text.em("Rutas del  ", as_="span", color= TextColor.TEXT_NAVBAR_2.value),
            rx.text.strong("Transporte publico San Juan del Rio", as_="span", color= TextColor.TEXT_NAVBAR_1.value)

        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEFAULT.value,
        z_index=999,
        top="0", #mantiene el nabvar estatico 
        #me quede en el minuto 3:27:02 b
        style= Sombra.SOMBRA.value
        
    )
