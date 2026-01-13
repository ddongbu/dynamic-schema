from typing import Dict, Any

from app.api.entities.repository.base_entities_repository import BaseEntityRepository


class BaseEntitiesService:
    def __init__(self, repository: BaseEntityRepository):
        self.repository = repository

    async def create_entity(self, new_entity, user_group_id):
        entity_id = await self.repository.insert_entity(new_entity, user_group_id)
        return entity_id

    async def update_entity(self, entity_id: int, group_id: int, update_data: Dict[str, Any]):
        filtered_data = {k: v for k, v in update_data.items() if v is not None}
        await self.repository.update_entity(entity_id, group_id, filtered_data)

    async def delete_entity(self, entity_id: int, group_id: int):
        await self.repository.delete_entity(entity_id, group_id)

    async def get_entity(self, entity_id: int, group_id: int):
        entity = await self.repository.get_entity_by_id(entity_id, group_id)
        return entity

    async def get_entities(self, group_id: int):
        entities = await self.repository.get_entities_by_group(group_id)
        return entities
