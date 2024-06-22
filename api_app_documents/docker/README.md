# compose file  

Multi Layers :-  requires 
Fast-api Service
Database  Service  

```yml
version: "3.9"

name: docker_compose_db

services:
  api_compose_db:
    build:
      context: ./todo
      dockerfile: Dockerfile.dev
    container_name: api_compose_con
    depends_on:
        - postgres_db
    ports:
      - "8000:8000"  # Expose hot port 8000 to container port 8000  
    networks:
      - my-api-net
  postgres_db:
    image: postgres:latest  # Use the official PostgreSQL image
    restart: always
    container_name: PostgresCont
    environment:
        - POSTGRES_USER=ziakhan
        - POSTGRES_PASSWORD=my_password
        - POSTGRES_DB=mydatabase
    ports:
        - '5433:5432'
    volumes:
        - postgres_db:/var/lib/postgresql/data
    networks:
      - my-api-net

volumes:
  postgres_db:
    driver: local

networks:
  my-api-net:  # Define the custom network
```

**(STEP : I )**
```yaml 
Services:
  api:
    build:
 ``` 
**(Step 1)**
```yaml
 postgres_db:
    image: postgres:latest  # Use the official PostgreSQL image
    restart: always         # always run. (Run always —> restart : always)
```   
   
https://hub.docker.com/_/postgres
  
**(Step 2)**
```yaml 
    container_name: PostgresCont
```    
	
# optional (better to give name , otherwise —> random name)	
    
Docker hub  —> postgres. 

Note 1:-
Fast-api :- code —> build image
Postgres :-  image 

Note 2:-
Database :- must be secure (specially user-name and password)
??  how to access  —>  db image 
 Use —> variable  ( key=value)

 **(Step 3)**
```yaml
services:
    environment:                    # environment variables
        - POSTGRES_USER=my_user				   	
        - POSTGRES_PASSWORD=my_password	  	
        - POSTGRES_DB=my_database				
```

Note 3:- 
PostgreSQL (Postgres) is open-source database software

 * Allows us to create and manage databases
 * We can create tables within a database to organize your data effectively.

Note 4:-
Postgres is running on network, like fast-api and other sites 

Require ??  -->  port to run 
Postgres default port 5432 

port :-  <localhost_port>:<container_port>

localhost_port :- any free port
container_port :-  postgres default port 5432 

**(Step 4)**
```yaml
services:
    ports:
        - '5433:5432'
```
Note 5:- 
Image —> immutable (can’t change / update)
Recreate with new version ( learning mode)

Image —> run container 
If container is lost / corrupted  —> data lost 
How —>  image: postgres :latest   (empty image)
Persistence :-  to continue doing something 
Require ?? —> data save,  use as required, can’t auto delete

Volume :- storage of data ( in our case postgres_db)

Now we create volume:-  (create storage)


**(STEP : II )** 
```yaml
services: 
  volumes:
  postgres_db:      # store data
    driver: local	  # location 
```    

note :- location (Service Providers (Google, local- machine …)
( in our case local : docker)
If container is lost / corrupted  —> data save (because of volume )

Note 6 :- 
How to use ?? —> volume:-  (  storage)

**(Step 6)**
```yaml
services:
    volumes:
        - postgres_db:/var/lib/postgresql/data
```	

Storage  :-  <localhost>:<container>

localhost :-  postgres_db
container :-   /var/lib/postgresql/data (default data directory inside a PostgreSQL container. )

## (path: postger data storage —> data location)

Map —> data sink  in volume ( if container lost  —> data secure)
  
Note 7:-
api. —> one container 
postgres_db —> other container 
Container are isolated 
System communication —> network
Network  (like we communicate through internet)

**(Step 7)**	
```yaml
services:
    networks:
      - my-api-net
```

**(STEP : III)** 
```yaml
networks:
  my-api-net:  # Define the custom network
```

Note 8:-
Flow of image ??

Database
Fast API

depend_on :-  Database
First run Database 
Secondly Fast API  

```yaml
api:
depends_on:
      - postgres_db  
```

How to connect with Database
Postgres Server —> how to access
Postgres Client 

pgAdmin is a open-source administration and management tool for PostgreSQL databases

Todo PostgresSQL_DB

## Volume (compose.yaml)

**1- Bind Mount Volume (BMV):**
A bind mount volume is a directory on the host machine that is mounted into a container.

### -./host-machine:/container

```yaml 
volumes:
      - ./todo:/code  # Sync local development directory with the container
```

**2- Persistent Volume (PV):** 
A persistent volume is a resource that is provisioned and managed by Kubernetes. It is used to store data that needs to be preserved even if a Kafka container is deleted or recreated.
In both cases, the data is stored outside of the container, so it is not lost when the container is deleted or recreated

Bind Mount Volume (BMV): a directory on the host machine that is mounted into a container.

Persistent Volume (PV): a resource that is provisioned and managed by Kubernetes.



Download and Install pgAdmin 4:
https://www.pgadmin.org/download/ 

### docker 

docker 
https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/14_docker 

### dev container

Dev Containers tutorial
https://code.visualstudio.com/docs/devcontainers/tutorial 


