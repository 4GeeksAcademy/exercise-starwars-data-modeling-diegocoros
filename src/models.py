import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    user_name = Column(String(80), nullable=False)
    favorites = relationship('Favorite', backref='user', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    climate = Column(String(80))
    terrain = Column(String(80))
    population = Column(String(80))
    favorites = relationship('Favorite', backref='planet', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    height = Column(String(80))
    mass = Column(String(80))
    hair_color = Column(String(80))
    skin_color = Column(String(80))
    eye_color = Column(String(80))
    birth_year = Column(String(80))
    gender = Column(String(80))
    favorites = relationship('Favorite', backref='character', lazy=True)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    model = Column(String(120))
    manufacturer = Column(String(120))
    cost_in_credits = Column(String(80))
    length = Column(String(80))
    crew = Column(String(80))
    passengers = Column(String(80))
    cargo_capacity = Column(String(80))
    favorites = relationship('Favorite', backref='starship', lazy=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=True)

render_er(Base, 'diagram.png')
