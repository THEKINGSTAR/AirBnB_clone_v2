#!/usr/bin/python3
"""This module defines a class to manage DATABASE storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

class DBStorage:
  """This class manages storage of hbnb models in SQL format"""
  __engine = None
  __session = None

  def __init__(self):
      """
      create the engine (self.__engine)
      """
      user: os.getenv("HBNB_MYSQL_USER")
      password: os.getenv("HBNB_MYSQL_PWD")
      host: os.getenv("HBNB_MYSQL_HOST")
      database: os.getenv("HBNB_MYSQL_DB")
      env = os.getenv("HBNB_ENV")

      self.__engine = create_engine(
                      'mysql+mysqldb://{}:{}@{}/{}'
                      .format(user, password, host, database),
                      pool_pre_ping=True)
      if (env is 'test'):
          Base.metadata.drop_all(self.__engine)

      if (env is not 'test'):
          self.reload()

  def all(self, cls=None):
    """    
    query on the current database session (self.__session) all objects depending of the class name (argument cls)
    if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
    this method must return a dictionary: (like FileStorage)
    key = <class-name>.<object-id>
    value = object
    """
    clases = [User, State, City, Amenity, Place, Review]
    results = {}
    
    if (cls is not None):
      query = self.__session.query(cls)
    else:
      query = self.__session.query(*clases)
    for obj in query.all():
      key = "{}.{}".format(type(obj).__name, obj.id)
      results[key] = obj
    return (results)


  def new(self, obj):
    """ add the object to the current database session (self.__session)"""
    self.__session.add(obj)

  def save(self):
    """commit all changes of the current database session (self.__session)"""
    self.__session.commit()

  def delete(self, obj=None):
    """delete from the current database session obj if not None"""
    if (obj is not None):
      self.__session.delete(obj)
      self.save()

  def reload(self):
    """
    create all tables in the database (feature of SQLAlchemy) 
    (WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine))
    create the current database session (self.__session) from the engine (self.__engine)
    by using a sessionmaker - the option expire_on_commit must be set to False ;
    and scoped_session - to make sure your Session is thread-safe
    """
    Base.metadata.create_all(self.__engine)
    strg_session = sessionmaker(
      bind = self.__engine, expire_on_commit=False)
    DBStorage.__session = scoped_session(strg_session)

  def close(self):
    """
    Close the current session
    """
    DBStorage.__session.remove()