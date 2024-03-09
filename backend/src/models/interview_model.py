from sqlalchemy import String, Column, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_model import Base


interview_task_association = Table(
    'interview_task_association',
    Base.metadata,
    Column('interview_id', Integer, ForeignKey('interview.id')),
    Column('task_id', Integer, ForeignKey('task.id'))
)


class InterviewModel(Base):
    __tablename__ = 'interview'

    name = Column(String(100), unique=False)
    tasks = relationship(
        "TaskModel", secondary=interview_task_association, back_populates="interviews", lazy="selectin")


class TaskModel(Base):
    __tablename__ = 'task'

    name = Column(String(100))
    content = Column(String(1000))
    interviews = relationship(
        "InterviewModel", secondary=interview_task_association, back_populates="tasks", lazy="selectin")
