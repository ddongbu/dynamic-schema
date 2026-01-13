from typing import Dict, Any

from app.api.users.repository.base_users_repository import BaseUserRepository


class BaseUserService:
    def __init__(self, repository: BaseUserRepository):
        self.repository = repository

    async def create_user(self, new_user):
        result = await self.repository.insert_user(new_user)
        return result

    async def update_user(self, user_id: int, update_data: Dict[str, Any]):
        filtered_data = {k: v for k, v in update_data.items() if v is not None}
        await self.repository.update_user(user_id, filtered_data)

    async def delete_user(self, user_id: int):
        await self.repository.delete_user(user_id)
