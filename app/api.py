from mangum import Mangum
from fastapi import (Depends, FastAPI, File, Form, Header, HTTPException, Path,
                     Query, UploadFile, status)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.configs.environment import Config

from app.exceptions.fast_api_validation import ValidationException
from app.exceptions.fast_api_custom import CustomException

# Import Exceptions
from app.exceptions.fast_api import http_exception_handler_custom, http_exception_handler,\
                                validation_exception_handler

from app.utils.responses import ResponseJson 

app = FastAPI(
  title=Config.PROJECT_NAME,
  version=Config.PROJECT_API_V1,
  debug=Config.DEBUG,
  default_response_class=ResponseJson
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exceptiones Handler
app.add_exception_handler(CustomException, http_exception_handler_custom)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ValidationException, validation_exception_handler)

# Routers
#pylint: disable=wrong-import-position
from app.routers.user import router as user_routers

# # Add routers
app.include_router(user_routers)
handler = Mangum(app)