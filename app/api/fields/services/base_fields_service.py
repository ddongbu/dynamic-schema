from app.api.fields.repository.base_fields_repository import BaseFieldRepository


class BaseFieldsService:
    def __init__(self, repository: BaseFieldRepository):
        self.repository = repository

    async def create_field(self, new_field, user_group_id):
        result = await self.repository.insert_field(new_field, user_group_id)
        return result

    async def patch_field(self, new_field, user_group_id, field_id):
        await self.repository.update_field(new_field, user_group_id, field_id)

    async def delete_field(self, field_id: int, user_group_id: int):
        await self.repository.delete_field(field_id, user_group_id)
