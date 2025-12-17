from typing import Any, Optional, Type, TypeVar

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_database_session

T = TypeVar("T")


class SessionManager:
    def __init__(
        self,
        request: Request,
        session: AsyncSession = Depends(get_database_session),
    ):
        self.request = request
        self.session = session
        self.pagination: Optional[dict] = {"limit": 100_000_000, "page": 1}

    def inject(self, service_cls: Type[T], repository_cls: Type[Any]) -> T:
        """
        repository_cls를 사용해 repository를 생성한 후,
        request & session을 주입한 service_cls를 반환
        """
        repository = repository_cls(self.session, self.pagination)
        service = service_cls(self.request, repository)  # type: ignore
        return service
