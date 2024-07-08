# GestionRecursosHumanos/servicios/usuario_servicio.py
from GestionRecursosHumanos.models.models import Usuario
from GestionRecursosHumanos.conexion.usuarios_conexion import (
    select_all_usuarios,
    select_usuario_por_id,
    crear_usuario,
    eliminar_usuario
)

def servicio_usuario_all():
    usuarios = select_all_usuarios()
    print("Salida usuarios", usuarios)
    return usuarios

def servicio_consultar_usuario_por_id(usuario_id: int):
    if usuario_id > 0:
        usuario = select_usuario_por_id(usuario_id)
        print(usuario)
        return usuario
    else:
        return select_all_usuarios()

def servicio_crear_usuario(nombre: str, email: str, tipo: str):
    usuario_existente = servicio_consultar_usuario_por_id(nombre)
    if not usuario_existente:
        nuevo_usuario = Usuario(nombre=nombre, email=email, tipo=tipo)
        return crear_usuario(nuevo_usuario)
    else:
        return "El usuario ya existe"

def servicio_eliminar_usuario(id: int):
    return eliminar_usuario(id)
