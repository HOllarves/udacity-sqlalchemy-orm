import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):

    '''
    Table class used to reference data as an object in our python environment
    '''

    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):

    '''
    Table class used to reference data as an object in our python environment
    '''

    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

# Using SQLite for this scenario, but Postgres or any other SQL software is also possible
engine = create_engine('sqlite:///restaurantmenu.db')


Base.metadata.create_all(engine)