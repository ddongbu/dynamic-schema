from sqlalchemy.ext.asyncio import AsyncSession

from app.core.base_repository import BaseRepository
from app.core.models import FieldDefinitions


class BaseFieldRepository(BaseRepository[FieldDefinitions]):
    def __init__(self, session: AsyncSession):
        super().__init__(FieldDefinitions, session)

    async def insert_field(self, new_field):
        result = await self.insert(data={**new_field.model_dump(exclude_defaults=True)}).returning(
            FieldDefinitions.id).execute()
        return result.scalar()

    async def update_field(self, new_field):
        await self.update(data={**new_field.model_dump(exclude_defaults=True)})

    async def delete_field(self, user_group_id):
        await self.delete(
            FieldDefinitions.group_id == user_group_id,
        ).execute()
