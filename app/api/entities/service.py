from sqlalchemy import select

from app.core.db import db_manager
from app.core.models import Entities


async def get_all_entities(user_group_id: int):
    select_query = (
        select(Entities)
        .where(Entities.group_id == user_group_id)
        .order_by(Entities.create_date.desc())
    )

    result = await db_manager.fetch_all(db="DB", query=select_query)
    return result


async def get_entity_info(entity_id: int, user_group_id: int):
    select_query = (
        select(Entities)
        .where(
            Entities.id == entity_id,
            Entities.group_id == user_group_id
        )
    )

    result = await db_manager.fetch_one(db="DB", query=select_query)
    return result
