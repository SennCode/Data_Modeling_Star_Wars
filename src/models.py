import os
import sys
import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250),)
    password = Column(String(250), nullable=False)
    suscription = Column(DateTime, default=datetime.datetime.utcnow)
    

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    person = relationship(Person)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    person = relationship(Person)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    person = relationship(Person)

class FavAux(Base):
    __tablename__ = 'favaux'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    planetas = relationship(Planetas)
    personajes = relationship(Personajes)
    vehiculos = relationship(Vehiculos)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')