# GestionRecursosHumanos/conexion/usuarios_conexion.py
from sqlmodel import Session, select
from sqlalchemy.exc import SQLAlchemyError
from GestionRecursosHumanos.models.models import Usuario, Administrador, Profesor
from GestionRecursosHumanos.conexion.conexion import connect

def select_all_usuarios():
    engine = connect()
    with Session(engine) as session:
        consulta = select(Usuario)
        usuarios = session.exec(consulta)
        return usuarios.all()

def select_usuario_por_id(usuario_id: int):
    engine = connect()
    with Session(engine) as session:
        consulta = select(Usuario).where(Usuario.id == usuario_id)
        resultado = session.exec(consulta)
        return resultado.one_or_none()

def crear_usuario(usuario: Usuario):
    engine = connect()
    try:
        with Session(engine) as session:
            session.add(usuario)
            session.commit()
            session.refresh(usuario)
            return usuario
    except SQLAlchemyError as e:
        print(e)
        return None

def eliminar_usuario(id: int):
    engine = connect()
    try:
        with Session(engine) as session:
            consulta = select(Usuario).where(Usuario.id == id)
            usuario = session.exec(consulta).one_or_none()
            if usuario:
                session.delete(usuario)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        print(e)
        return False
