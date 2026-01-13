from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.base_repository import BaseRepository
from app.core.models import FieldDefinitions


class BaseFieldRepository(BaseRepository[FieldDefinitions]):
    def __init__(self, session: AsyncSession):
        super().__init__(FieldDefinitions, session)

    async def insert_field(self, new_field, user_group_id: int):
        data = new_field.model_dump(exclude_defaults=True)
        data['group_id'] = user_group_id
        result = await self.insert(data=data).returning(FieldDefinitions.id).execute()
        return result.scalar()

    async def update_field(self, new_field, user_group_id: int, field_id: int):
        await self.update(
            and_(
                FieldDefinitions.id == field_id,
                FieldDefinitions.group_id == user_group_id
            ),
            data={**new_field.model_dump(exclude_defaults=True)}
        ).execute()

    async def delete_field(self, field_id: int, user_group_id: int):
        await self.delete(
            and_(
                FieldDefinitions.id == field_id,
                FieldDefinitions.group_id == user_group_id
            )
        ).execute()
