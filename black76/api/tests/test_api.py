import pytest
from dateutil import parser
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

from api.factories import (
    CompanyFactory,
    ContactFactory,
    InteractionFactory,
)


@pytest.mark.django_db
def test_company_list():
    CompanyFactory.create(name='Acme, Inc.')
    client = APIClient()
    response = client.get(reverse('company-list'))

    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert len(data) == 1
    assert data[0]['name'] == 'Acme, Inc.'


@pytest.mark.django_db
def test_contact_list():
    ContactFactory.create(first_name='John', last_name="Smith")
    client = APIClient()
    response = client.get(reverse('contact-list'))

    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert len(data) == 1
    assert data[0]['first_name'] == 'John'
    assert data[0]['last_name'] == 'Smith'


@pytest.mark.django_db
def test_interaction_list():
    date = timezone.now()
    InteractionFactory.create(name='Acme, Inc.', date=date)
    client = APIClient()
    response = client.get(reverse('interaction-list'))

    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert len(data) == 1
    assert data[0]['name'] == 'Acme, Inc.'
    assert parser.parse(data[0]['date']) == date


