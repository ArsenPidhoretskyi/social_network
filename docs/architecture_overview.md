# Social Network: Architecture overview #

We use [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) to run all application components and backing services in isolated environment.

## Software versions ##

* Python **[3.11](https://docs.python.org/)**, installed via [pyenv](https://github.com/pyenv/pyenv).
* Django **[latest stable](https://docs.djangoproject.com/)**, installed via [pip](https://pypi.python.org/pypi) - official Python package index.
* Postgres **[15.0](https://www.postgresql.org/docs/15.0/static/index.html)**, installed via [official Docker image](https://hub.docker.com/_/postgres).

## Postgres databases ##

| DB name | Description | Owner |
| ------- | ----------- | ----- |
| `social_network_db` | database for main application | `postgres` |
