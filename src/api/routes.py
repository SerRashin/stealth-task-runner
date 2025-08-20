from fastapi import APIRouter, HTTPException
from src.models.job import Job
from src.services.runner import Runner

router = APIRouter()

@router.post("/run")
def run(job: Job):
    try:
        return Runner().run(job)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, detail=str(e))
