import pytest
from dotenv import dotenv_values
import os


def pytest_sessionstart(session):  # type: ignore
    """Setup before tests start."""

    # Update the environment with example env
    os.environ["ENV"] = "TESTING"
    for key, val in dotenv_values(".env.example").items():
        os.environ[key] = val  # type: ignore


@pytest.fixture(scope="session", autouse=True)
def celery_config():
    from celery_example.tasks import app as celery_app

    celery_app.conf.update(task_always_eager=True)
    return celery_app
