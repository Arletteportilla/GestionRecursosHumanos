import reflex as rx
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

class Usuario(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    email: str
    tipo: str  # 'administrador' o 'profesor'

class Administrador(Usuario):
    pass

class Profesor(Usuario):
    pass

class Contrato(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id")
    tipo: str  # 'temporal', 'permanente', etc.
    duracion: str  # '6 meses', '1 año', etc.
    fecha_inicio: str
    fecha_fin: str

class Asistencia(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id")
    fecha: str
    hora_entrada: str
    hora_salida: str
    aula: str
    validado: bool
    penalizacion: str  # 'ninguna', 'fuera de la universidad', etc.

# Relaciones
usuarios = Relationship(back_populates="usuario")
contratos = Relationship(back_populates="contrato")
asistencias = Relationship(back_populates="asistencia")