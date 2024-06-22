import uuid
from sqlmodel import SQLModel, Field 
from pydantic import EmailStr
from typing import Optional

class UserBase(SQLModel):
    user_name: str
    phone_number: int = Field(max_digits=11)

class UserAuth(SQLModel):
    user_email: EmailStr
    user_password: str

class UserModel(UserAuth, UserBase):
    "place holder"
    pass

class User(UserModel, table=True):
    user_id: Optional[int] = Field(int, primary_key=True)
    kid: str = Field(default=lambda:uuid.uui4().hex)


#============================================================================================================================

### str = Field(default=lambda: uuid.uui4().hex) 
### uuid.uui4(): Generates a random UUID.   {note: import uuid}
### .hex: Converts the UUID to a hexadecimal string.
### note :- hex : Returns random id as 32 character hexadecimal string.
### 1-Sets the default value of the kid field to a new random UUID as a hexadecimal string,
### 2-  using a lambda function.
################
### UUID :- used *) generate unique random id. *) cryptography and hashing applications
### UUID :- useful, generating random documents, addresses   (keep information organized and secure.) 
### UUID (Universally Unique Identifier) data type stores a 128-bit value 
### UUID  is unique across both space and time
### uuid4() :- Generate a random UUID.
### generates a random UUID using the version 4 UUID algorithm.
### function, which returns a new UUID object. 
################

### Lambda :-  arguments  : expression
### Lambda :-  x,y  : x + y

### https://python.useinstructor.com/concepts/fields/#default-values

################    
## place holder :-  : a person or thing that occupies the position or place of another person or thing.  
    
## Definition and Usage. The placeholder attribute specifies a short hint that describes the expected value of an input field or a textarea.    
    
# class User(UserModel, table=True):
#     user_id: Optional[int] = Field(int, primary_key=True)

### pass is a placeholder statement that does nothing when executed.     

### Placeholder: The primary purpose of pass in this context is to act as a placeholder. 
### Since UserModel inherits from both UserBase and UserAuth, it already combines 
### all the necessary properties for a user. The pass statement indicates that 
### no additional implementation is needed within this class itself.        