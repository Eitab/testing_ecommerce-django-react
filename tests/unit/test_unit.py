from rest_framework.response import Response
import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient
from base.models import Review

from base.models import Product

client = APIClient()
'''
Unit tests -> checking user creation func
'''
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('tatocc','nancy@gmail.com','tato cac')
    count = User.objects.all().count()
    assert count == 1

@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True

@pytest.mark.django_db
def test_delete_user(user_1):
    user = User.objects.get(id=user_1.id)
    user.delete()
    count = User.objects.all().count()
    assert count == 0

@pytest.mark.django_db
def test_update_username(user_1):
    user=User.objects.create_user('tatocc','nancy@gmail.com','tato cac')
    user_update=User.objects.get(id=user_1.id)
    user_update.username='alex'
    assert 'alex' == user_update.username

'''
Unit tests -> product
'''

#unit test- testing if prpduct can be created as a unit (by it self with out dependecies)
def create_product():
  return Product.objects.create(
        name="Product Name",
        price=0,
        brand="Sample brand ",
        countInStock=0,
        category="Sample category",
        description=" ")

def create_product_review():
    return Review.objects.create(
        product=create_product(),
        name=User.username,
        rating=5,
        comment="very good"
    )

@pytest.mark.django_db
def test_product_creation():
    p = create_product()
    assert isinstance(p, Product) is True
    assert p.name == "Product Name"

@pytest.mark.django_db
def test_ProductReview():
    p = create_product_review()
    assert p.rating == 5
    assert p.comment == "very good"

@pytest.mark.django_db
def test_product_data():
    p = create_product()
    assert p.name == "Product Name"
    assert p.price == 0
    assert p.brand == "Sample brand "
    assert p.countInStock == 0
    assert p.category == "Sample category"
    assert p.description == " "