from fastapi import APIRouter, HTTPException

from src.models.request_models import (
    PreprocessRequest,
    PreprocessResponse
)
from src.services.preprocessing_engine import preprocess_text


router = APIRouter()


@router.post(
    "/preprocess",
    response_model=PreprocessResponse
)
def preprocess_endpoint(request: PreprocessRequest):

    try:
        result = preprocess_text(request)

        return PreprocessResponse(
            original_text=result["original_text"],
            processed_text=result["processed_text"],
            language=result["language"],
            applied_steps=result["applied_steps"],
            success=True,
            message="Text preprocessing completed successfully."
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )