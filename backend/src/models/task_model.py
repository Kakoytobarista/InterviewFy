# from sqlalchemy import String, Column
# from sqlalchemy.orm import relationship
#
# from .association_tables import interview_task_association
# from .base_model import Base
#
#
# class TaskModel(Base):
#     __tablename__ = 'task'
#
#     name = Column(String(100))
#     content = Column(String(1000))
#     interviews = relationship("InterviewModel", secondary=interview_task_association, back_populates="tasks")
