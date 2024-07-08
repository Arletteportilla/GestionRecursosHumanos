import reflex as rx
from GestionRecursosHumanos.Component.navbar import render_navbar
from GestionRecursosHumanos.Component.header import header
from GestionRecursosHumanos.Component.footer import pie_de_pagina
from GestionRecursosHumanos.views.usuarios_page import usuarios_page
from GestionRecursosHumanos.servicios.usuarios_servcios import servicio_usuario_all
from rxconfig import config

class State(rx.State):
    """The app state."""
    pass

def index() -> rx.Component:
    
    usuarios = servicio_usuario_all()

    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            render_navbar(),
            header(),
            lista_usuarios(usuarios),
            pie_de_pagina(),
        ),
        rx.logo(),
    )

def lista_proyecto(trabajos):
    return rx.hstack(*[
        rx.box(
            rx.image(src=trabajo['image_url']),
            rx.text(trabajo['titulo']),
            rx.text(trabajo['descripcion']),
            key=trabajo['titulo']
        ) for trabajo in trabajos
    ])

def lista_usuarios(usuarios):
    return rx.hstack(*[
        rx.box(
            rx.text(f"Usuario: {usuario.nombre}, Email: {usuario.email}, Tipo: {usuario.tipo}"),
            key=usuario.id
        ) for usuario in usuarios
    ])

app = rx.App()
app.add_page(index)
app.add_page(usuarios_page, route="/usuarios")
