from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from starlette.endpoints import HTTPEndpoint

from app.database.get_db import get_db
from app.utils.jwt import get_token

from app.exceptions.fast_api_custom import CustomException

from app.models.user.user import UserModel
from app.schemas import response, user, pagination

class UsersResource(HTTPEndpoint):
  @staticmethod
  async def get(params: pagination.paginationsValidate = Depends(), 
                db: Session = Depends(get_db), token = Depends(get_token) ):
    query = UserModel.read_paginate(params)
    return pagination.PaginationsBase(
      total=query.total, page=query.page, per_page=query.per_page, items=query.items
    )

  @staticmethod
  async def post( body: user.UserValidate, db: Session = Depends(get_db), token = Depends(get_token) ):
    query_user = UserModel.create(db, last_name=body.last_name, first_name= body.first_name, phone=body.phone, 
                                  description=body.description)
    db.commit()
    return query_user.id

class UsersSelectResource(HTTPEndpoint):
  @staticmethod
  async def get(db: Session = Depends(get_db), token = Depends(get_token)):
    query_users = UserModel.read_select()
    return query_users

class UserResource(HTTPEndpoint):
  @staticmethod
  async def get(user_id: str, db: Session = Depends(get_db), token = Depends(get_token)):
    query_user = UserModel.read(user_id)
    if not query_user:
      raise CustomException(status_code=404, type='NoData',  detail="No existe Usuario")
    return query_user
  
  @staticmethod
  async def put(user_id: str, body: user.UserValidate, db: Session = Depends(get_db), token = Depends(get_token)):
    query_user = UserModel.update(db, str(user_id), last_name=body.last_name, first_name= body.first_name, phone=body.phone,
                                    description=body.description)
    db.commit()
    return
  
  @staticmethod
  async def delete(user_id: str, db: Session = Depends(get_db), token = Depends(get_token)):
    query_user = UserModel.delete(db, user_id)
    db.commit()
    return 

class UserRestoreResource(HTTPEndpoint):
  @staticmethod
  async def put(user_id: str, db: Session = Depends(get_db), token = Depends(get_token)):
    query_user = UserModel.restore(db, user_id)
    db.commit()
    return 

  