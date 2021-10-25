# Boilerplate
- [VueCLI](https://github.com/vuejs/vue-cli)
- [Django](https://github.com/django/django)
- [Django Rest Framework](https://github.com/encode/django-rest-framework)
- [Channels](https://github.com/django/channels)
- [Celery](https://github.com/celery/celery)
- [Flower](https://github.com/mher/flower)
- [Containerized](https://www.docker.com/)
- [Postgres](https://github.com/postgres/postgres)
- [Redis](https://github.com/redis/redis)

## Getting Started

- Copy `.env.template` to `.env` and make neceessary changes
- Run `docker-compose up --build -d` to complete setup
- Browse to http://localhost to view the application

## How it works

The demo application is a simple task management app, that allows user to login and manage tasks. Tasks can be executed and users will be notified when tasks are complete.

- The frontend application for task management is built with [VueCLI](https://github.com/vuejs/vue-cli) (80)
- The backend API is built with [Django](https://github.com/django/django) and [Django Rest Framework](https://github.com/encode/django-rest-framework) (8000)
- A background worker running [Celery](https://github.com/celery/celery) to execute long-running tasks (8000)
- Frontend is connected via web sockets to the backend using Channels (WS)
- Worker sends messages to frontend using sockets when tasks are completed
- Channels and Celery both use [Redis](https://github.com/redis/redis) as message broker (6379)
- Workers and tasks can be monitored using [Flower](https://github.com/mher/flower) (5555)
- [Postgres](https://github.com/postgres/postgres) is the primary database (5432), but [SQLite](https://github.com/sqlite/sqlite) will be used if environment variables are not found
- Postgres is managed by [PGAdmin](https://github.com/postgres/pgadmin4) (8080)