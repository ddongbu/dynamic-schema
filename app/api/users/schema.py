from datetime import datetime
from typing import Optional

from pydantic import Field

from app.core.schema import SchemaConfig


class BaseUser(SchemaConfig):
    username: str = Field(description="이름", alias="username")
    group_id: int = Field(description="그룹 KEY", alias="group_id")
    role: int = Field(description="권한", alias="role")


class UserRes(BaseUser):
    id: int = Field(description="KEY", alias="id")
    create_date: datetime = Field(description="생성 일시", alias="create_date")
    update_date: Optional[datetime] = Field(description="수정 일시", alias="update_date")


class UserReq(BaseUser):
    ...


class UserUpdateReq(SchemaConfig):
    username: Optional[str] = Field(default=None, description="이름", alias="username")
    group_id: Optional[int] = Field(default=None, description="그룹 KEY", alias="group_id")
    role: int = Field(description="권한", alias="role")
