import pytest

@pytest.mark.smoke
def test_valid_login():
    assert {"status": "success"}["status"] == "success"

@pytest.mark.smoke
def test_invalid_login():
    response = {"status": "unauthorized"}
    assert response["status"] == "unauthorized"

@pytest.mark.regression
def test_profile_update():
    profile = {"name": "automation-user", "updated": True}
    assert profile["updated"] is True

@pytest.mark.regression
def test_logout():
    session = {"active": False}
    assert session["active"] is False
