from typing import Dict, List

from fastapi import APIRouter, Depends

from app.api.fields import service
from app.api.fields.repository.base_fields_repository import BaseFieldRepository
from app.api.fields.schema import FieldsRes, FieldsReq
from app.api.fields.services.base_fields_service import BaseFieldsService
from app.core.schema import BaseResponse
from app.core.session_manager import SessionManager

router = APIRouter()


@router.get("/{user_group_id}", response_model=BaseResponse[Dict[str, List[FieldsRes]]])
async def get_field_list(
    user_group_id: int,
):
    data = await service.get_all_fields(user_group_id)
    return BaseResponse(message="SUCCESS", data={"list": data})


@router.post("/{user_group_id}")
async def post_field(
    user_group_id: int,
    req: FieldsReq,
    session_manager: SessionManager = Depends()
):
    base_field_service = session_manager.inject(BaseFieldsService, BaseFieldRepository)
    await base_field_service.create_field(req, user_group_id)
    return BaseResponse(message="SUCCESS")


@router.patch("/{user_group_id}/{field_id}")
async def patch_field(
    user_group_id: int,
    field_id: int,
    req: FieldsReq,
    session_manager: SessionManager = Depends(),
):
    base_field_service = session_manager.inject(BaseFieldsService, BaseFieldRepository)
    await base_field_service.patch_field(req, user_group_id, field_id)
    return BaseResponse(message="SUCCESS")


@router.delete("/{user_group_id}/{field_id}")
async def delete_field(
    user_group_id: int,
    field_id: int,
    session_manager: SessionManager = Depends(),
):
    base_field_service = session_manager.inject(BaseFieldsService, BaseFieldRepository)
    await base_field_service.delete_field(field_id, user_group_id)
    return BaseResponse(message="SUCCESS")
