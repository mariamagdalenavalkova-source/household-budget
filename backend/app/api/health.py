import logging
from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.db.session import get_db

logger = logging.getLogger(__name__)

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check(db: Annotated[Session, Depends(get_db)]) -> JSONResponse:
    """Report whether the API and the database are working."""
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        # Full details go to the developer log, never to the user
        logger.exception("Database health check failed")
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "error", "database": "unavailable"},
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "ok", "database": "ok"},
    )
