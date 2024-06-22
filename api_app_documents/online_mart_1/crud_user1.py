from sqlmodel import Session, select
from api_app_documents.online_mart import UserModel, User
##from app.db.db_connector import DB_SESSION
from fastapi import Depends
from typing import Annotated

get_session : str = print("db session")

DB_SESSION = Annotated[Session, Depends(get_session)]

## get the power of session (DB_SESSION)
## step 1:- authenticate user already exist (email must be unique)

def user_add(user_details: UserModel, session: DB_SESSION): 
    ## verify user email and password match user_details (get list of users)
    db_statement = select(User).where(User.user_email == user_details.user_email).where(User.user_password == user_details.user_password)
    
    db_user_info = session.exec(db_statement).one_or_none()
    
    # either user exist or not-exist
    if db_user_info:
        print("User already exist")  # user already in db
        # TODO: add exception here
    else:
        user = select(User)       # add user in db
        session.add(user)
        session.commit()
        session.refresh(user)
        return user_details  
    

## one_or_none() either use has password or none
## one():- if user don't has password it can't go further so use one_or_none()