# Day 19: Automated API Testing

## What we are testing

The test suite covers the full employee API:

- `POST /employees`
- `GET /employees`
- `GET /employees/{id}`
- `PUT /employees/{id}`
- `DELETE /employees/{id}`
- Request validation failures (`422`)
- Missing employees (`404`)
- Duplicate email conflicts (`409`)

## How the tests work

```text
test_employees.py -> TestClient -> FastAPI -> employee_service -> SQLite
```

`TestClient` sends requests directly to the FastAPI application. It does not
start a real web server, and we do not need to open Swagger.

Each test receives a fresh temporary SQLite database through a pytest fixture.
This keeps tests independent and prevents them from changing `employees.db`.

## Arrange, Act, Assert

Most tests follow three simple steps:

1. **Arrange** the input data and any existing employee.
2. **Act** by calling an endpoint with `TestClient`.
3. **Assert** the status code and response body.

## Run the project

```bash
cd day19
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger is available at `http://127.0.0.1:8000/docs` while the server runs.

## Run the tests

```bash
cd day19
source .venv/bin/activate
pytest -v
```

For a shorter output, run `pytest -q`.

# Docker Compose

# What is Docker Compose?

Docker Compose is a tool used to define and run a group of related containers from one YAML file, usually named compose.yaml.

For example, a web application may need:

An application container

A database container

A Redis cache

A background worker

Instead of starting each container manually with separate docker run commands, Compose lets us describe the complete application once and manage it as one unit.

services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      DATABASE_URL: postgres://appuser:password@db:5432/appdb
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: password
      POSTGRES_DB: appdb
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:

# Why is Docker Compose more useful with 3–5 containers?

For a single container, a short docker run command may be enough. Compose still works, but its advantage is smaller because there is only one image, port, and container to manage.

With three to five containers, manual commands quickly become harder to manage. Each container may need its own ports, environment variables, volumes, network settings, and startup dependencies. The containers must also be able to find and communicate with one another.

Compose makes this easier by keeping the complete setup in one version-controlled file. A developer can start the application, database, cache, and worker with one command:

docker compose up

Compose also creates a shared network automatically. In the example above, the application reaches PostgreSQL using the service name db instead of finding the database container's changing IP address.

The main benefits for a multi-container application are:

One file describes the entire local environment.

One command starts all related containers.

Services can communicate using their service names.

Configuration is consistent across developers' machines.

Logs from all services can be viewed together.

The complete environment can be stopped and removed together.

# What is a service?

A service is the Compose definition of one application component. It tells Docker how to create and run that component's container.

In the example, app and db are services. A service can define its image or build instructions, ports, environment variables, volumes, networks, health checks, and other runtime settings.

A service usually creates one container, but it can also be scaled to multiple container instances when the application supports it.

# What does build: . mean?

build: . tells Compose to build a Docker image using the current directory (.) as the build context.

By default, Docker looks for a file named Dockerfile in that directory. Files required by the Dockerfile, such as application source code or dependency files, must be inside the build context.

services:
  app:
    build: .

This is different from image: nginx:latest, which downloads or uses an already-built image.

What does ports do?

ports publishes a container port on the host machine. The common format is:

ports:
  - "HOST_PORT:CONTAINER_PORT"

For example:

ports:
  - "8080:8080"

This sends traffic received on port 8080 of the host to port 8080 inside the container. It allows a browser or another program outside the Compose network to reach the application.

Containers in the same Compose network normally communicate directly through service names and container ports, so every internal service does not need to publish a host port.

# What does environment do?

environment sets environment variables inside a container. Applications use them for runtime configuration such as database addresses, feature settings, usernames, or log levels.

environment:
  DATABASE_HOST: db
  LOG_LEVEL: info

Environment variables help keep configuration separate from application code. Passwords and other secrets should not be committed directly to the Compose file. For local development, they can be supplied through an ignored .env file or another secure secret-management method.

# What does volumes do?

volumes connects storage outside a container's writable layer to a path inside the container.

Common volume types include:

Named volume: Docker-managed persistent storage, often used for database data.

Bind mount: Maps a specific host file or directory into the container, often used to make local source-code changes immediately available during development.

# Example of a named volume:

services:
  db:
    image: postgres:16
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:

The database writes to /var/lib/postgresql/data, but the actual data is kept in the postgres-data volume outside the container's writable layer.

# docker compose up versus docker compose down

docker compose up creates and starts the services defined in the Compose file. It also creates required networks and volumes if they do not already exist. By default, it attaches to the containers and displays their logs.

docker compose up

Use -d to run the services in the background:

docker compose up -d

docker compose down stops and removes the containers and default networks created by Compose:

docker compose down

Named volumes are preserved by default, which protects persistent data. To deliberately remove them as well, use:

docker compose down --volumes

That option is destructive for data stored in those volumes and should be used carefully.

# Why persistent data should not live only inside a container

A container should be treated as replaceable. It may be deleted and recreated during a rebuild, deployment, upgrade, failure recovery, or docker compose down operation.

If important data exists  only in the container's writable layer, deleting that container deletes the data with it. This is especially dangerous for databases, uploaded files, and other state that must survive restarts or replacements.

Persistent data should be stored in a named volume, bind-mounted storage, or an external managed service. This separates the application's lifecycle from the data's lifecycle. The container can then be rebuilt or replaced without losing the application data.
