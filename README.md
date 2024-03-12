# Reecheble Finance Web-API


Reecheble Finance **Web-API** application built in Python using the
`Ports & Adapters` architecture.

<img src="./assets/application_architecture.svg" alt="Microservice Architecture">

## Developer Setup Guide

This section outlines the development setup of the Reecheble Finance **Web-API** application.
> **_NOTE:_** These steps will apply when the project's directory has been set as
> the working directory. Adjust accordingly if the working directory is different
> from project directory.


1. Clone the repository to your development environment.
   ```
   git clone <repository_url>
   ```
2. Install `poetry` to the environment using `pip`. Poetry can be installed system-wide.
   ```
   pip install poetry
   ```
3. Install project dependencies using `poetry`.
   ```
   poetry install
   ```
4. Activate `pre-commit` hooks.
   ```
   poetry run pre-commit install --hook-type commit-msg --hook-type pre-push
   ```
5. Start the server by running the `main.py` file located in the project directory.

6. Visit [API Host Service](http://0.0.0.0:8000/latest/docs) to view documentation.

## Docker Setup Guide

This section outlines the setup for a docker container.

## Stack Overview

### Overall
| Library        | Description               | External Content                 |
|----------------|---------------------------|----------------------------------|
| [sqlalchemy]() | ORM                       | [Introduction]() > [Deep Dive]() |
| [pydantic]()   | Parser                    | [Introduction]() > [Deep Dive]() |
| [asyncio]()    | Asyncronous processessing | [Introduction]() > [Deep Dive]() |

### API Server
The swagger document can be found at [API Host Service](http://0.0.0.0:8000/latest/docs)

| Library                                 | Description            | External Content                                                                                     |
|-----------------------------------------|------------------------|------------------------------------------------------------------------------------------------------|
| [fastAPI](https://fastapi.tiangolo.com) | Design & document APIs | [Introduction](https://blog.devgenius.io/brief-introduction-to-fastapi-d6f25793b11a) > [Deep Dive]() |
| [uvicorn](https://www.uvicorn.org/)     | Web Server             | [Introduction]() > [Deep Dive]()                                                                     |

### Testing
| Library                                                              | Description                 | External Content                                                                                                                                     |
|----------------------------------------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [pytest](https://docs.pytest.org/en/7.1.x/index.html)                | Testing framework           | [Introduction](https://docs.pytest.org/en/7.1.x/getting-started.html) > [Deep Dive](https://docs.pytest.org/en/7.1.x/reference/reference.html)       |
| [hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html) | UnitTest creation framework | [Introduction](https://hypothesis.readthedocs.io/en/latest/quickstart.html) > [Deep Dive](https://hypothesis.readthedocs.io/en/latest/settings.html) |

### Database Migrations
| Library     | Description         | External Content                 |
|-------------|---------------------|----------------------------------|
| [alembic]() | Database Migrations | [Introduction]() > [Deep Dive]() |

## Features

### Included
- [X] Dependency setup using poetry
- [X] Rolling file logging with console output
- [X] Swagger Documented APIs (FastAPI)
- [x] Docker containerization
- [x] Unit Testing

### Feature Backlog
- [ ] Kubernetes cluster integration
- [ ] Event messaging integration
- [ ] API Stress Testing
