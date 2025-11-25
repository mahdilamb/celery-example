from celery_example.tasks import add


def test_add():
    """Test basic maths are correctly calculated."""
    result = add.delay(2, 3).get()
    assert result == 5
