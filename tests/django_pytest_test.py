import pytest
# pip install pytest pytest-django pytest-cov
from django.test import Client
from django.urls import reverse
from proj_maths.models import CustomUser


# декоратор. Говорит нам, что в каждом тесте нужно инициировать клиент, в котором мы будет проводить тесты
@pytest.fixture
def client():
    client = Client()
    response = client.post('/login/', {'username': 'admin', 'password': 'qwerty'})
    return client

def test_hello_world(client):
    response = client.get(reverse("terms_list"))
    assert "Список терминов" in response.content

@pytest.mark.django_db
def test_user_creation():
    user = CustomUser.objects.create(phone="89123123145", age=29)
    assert user.age == 29