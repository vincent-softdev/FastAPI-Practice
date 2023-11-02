from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    # table name    
    __tablename__ = 'todos'

    # variables
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(String)
    complete = Column(Boolean, default=False)

