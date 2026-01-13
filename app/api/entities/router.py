from typing import Dict, List

from fastapi import APIRouter, Depends

from app.api.entities import service
from app.api.entities.repository.base_entities_repository import BaseEntityRepository
from app.api.entities.schema import EntityRes, EntityReq, EntityUpdateReq
from app.api.entities.services.base_entities_service import BaseEntitiesService
from app.core.schema import BaseResponse
from app.core.session_manager import SessionManager

router = APIRouter()


@router.get("/{user_group_id}", response_model=BaseResponse[Dict[str, List[EntityRes]]])
async def get_entity_list(
    user_group_id: int,
):
    data = await service.get_all_entities(user_group_id)
    return BaseResponse(message="SUCCESS", data={"list": data})


@router.get("/{user_group_id}/{entity_id}", response_model=BaseResponse[EntityRes])
async def get_entity(
    user_group_id: int,
    entity_id: int,
):
    data = await service.get_entity_info(entity_id, user_group_id)
    return BaseResponse(message="SUCCESS", data=data)


@router.post("/{user_group_id}")
async def create_entity(
    user_group_id: int,
    req: EntityReq,
    session_manager: SessionManager = Depends(),
):
    base_entity_service = session_manager.inject(BaseEntitiesService, BaseEntityRepository)
    await base_entity_service.create_entity(req, user_group_id)
    return BaseResponse(message="SUCCESS")


@router.put("/{user_group_id}/{entity_id}")
async def update_entity(
    user_group_id: int,
    entity_id: int,
    req: EntityUpdateReq,
    session_manager: SessionManager = Depends(),
):
    base_entity_service = session_manager.inject(BaseEntitiesService, BaseEntityRepository)
    update_data = req.model_dump(exclude_unset=True)
    await base_entity_service.update_entity(entity_id, user_group_id, update_data)
    return BaseResponse(message="SUCCESS")


@router.delete("/{user_group_id}/{entity_id}")
async def delete_entity(
    user_group_id: int,
    entity_id: int,
    session_manager: SessionManager = Depends(),
):
    base_entity_service = session_manager.inject(BaseEntitiesService, BaseEntityRepository)
    await base_entity_service.delete_entity(entity_id, user_group_id)
    return BaseResponse(message="SUCCESS")
