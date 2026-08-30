import psycopg
from database import connect
from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/live")
def liveness_check():
    return {"status": "alive"}


@router.get("/ready")
def readiness_check():
    try:
        connection = connect()

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        connection.close()

        return {
            "status": "ready",
            "database": "connected",
        }

    except psycopg.Error as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "status": "not ready",
                "database": "unavailable",
            },
        ) from error
