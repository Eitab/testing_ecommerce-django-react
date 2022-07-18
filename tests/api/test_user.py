from rest_framework.response import Response
import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient

from base.models import Product

client = APIClient()

'''
Integration testing testing api to register user
'''
@pytest.mark.django_db
def test_register_user():
    payload = dict(
        name="testing123",
        email="test11@test.com",
        password="super-secret"
    )
    response = client.post("/api/users/register/", payload)
    data = response.data
    assert data["name"] == payload["name"]
    assert data["username"] == payload["email"]
    assert "password" not in data

@pytest.mark.django_db
def test_login_user():
    payload = dict(
        name="toti",
        email="toti_kk@gmail",
        password="totikk"
    )
    client.post("/api/users/register/", payload)
    response = client.post("/api/users/login/", dict(username="toti_kk@gmail",password="totikk"))
    data = response.data
    assert data["username"] == payload["email"]
    assert response.status_code == 200 # status 200 for login success


@pytest.mark.django_db
# wrong username and pass
def test_login_user_fail():
    response = client.post("/api/users/login/", dict(username="totibb_kk@gmail",password="totitgkk"))
    assert response.status_code == 401 # 401 for failed login

@pytest.mark.django_db
# mandatory fields
def test_failed_login():
    response = client.post("/api/users/login/", dict(username="totibb_kk@gmail"))
    assert response.status_code == 400 # 400 client error-תחביר בקשה פגום

@pytest.mark.django_db
def test_show_user_profile():
    payload = dict(
        name="toti",
        email="toti_kk@gmail",
        password="totikk"
    )
    client.post("/api/users/register/", payload)
    response = client.post("/api/users/login/", dict(username="toti_kk@gmail", password="totikk"))
    response = client.get('http://127.0.0.1:8000/#/profile')
    assert response.status_code == 200







