# Commands : Poetry 

## Create Project with Poetry

create new project
```shell
$ poetry —-version
$ poetry new project_name 
$ cd project_name
```

add drivers
```shell
$ poetry add fastapi uvicorn\[standard\] 
```

add drivers for db
```shell
$ poetry add sqlmodel psycopg psycopg2
```

add drivers for testing
```shell
$ poetry add pytest
$ poetry run pytest
```

add drivers (one line command)
```shell
$ poetry add fastapi sqlmodel uvicorn\[standard\] psycopg 
```

add aiokafka
> **Note**
> aiokafka is an asynchronous Kafka client for Python, which allows your application to interact with Apache Kafka message brokers in an asynchronous manner.

```shell
$ poetry add aiokafka
```

```shell
$ poetry add protobuf
```

```shell
$ poetry add passlib 
```

```shell
$ poetry add  
```

```shell
$ poetry add  
```

```shell
$ poetry add  
```

```shell
$ poetry add  
```

```shell
$ poetry add  
```

run poetry app

```shell
$ poetry run uvicorn folder_name.file_name:app --port 8000 --reload

$ poetry run uvicorn app.main:app --port 8000 --reload
```

**commands**

drivers
```shell
poetry add fastapi sqlmodel uvicorn\[standard\] psycopg 
```

drivers for testing
```shell
poetry add pytest
poetry run pytest
```

```shell
poetry add aiokafka
```

```shell
poetry add protobuf
```

```shell
poetry add pyjwt
```

```shell
pip install "passlib[bcrypt]"

poetry add "passlib[bcrypt]" 
```
**======================================**

```shell
poetry add types-python-jose
```

```shell
poetry add "python-jose[cryptography]"
```

```shell
poetry add types-passlib
```
generate a random string of bytes in hexadecimal format
```bash
openssl rand -hex 32
``` 



Poetry 

FastAPI app
[fastapi-docs-url]: https://fastapi.tiangolo.com/advanced/dataclasses/

Test Applications with FastAPI and SQLModel
[SQLModel-docs-url]: https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/?h=test#__code_5_annotation_4
