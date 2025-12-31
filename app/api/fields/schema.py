from datetime import datetime
from typing import Optional, Dict, Any

from pydantic import Field

from app.core.schema import SchemaConfig


class BaseFields(SchemaConfig):
    name: str = Field(description="필드 명")
    group_id: int = Field(description="그룹 ID")
    field_type: str = Field(description="필드 타입")
    options: Optional[Dict[str, Any]] = Field(default=None, description="필드 옵션")
    is_required: bool = Field(description="필수 여부")
    display_order: int = Field(default=0, description="표시 순서")


class FieldsRes(BaseFields):
    id: int = Field(description="필드 ID")
    create_date: datetime = Field(description="생성 일시")
    update_date: Optional[datetime] = Field(default=None, description="생성 일시")


class FieldsReq(BaseFields):
    ...
