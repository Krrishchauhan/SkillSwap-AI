from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    skills_required = Column(String)

    owner_id = Column(Integer)
   
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(Integer)
    user_id = Column(Integer)

    message = Column(String)