from fastapi import APIRouter
from typing import List, Optional, Union

from app.database.get_db import get_db

from app.middlewares.auth_db import AuthDbMiddleware

from app.schemas import user, pagination

from app.resources.user import UsersResource, UsersSelectResource, UserResource, UserRestoreResource


router = APIRouter(
  prefix='/users',
  tags=["users"],
  route_class=AuthDbMiddleware
)

# User Pagination and Save
router.add_api_route("", 
  UsersResource.get, 
  methods=['GET'], 
  name="Mostrar usuarios con paginación",
  response_model=pagination.PaginationsBase[List[user.UserSchema]]
)

router.add_api_route("", 
  UsersResource.post, 
  methods=['POST'],
  name="Registrar usuarios",
)

# User Select
router.add_api_route("/select", 
  UsersSelectResource.get, 
  methods=['GET'],
  name="Mostrar usuarios totales sin paginación",
  response_model=List[user.UserSchema]
)

# User Id
router.add_api_route("/{user_id}", 
  UserResource.get, 
  methods=['GET'], 
  name="Mostrar un usuario",
  response_model=user.UserSchema
)

router.add_api_route("/{user_id}", 
  UserResource.put, 
  methods=['PUT'],
  name="Modificar un usuario",
)

router.add_api_route("/{user_id}", 
  UserResource.delete, 
  methods=['DELETE'],
  name="Desactivar un usuario",
)

# User Restore
router.add_api_route("/{user_id}/restore", 
  UserRestoreResource.put, 
  methods=['PUT'],
  name="Restaurar un usuario",
)
