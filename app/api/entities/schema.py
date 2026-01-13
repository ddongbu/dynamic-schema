from datetime import datetime
from typing import Optional, Dict, Any

from pydantic import Field

from app.core.schema import SchemaConfig


class BaseEntity(SchemaConfig):
    name: str = Field(description="엔티티명")
    custom_fields: Dict[str, Any] = Field(default_factory=dict, description="커스텀 필드 데이터")


class EntityRes(BaseEntity):
    id: int = Field(description="엔티티 ID")
    group_id: int = Field(description="그룹 ID")
    create_date: datetime = Field(description="생성 일시")
    update_date: Optional[datetime] = Field(default=None, description="수정 일시")


class EntityReq(BaseEntity):
    ...


class EntityUpdateReq(SchemaConfig):
    name: Optional[str] = Field(default=None, description="엔티티명")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="커스텀 필드 데이터")
