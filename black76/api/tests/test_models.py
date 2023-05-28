import pytest

from minihub.factories import (
    ContactFactory,
    InteractionFactory,
)


@pytest.mark.django_db
def test_interaction_has_contacts():
    interaction = InteractionFactory.create(
        contacts=(ContactFactory.create(), ContactFactory.create()),
    )
    assert interaction.contacts.count() == 2


@pytest.mark.django_db
def test_contact_has_company():
    contact = ContactFactory.create()
    assert contact.company.name
