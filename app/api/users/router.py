from typing import Dict, List

from fastapi import APIRouter, Depends

from app.api.users import service
from app.api.users.repository.base_users_repository import BaseUserRepository
from app.api.users.schema import UserRes, UserReq, UserUpdateReq
from app.api.users.services.base_users_service import BaseUserService
from app.core.schema import BaseResponse
from app.core.session_manager import SessionManager

router = APIRouter()


@router.get("", response_model=BaseResponse[Dict[str, List[UserRes]]])
async def get_users():
    data = await service.get_all_users()
    return BaseResponse(message="SUCCESS", data={"list": data})


@router.get("/{user_id}", response_model=BaseResponse[UserRes])
async def get_user(user_id: int):
    data = await service.get_user_info(user_id)
    return BaseResponse(message="SUCCESS", data=data)


@router.post("")
async def create_user(
    req: UserReq,
    session_manager: SessionManager = Depends()
):
    base_user_service = session_manager.inject(BaseUserService, BaseUserRepository)
    await base_user_service.create_user(req)
    return BaseResponse(message="SUCCESS")


@router.put("/{user_id}")
async def update_user(
    user_id: int,
    req: UserUpdateReq,
    session_manager: SessionManager = Depends()
):
    base_user_service = session_manager.inject(BaseUserService, BaseUserRepository)
    update_data = req.model_dump(exclude_unset=True)
    await base_user_service.update_user(user_id, update_data)
    return BaseResponse(message="SUCCESS")


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    session_manager: SessionManager = Depends()
):
    base_user_service = session_manager.inject(BaseUserService, BaseUserRepository)
    await base_user_service.delete_user(user_id)
    return BaseResponse(message="SUCCESS")
