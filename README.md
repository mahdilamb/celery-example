# Celery example

Very basic example demonstrating the usage of [celery](https://docs.celeryq.dev/) for a task queue.

All the tasks can be found in the shared module [tasks.py](./src/celery_example/tasks.py). These are then called by the [package](./src/celery_example/__main__.py).

```mermaid
flowchart TD

    A["Application calls task.add(x, y)"] --> B["Celery sends task to RabbitMQ broker"]

    B --> C["RabbitMQ queues the task"]

    C --> D["Celery worker fetches task"]

    D --> E["Worker executes add(x, y)"]

    E --> F["Worker stores result in Redis"]

    A --> W["Application waits for result"]

    W --> G["Application requests result from Redis"]

    G --> H["Redis returns result"]

```

## Docker testing

For testing, you can either use docker:

1. Copy the env file:

    ```shell
    cp .env.example .env
    ```

2. Run services

   ```shell
   docker compose up
   ```

## Pytest testing

For testing in pytest, we add an [autouse fixture](./tests/conftest.py#L6) which converts the app into eager evaluation and thus does not backends.
