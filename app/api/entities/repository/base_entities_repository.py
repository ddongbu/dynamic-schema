from sqlalchemy.ext.asyncio import AsyncSession

from app.core.base_repository import BaseRepository
from app.core.models import Entities


class BaseEntityRepository(BaseRepository[Entities]):
    def __init__(self, session: AsyncSession):
        super().__init__(Entities, session)

    async def insert_entity(self, new_entity, user_group_id):
        payload = new_entity.model_dump(exclude_defaults=True)
        payload['group_id'] = user_group_id
        result = await self.insert(data=payload).returning(
            Entities.id).execute()
        return result.scalar()

    async def update_entity(self, entity_id: int, group_id: int, update_data):
        await self.update(
            Entities.id == entity_id,
            Entities.group_id == group_id,
            data={**update_data}
        ).execute()

    async def delete_entity(self, entity_id: int, group_id: int):
        await self.delete(
            Entities.id == entity_id,
            Entities.group_id == group_id
        ).execute()

    async def get_entity_by_id(self, entity_id: int, group_id: int):
        result = await self.select(
            Entities.id == entity_id,
            Entities.group_id == group_id
        ).execute()
        return result.scalar()

    async def get_entities_by_group(self, group_id: int):
        result = await self.select(
            Entities.group_id == group_id
        ).orderby(Entities.create_date.desc()).execute()
        return result.scalars()
