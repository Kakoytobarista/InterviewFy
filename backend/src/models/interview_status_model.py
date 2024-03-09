from sqlalchemy import Column, ForeignKey, Boolean, Float, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class InterviewStatusModel(Base):
    __tablename__ = 'interview_status'

    interview_id: Mapped[int] = mapped_column(ForeignKey("interview.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    is_passed: Mapped[bool] = mapped_column(Boolean(), default=False)
    score: Mapped[float] = mapped_column(Float(), default=0)

    __table_args__ = (
        UniqueConstraint('interview_id', 'user_id'),
    )
