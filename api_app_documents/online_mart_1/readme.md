# online mart

```python  
    db_user_info = session.exec(db_statement).one_or_none()
```

**one_or_none() either use has data or none**
**one():- if user don't has password it can't go further so use one_or_none()**

```python 
class User(UserModel, table=True):
    user_id: Optional[int] = Field(int, primary_key=True)
    kid: str = Field(default=lambda:uuid.uui4().hex)
```


Default values
https://python.useinstructor.com/concepts/fields/ 

Fastapi-mail
https://sabuhish.github.io/fastapi-mail/ 

**=====================================================================================**

```python
## get the power of session (DB_SESSION)
## step 1:- authenticate user already exist (email must be unique)
    
    db_user_info = session.exec(db_statement).one_or_none()

## one_or_none() either use has data or none
## one():- if user don't has password it can't go further so use one_or_none()
```

user_models.py (set a newly generated UUID's hexadecimal representation)
```bash
import uuid
    kid: str = Field(default=lambda:uuid.uui4().hex)
```

***Field(...):*** Field is a class from Pydantic used to define metadata for fields in a Pydantic model.

**default=lambda: uuid.uuid4().hex**

***default=*** specifies the default value for the kid field.
***lambda:*** introduces an anonymous function that generates a default value.
***uuid.uuid4()*** generates a random UUID (Universally Unique Identifier) version 4.
***.hex*** converts the UUID object to its hexadecimal string representation.

https://python.useinstructor.com/concepts/fields/#default-values

crud_user.py (creates a User object using attributes from user_form and sets user_password to hashed_password.)

```bash
user = User(**user_form.model_dump(), user_password=hashed_password)
# example
user = UserCreate(name="John")
User(**user.model_dump())
```
#### Full Flow :- User(**user_form.model_dump(), user_password=hashed_password)
***1- Pydantic Model:*** UserModel instance (user_form) holds user details.

***2- Convert to Dictionary:*** user_form.model_dump() converts the instance to a 3 dictionary.

***3- Dictionary Unpacking:*** **user_form.model_dump() unpacks the dictionary into keyword arguments.

***4- Create User Object:*** User(**user_form.model_dump(), user_password=hashed_password) creates a new User object with the provided details and the hashed password.

**model_dump()** method in Pydantic :- converts a model instance into a dictionary with the model's attribute names as keys and their corresponding values.

returns a standard Python dictionary (dict) containing the attributes and values of the model instance.
https://stackoverflow.com/questions/77476105/can-pydantic-model-dump-return-exact-type


**links**

OAuth2 with Password (and hashing), Bearer with JWT tokens¶
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=jwt#hash-and-verify-the-passwords

Default values
https://python.useinstructor.com/concepts/fields/ 

Fastapi-mail
https://sabuhish.github.io/fastapi-mail/ 

Profiles
https://docs.docker.com/compose/compose-file/15-profiles/

Using profiles with Compose
https://docs.docker.com/compose/profiles/


**generate a random string of bytes in hexadecimal format**
```bash
openssl rand -hex 32
``` 


