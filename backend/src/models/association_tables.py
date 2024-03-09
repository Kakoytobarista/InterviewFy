from sqlalchemy import Table, Column, Integer, ForeignKey

from src.models.base_model import Base

interview_task_association = Table(
    'interview_task_association',
    Base.metadata,
    Column('interview_id', Integer, ForeignKey('interview.id')),
    Column('task_id', Integer, ForeignKey('task.id'))
)
