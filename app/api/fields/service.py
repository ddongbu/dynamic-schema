from sqlalchemy import select

from app.core.db import db_manager
from app.core.models import FieldDefinitions


async def get_all_fields(user_group_id: int):

    # 필드명의 리스트는 display_order 정렬 순서로
    select_query = (
        select(FieldDefinitions)
        .where(FieldDefinitions.group_id == user_group_id)
        .order_by(FieldDefinitions.display_order, FieldDefinitions.id)
    )

    result = await db_manager.fetch_all(db="DB", query=select_query)
    return result
