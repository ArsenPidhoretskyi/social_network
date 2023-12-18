## Docker

To start project faster we use docker and docker compose. In docker compose file we have all services that we need to
run, some of them mapped to local ports, so we can access them from the host machine.
You can change default ports by create `.env` file in `docker` directory and set variables with the same name as in
`docker-compose.yml` file.

Example of `.env` file:

```dotenv
API_LOCAL_PORT=8099 # change default port for api service from 8000 to 8099
```

## Services

### api

The `api` service is responsible for running django application.
The api service has the following configurations:

 - Command: `make run` (runs the API, see `api/Makefile` for details)
 - Ports: `${LOCAL_IP:-127.0.0.1}:${API_LOCAL_PORT:-8000}:8000` (by default maps http://localhost:8000 to the API container)
 - Environment File: `../api/.env` (loads environment variables from the specified file)
 - Volumes: `../api:/opt/api` (mount `api` directory to `/opt/api` in the container, to make
sure that we have the same code in the container and on the host machine for development purposes.)

#### api build
 - Target `local` is used to build image for local development, check `docker/images/api/Dockerfile` for details.
 - Target `live` is used to build image for production. `docker/images/api/Dockerfile` - is production ready, but docker
   compose configuration only for local development.

### postgres-db

The `postgres-db` service is a PostgreSQL database service.
