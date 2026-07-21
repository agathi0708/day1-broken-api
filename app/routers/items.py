from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app import models

router = APIRouter()


@router.get("/")
def list_items(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Returns every ticket along with its owning team's name."""

    results = (
        db.query(
            models.Item.id,
            models.Item.name,
            models.Owner.name.label("owner")
        )
        .join(models.Owner, models.Item.owner_id == models.Owner.id)
        .all()
    )

    return [
        {
            "id": row.id,
            "name": row.name,
            "owner": row.owner,
        }
        for row in results
    ]