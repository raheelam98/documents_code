# Commands : Poetry 

## Create Project with Poetry

create new project
```shell
poetry —-version
poetry new project_name 
cd project_name
```
**Poetry environmnet**

```bash
poetry add fastapi sqlmodel uvicorn\[standard\] psycopg
```

```bash
poetry add passlib bcrypt python-jose 
```

```bash
poetry add python-multipart
```

**Detail**

add drivers
```shell
poetry add fastapi uvicorn\[standard\] 
```

add drivers for db
```shell
poetry add sqlmodel psycopg psycopg2
```

add drivers for testing
```shell
poetry add pytest
poetry run pytest
```

add drivers (one line command)
```shell
poetry add fastapi sqlmodel uvicorn\[standard\] psycopg 
```

add aiokafka
> **Note**
> aiokafka is an asynchronous Kafka client for Python, which allows your application to interact with Apache Kafka message brokers in an asynchronous manner.

```shell
poetry add aiokafka
```

```shell
poetry add protobuf
```


**Current virtual environment for your Poetry project**

```bash
poetry env info --path
```

List all virtual environments associated with the current project

```bash
poetry env list
```

**run poetry app**

```shell
poetry run uvicorn folder_name.file_name:app --port 8000 --reload

poetry run uvicorn app.main:app --port 8000 --reload
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
poetry add pyjwt
```

**Generate a random string of bytes in hexadecimal format**
```bash
openssl rand -hex 32
``` 


Poetry 

FastAPI app
[fastapi-docs-url]: https://fastapi.tiangolo.com/advanced/dataclasses/

Test Applications with FastAPI and SQLModel
[SQLModel-docs-url]: https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/?h=test#__code_5_annotation_4
