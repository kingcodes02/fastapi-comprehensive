from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, models, utils, oauth2
from ..database import get_db


router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login", response_model=schemas.Token)
def login(payLoad: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.email == payLoad.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Invalid Credentials. Either email or password is/are wrong.")

    if not utils.verify(payLoad.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Invalid Credentials. Either email or password is/are wrong.")

    # create token
    # return token

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
