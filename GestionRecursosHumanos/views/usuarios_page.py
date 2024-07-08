import reflex as rx
from GestionRecursosHumanos.models.models import Usuario
from GestionRecursosHumanos.servicios.usuarios_servcios import (
    servicio_usuario_all,
    servicio_consultar_usuario_por_id,
    servicio_crear_usuario,
    servicio_eliminar_usuario
)

class UsuarioState(rx.State):
    usuarios: list[Usuario] = []
    buscar_id: int = 0

    @rx.background
    async def get_todos_usuarios(self):
        async with self:
            self.usuarios = servicio_usuario_all()
            print("Usuarios page", self.usuarios)

    @rx.background
    async def get_usuario_por_id(self):
        async with self:
            self.usuarios = [servicio_consultar_usuario_por_id(self.buscar_id)]

    def buscar_onchange(self, value: str):
        self.buscar_id = int(value)

    @rx.background
    async def crear_usuario(self, data: dict):
        async with self:
            try:
                usuario_creado = servicio_crear_usuario(**data)
                if usuario_creado:
                    self.usuarios.append(usuario_creado)
            except Exception as e:
                print(e)

    @rx.background
    async def eliminar_usuario(self, id: int):
        async with self:
            try:
                if servicio_eliminar_usuario(id):
                    self.usuarios = [u for u in self.usuarios if u.id != id]
            except Exception as e:
                print(e)

@rx.page(route="/usuarios", title="Lista de Usuarios", on_load=UsuarioState.get_todos_usuarios)
def usuarios_page() -> rx.Component:
    return rx.flex(
        rx.heading("Usuarios", title="Usuarios", size="5", center=True),
        rx.vstack(
            buscar_usuario_id(),
            dialog_usuario_form(),
            justify="center",
            style={"margin": "20px", 'width': "100%"},
        ),
        tabla_usuarios(UsuarioState.usuarios),
        direction="column",
        justify="center",
        style={"margin": "auto", 'width': "100%"},
    )

def tabla_usuarios(lista_usuarios: list[Usuario]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID"),
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Tipo"),
                rx.table.column_header_cell("Acciones"),
            )
        ),
        rx.table.body(
            rx.foreach(lista_usuarios, row_table)
        ),
    )

def row_table(usuario: Usuario) -> rx.Component:
    return rx.table.row(
        rx.table.cell(usuario.id),
        rx.table.cell(usuario.nombre),
        rx.table.cell(usuario.email),
        rx.table.cell(usuario.tipo),
        rx.table.cell(
            rx.hstack(
                rx.button("Eliminar", on_click=lambda: UsuarioState.eliminar_usuario(usuario.id)),
            )
        ),
    )

def buscar_usuario_id() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="ID", on_change=UsuarioState.buscar_onchange),
        rx.button("Buscar Usuario", on_click=UsuarioState.get_usuario_por_id)
    )

def dialog_usuario_form() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Crear Usuario", variant="outline"),
        ),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title("Crear Usuario"),
                crear_usuario_form(),
                justify="center",
                align="center",
                direction="column",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", variant="soft", color_scheme="red"),
                ),
                spacing="2",
                justify="end",
                margin_top="10px",
            ),
            style={"width": "400px"},
        ),
    )

def crear_usuario_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(placeholder="Nombre", name="nombre"),
            rx.input(placeholder="Email", name="email"),
            rx.input(placeholder="Tipo", name="tipo"),
            rx.dialog.close(
                rx.button("Crear Usuario", type="submit"),
            ),
        ),
        on_submit=UsuarioState.crear_usuario,
    )
