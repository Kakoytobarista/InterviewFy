from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column
import enum

from .base_model import Base


class UserRole(enum.Enum):
    teacher = "teacher"
    candidate = "candidate"


class UserModel(Base):
    __tablename__ = "user"

    full_name: Mapped[str] = mapped_column(String(50), unique=True)
    role: Mapped[Enum] = mapped_column(Enum(UserRole), nullable=False, default=UserRole.candidate.value)
