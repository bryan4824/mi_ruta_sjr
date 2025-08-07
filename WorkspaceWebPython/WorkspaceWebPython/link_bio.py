import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.hstack(
        rx.text(
            "my ruta SJR", 
            height="40px"
        ),
        position="sticky", 
        bg="blue",
        padding_x="16px",
        padding_y="10px",
        z_index=999
    )

app = rx.App()
app.add_page(index)
app._compile()