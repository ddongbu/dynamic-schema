from sqlalchemy.ext.asyncio import AsyncSession

from app.core.base_repository import BaseRepository
from app.core.models import Users


class BaseUserRepository(BaseRepository[Users]):
    def __init__(self, session: AsyncSession):
        super().__init__(Users, session)

    async def insert_user(self, new_user):
        result = await self.insert(data={**new_user.model_dump(exclude_defaults=True)}).returning(
            Users.id).execute()
        return result.scalar()

    async def update_user(self, user_id: int, update_data):
        await self.update(
            Users.id == user_id,
            data={**update_data}
        ).execute()

    async def delete_user(self, user_id: int):
        await self.delete(
            Users.id == user_id
        ).execute()

    async def get_user_by_id(self, user_id: int):
        result = await self.select(
            Users.id == user_id
        ).execute()
        return result.scalar()
