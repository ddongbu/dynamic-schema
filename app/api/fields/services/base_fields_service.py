from app.api.fields.repository.base_fields_repository import BaseFieldRepository


class BaseFieldsService:
    def __init__(self, repository: BaseFieldRepository):
        self.repository = repository

    async def create_field(self, new_field):
        await self.repository.insert_field(new_field)

    async def patch_field(self, new_field):
        await self.repository.update_field(new_field)

    async def delete_field(self, user_group_id):
        await self.repository.delete_field(user_group_id)
