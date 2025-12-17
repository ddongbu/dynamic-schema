import datetime
from typing import Optional

from sqlalchemy import (ARRAY, Boolean, DateTime, Identity, Integer, PrimaryKeyConstraint,
                        String, UniqueConstraint, text)
from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column)


class Base(DeclarativeBase):
    pass

class UsersEx(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='vd_manager_pkey'),
        UniqueConstraint('email', name='vd_manager_pk_2'),
        {'comment': '내부담당자', 'schema': 'admin_system'}
    )

    id: Mapped[int] = mapped_column(Integer,
                                    Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647,
                                             cycle=False, cache=1), primary_key=True, comment='담당자 코드')
    email: Mapped[str] = mapped_column(String(100), comment='구글 이메일')
    auth_id: Mapped[int] = mapped_column(Integer, comment='권한 코드')
    name: Mapped[str] = mapped_column(String(30), comment='이름')
    is_active: Mapped[bool] = mapped_column(Boolean, server_default=text('true'), comment='활동 여부')
    create_date: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'),
                                                           comment='레코드 생성 일시')
    update_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='레코드 수정 일시')