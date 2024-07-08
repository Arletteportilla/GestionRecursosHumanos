import reflex as rx 

def header() -> rx.Component:
    return rx.grid(
        rx.center(
            rx.box(
                rx.heading("Sistema de Gestión de Citas Médicas", size="4"),
                rx.heading("Hospital XYZ", size="3"),
                rx.button("Ver Horarios", size="2", variant="outline", margin_top="3rem"),
            )
        ),
        rx.center(
            rx.image( 
                src="hospital.png",
                alt="Imagen del hospital",
                width="200px",
                height="auto",
                )
        ),
        columns="2",
        spacing="2",
        width="100%",
    )