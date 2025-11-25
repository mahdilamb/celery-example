import pytest
from celery_example.tasks import app as celery_app


@pytest.fixture(scope="session", autouse=True)
def celery_config():
    celery_app.conf.update(task_always_eager=True)
    return celery_app
