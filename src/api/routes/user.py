from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from uuid import UUID

from db.repo import Repo
from db.utils import get_session
from db.models.user import User
from schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])

user_repo = Repo(User)


@router.post("/", response_model=UserRead)
async def create_user(user_in: UserCreate):
    user = await user_repo.add(
        login=user_in.login,
    )
    return user


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: UUID):
    return user_repo.get_by_field("id", user_id)


@router.get("/", response_model=List[UserRead])
async def list_users():
    return await user_repo.get_all()


@router.patch("/{user_id}", response_model=UserRead)
async def update_user(user_id: UUID, user_in: UserUpdate):
    update_data = user_in.dict(exclude_unset=True)

    updated_rows = await user_repo.update_by_field("id", user_id, **update_data)

    if not updated_rows:
        raise HTTPException(status_code=404, detail="User not found")

    return await user_repo.get_by_field("id", user_id)


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: UUID):
    deleted_rows = await user_repo.delete_by_field("id", user_id)

    if not deleted_rows:
        raise HTTPException(status_code=404, detail="User not found")
