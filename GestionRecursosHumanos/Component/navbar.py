import reflex as rx 
from ..styles.color import Color 
from .link_icon import link_icon

def render_navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="favicon.ico",
                alt="Logo del Sistema de Gestión de Citas Médicas",
                width=100,
                height=100,
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                "Sistema de Gestión de Citas Médicas",
                font_size="2em",
                padding_y="0.75em",
                padding_x="0.2em",
            ),
            rx.spacer(),
            link_icon(
                "instagram.png",
                "http://hospitalxyz.com"
            ),
            link_icon(
                "instagram.png",
                "http://hospitalxyz.com"
            ),
            link_icon(
                "instagram.png",
                "http://hospitalxyz.com"
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("Menu"),
                ),
                rx.menu.content(
                    rx.menu.item("Inicio"),
                    rx.menu.separator(),
                    rx.menu.item("Citas"),
                    rx.menu.item("Médicos"),
                    rx.menu.item("Pacientes"),
                    rx.menu.item("Especialidades"),
                    rx.menu.item("Contacto")
                ),
            ),

        ),
        background_color=Color.BACKGROUND.value,
        position="sticky",
        border_bottom=f"0.25 solid {Color.SECONDARY.value}",
        padding="10px",
        z_index="999",
        top="0",
        width="100%",
    )
