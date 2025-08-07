import reflex as rx
from rxconfig import config

from WorkspaceWebPython.components.navbar import navbar
from WorkspaceWebPython.components.footer import footer
from WorkspaceWebPython.views.header.header import header
from WorkspaceWebPython.views.links.links import links

import WorkspaceWebPython.styles.styles as styles

class State(rx.State):
    def handle_submit(self, form_data: dict):
        """Handle the form submission."""
        print(f"Form submitted with data: {form_data}")

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
            rx.desktop_only(
                rx.hstack(
                    rx.link("Inicio", href="/", font_size="1rem", color="black", font_weight="bold", 
                            _hover={"color": "#000000", "font_weight": "bold", "text_decoration": "none"}),
                    rx.link("Rutas", href="/rutas", target="_blank", font_size="1rem", color="black", 
                            _hover={"color": "#070808", "font_weight": "bold", "text_decoration": "none"}),
                    #rx.link("Acerca", href="/acerca", font_size="1rem", color="black", 
                     #   _hover={"color": "#000000", "font_weight": "bold", "text_decoration": "none"}),
                    spacing="6",
                    position="fixed",
                    top="35px",
                    right="60px",
                    color="black"
                ),rx.link(
                    rx.image(src="/logo_2.png", height="60px", alt="Logo Mi Ruta San Juan"),
                    href="/",
                    position="absolute",
                    top="20px",
                    left="40px"
            )),
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
                src="/logo.png",
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

def rutas() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                align_items="center",
                justify_content="center"
            )
        ),
        footer(),
    )


app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
        "https://fonts.googleapis.com/css2?family=Changa+One:ital@0;1&family=Playwrite+AU+QLD:wght@100..400&family=Rubik+Mono+One&family=Varela+Round&display=swap",
        "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap",
        "https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap"
    ],
)

app.add_page(index)
# Aquí la corrección: Tienes que añadir la página 'rutas' a la aplicación.
app.add_page(rutas, route="/rutas", title="Rutas")
app._compile()