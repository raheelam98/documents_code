# kong

Kong:- api gateway

**1a :- create extensions approach**

```yaml
```

```yaml
x-kong-config: ## (variable approach : call extension Start from x)
  &kong-env  ##(name of extension)
## Note 1b :- use extensions 
environment:
      <<: *kong-env  (use extension here)
```      

**Note 2 : Services (4 services)**

```yaml
kong-migrations:     ## (.service 1)
kong-migrations-up:  ## (.service 2)
kong:                ## (.service 3)
db:                  ## (.service 4)
```

**Note3 :- kong:  (.service 3)**


**kong - docker-compose.yaml**

```yaml
version: ‘3.9’. (schema)

x-kong-config: (variable approach : call extension Start from x)
  &kong-env  (name of extension)
  KONG_DATABASE: ${KONG_DATABASE:-postgres}. (.)
  KONG_PG_DATABASE: ${KONG_PG_DATABASE:-kong} (.)
  KONG_PG_HOST: db
  KONG_PG_USER: ${KONG_PG_USER:-kong}
  KONG_PG_PASSWORD_FILE: /run/secrets/kong_postgres_password

volumes:
  kong_data: {}
  kong_prefix_vol:
    driver_opts:
      type: tmpfs
      device: tmpfs
  kong_tmp_vol:
    driver_opts:
      type: tmpfs
      device: tmpfs

networks:
  default:
    driver: bridge

services:

  kong-migrations:   ## (.service 1)
    image: "${KONG_DOCKER_TAG:-kong:latest}"
    command: kong migrations bootstrap
    profiles: [ "database" ]
    depends_on:
      - db
    environment:
      <<: *kong-env  (use extension here)
    secrets:
      - kong_postgres_password
    restart: on-failure

  kong-migrations-up: ## (.service 2)
    image: "${KONG_DOCKER_TAG:-kong:latest}"
    command: kong migrations up && kong migrations finish
    profiles: [ "database" ]
    depends_on:
      - db
    environment:
      <<: *kong-env
    secrets:
      - kong_postgres_password
    restart: on-failure

  kong:              ## (.service 3)
    image: “${KONG_DOCKER_TAG:-kong:latest}"(.create latest image)
    user: "${KONG_USER:-kong}"
    environment:
      <<: *kong-env
      KONG_ADMIN_ACCESS_LOG: /dev/stdout
      KONG_ADMIN_ERROR_LOG: /dev/stderr
      KONG_PROXY_LISTEN: “${KONG_PROXY_LISTEN:-0.0.0.0:8000}" (.im)
      KONG_ADMIN_LISTEN: "${KONG_ADMIN_LISTEN:-0.0.0.0:8001}"
      KONG_ADMIN_GUI_LISTEN: "${KONG_ADMIN_GUI_LISTEN:-0.0.0.0:8002}"
      KONG_PROXY_ACCESS_LOG: /dev/stdout
      KONG_PROXY_ERROR_LOG: /dev/stderr
      KONG_PREFIX: ${KONG_PREFIX:-/var/run/kong}
      KONG_DECLARATIVE_CONFIG: "/opt/kong/kong.yaml"
    secrets:
      - kong_postgres_password
    ports:
      # The following two environment variables default to an insecure value (0.0.0.0)
      # according to the CIS Security test.
      - "${KONG_INBOUND_PROXY_LISTEN:-0.0.0.0}:8000:8000/tcp"
      - "${KONG_INBOUND_SSL_PROXY_LISTEN:-0.0.0.0}:8443:8443/tcp"
      # Making them mandatory but undefined, like so would be backwards-breaking:
      # - "${KONG_INBOUND_PROXY_LISTEN?Missing inbound proxy host}:8000:8000/tcp"
      # - "${KONG_INBOUND_SSL_PROXY_LISTEN?Missing inbound proxy ssl host}:8443:8443/tcp"
      # Alternative is deactivating check 5.13 in the security bench, if we consider Kong's own config to be enough security here

      - "127.0.0.1:8001:8001/tcp"
      - "127.0.0.1:8444:8444/tcp"
      - "127.0.0.1:8002:8002/tcp"
    healthcheck:
      test: [ "CMD", "kong", "health" ]
      interval: 10s
      timeout: 10s
      retries: 10
    restart: on-failure:5
    read_only: true
    volumes:
      - kong_prefix_vol:${KONG_PREFIX:-/var/run/kong}
      - kong_tmp_vol:/tmp
      # - ./config:/opt/kong
    security_opt:
      - no-new-privileges

  db: (.service 4)
    image: postgres:9.5
    profiles: [ "database" ]
    environment:
      POSTGRES_DB: ${KONG_PG_DATABASE:-kong}
      POSTGRES_USER: ${KONG_PG_USER:-kong}
      POSTGRES_PASSWORD_FILE: /run/secrets/kong_postgres_password
    secrets:
      - kong_postgres_password
    healthcheck:
      test:
        [
          "CMD",
          "pg_isready",
          "-d",
          "${KONG_PG_DATABASE:-kong}",
          "-U",
          "${KONG_PG_USER:-kong}"
        ]
      interval: 30s
      timeout: 30s
      retries: 3
    restart: on-failure
    stdin_open: true
    tty: true
    volumes:
      - kong_data:/var/lib/postgresql/data

secrets:
  kong_postgres_password:
    file: ./POSTGRES_PASSWORD
```


Profiles
https://docs.docker.com/compose/compose-file/15-profiles/

Using profiles with Compose
https://docs.docker.com/compose/profiles/

GenAI Quarter 5 Online Class 14: Protobuf in Kafka & Introduction to Kong - An API Gateway
https://www.youtube.com/watch?v=nMXMV48EiQA&t=5332s 

learn-generative-ai/05_microservices_all_in_one_platform
/17_kong/
https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/17_kong