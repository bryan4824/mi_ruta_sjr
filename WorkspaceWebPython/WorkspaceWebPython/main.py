import reflex as rx
from WorkspaceWebPython.WorkspaceWebPython import index

class State(rx.State):
    pass

def main():
    return index()


def index() -> rx.Component:

    return rx.container(     
        rx.vstack(
          
            rx.box(
                height="100px",
                width="100%",
                bg="white",
                position="absolute",
                top="0px",
                left="0px",
                z_index="-1",
                box_shadow="md"
            ),

            rx.link(
                rx.image(src="/logo.png", height="60px", alt="Logo Mi Ruta San Juan"),
                href="/",
                position="absolute",
                top="20px",
                left="40px"
            ),

            rx.desktop_only(
                rx.hstack(
                    rx.link("Inicio", href="/", font_size="1rem", color="black", font_weight="bold",_hover={"text_decoration": "underline" }),
                    rx.link("Rutas", href=main(), font_size="1rem", _hover={"color": "black"}),
                    rx.link("Acerca", href="/acerca", font_size="1rem", _hover={"color": "black"}),
                    spacing="6",
                    position="absolute",
                    top="35px",
                    right="60px"
                )
            ),

            rx.heading("Mi ruta San Juan", size="9",
                       position="absolute",
                       top="100px",
                       left="460px",
                       font_family="Times New Roman, sans-serif",
                       ),

            rx.text("Nuestro proposito es ayudar a la población de San Juan del Rio y turistas en la orientación del uso de transporte público, mediante una herramienta digital que facilite la visualización de las rutas disponibles y apoye al usuario en la toma de decisiones para elegir la ruta más cercana y adecuada para llegar a su destino.",
                    size="5", color="black",
                    position="absolute",
                    text_align="justify",
                    max_width="600px",
                    top="185px",
                    left="380px",
                    font_family="Arial, sans-serif",
                    ),

            rx.image(
                src="/camion1.JPG",    
                width="300px",
                height="175px",
                position="absolute",
                top="370px",
                left="525px",
                object_fit="cover",
                border_radius="12px",
                style={"boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)"},
                transition="transform 0.3s ease",
                _hover={
                    "transform": "scale(1.05)",
                    "boxShadow": "0 8px 16px rgba(0, 0, 0, 0.3)"
                }
            ),

            rx.heading("Lugares interesantes en San Juan del Rio", size="8",
                       position="absolute",
                       text_align="justify",
                       max_width="900px",
                       top="600px",
                       left="380px",
                       font_family="Times New Roman, sans-serif",
                       ),

            rx.image(
                src="/lugar1.jpg",
                width="300px",
                height="175px",
                position="absolute",
                top="670px",
                left="330px",
                object_fit="cover",
                border_radius="12px",
                style={"boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)"},
                transition="transform 0.3s ease",
                _hover={
                    "transform": "scale(1.05)",
                    "boxShadow": "0 8px 16px rgba(0, 0, 0, 0.3)"
                }
            ),

            rx.image(
                src="/lugar2.jpg",
                width="300px",
                height="175px",
                position="absolute",
                top="670px",
                left="730px",
                object_fit="cover",
                border_radius="12px",
                style={"boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)"},
                transition="transform 0.3s ease",
                _hover={
                    "transform": "scale(1.05)",
                    "boxShadow": "0 8px 16px rgba(0, 0, 0, 0.3)"
                }
            ),

            rx.heading("Jardín de Independencia", size="5", color="black",
                       position="absolute",
                       text_align="justify",
                       max_width="900px",
                       top="865px",
                       left="365px",
                       font_family="Arial, sans-serif",
                       ),

            rx.heading("Puente de la Historia", size="5", color="black",
                       position="absolute",
                       text_align="justify",
                       max_width="900px",
                       top="865px",
                       left="775px",
                       font_family="Arial, sans-serif",
                       ),

            rx.image(
                src="/lugar3.jpg",
                width="300px",
                height="175px",
                position="absolute",
                top="925px",
                left="520px",
                object_fit="cover",
                border_radius="12px",
                style={"boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)"},
                transition="transform 0.3s ease",
                _hover={
                    "transform": "scale(1.05)",
                    "boxShadow": "0 8px 16px rgba(0, 0, 0, 0.3)"
                }
            ),

            rx.heading("Parque de las Garzas", size="5", color="black",
                       position="absolute",
                       text_align="justify",
                       max_width="900px",
                       top="1120px",
                       left="565px",
                       font_family="Arial, sans-serif",
                       ),

            rx.heading("¿Qué ventajas tiene usar Mi Ruta San Juan del Rio?", size="7", color="black",
                       position="absolute",
                       max_width="900px",
                       top="1190px",
                       left="380px",
                       font_family="Times New Roman, sans-serif",
                       ),

            rx.text("1- Ahorrar tiempo al momento de buscar la ruta indicada.\n2- Evitar confusiones en base a las rutas\n3- Es una guía confiable para foráneos y turistas\n4- Mejor movilidad urbana\n5- Accesibilidad desde cualquier lugar\n6- Mayor seguridad al tomar el transporte",
                    size="5", color="black",
                    position="absolute",
                    white_space="pre-line",
                    line_height="2",
                    max_width="400px",
                    top="1265px",
                    left="660px",
                    font_family="Times New Roman, sans-serif",
                    ),

            rx.image(
                src="/camion2.JPG",
                width="310px",
                height="185px",
                position="absolute",
                top="1300px",
                left="300px",
                object_fit="cover",
                border_radius="12px",
                style={"boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)"},
                transition="transform 0.3s ease",
                _hover={
                    "transform": "scale(1.05)",
                    "boxShadow": "0 8px 16px rgba(0, 0, 0, 0.3)"
                }
            ),

            
            rx.image(
                src="/logo2.png",
                width="100px",
                height="100px",
                position="absolute",
                top="1600px",
                left="630px",
                object_fit="cover",
                border_radius="12px",
            ),

            rx.text("2024-2025 Mi Ruta San Juan Del Río.",
                size="4", color="blue",
                position="absolute",
                white_space="pre-line",
                line_height="2",
                max_width="400px",
                top="1720px",
                left="540px",
                font_family="Times New Roman, sans-serif",
            ),

            rx.text("Universidad Tecnológica de San Juan del Río.",
                size="3", color="black",
                position="absolute",
                white_space="pre-line",
                line_height="2",
                max_width="400px",
                top="1765px",
                left="510px",
                font_family="Arial, sans-serif",
            ),

        ),
        style={
            "backgroundImage": "linear-gradient(to right, #A3DC94, #4CCD99)",  
            "minHeight": "300vh",
            "position": "relative",
        }

    )

app = rx.App()
app.add_page(index)
