from datetime import datetime

import factory

from minihub.models import(
    Company,
    Contact,
    Interaction,
)


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker('name')


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    company = factory.SubFactory(CompanyFactory)


class InteractionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Interaction

    date = factory.LazyFunction(datetime.now)
    name = factory.Faker('name')

    @factory.post_generation
    def contacts(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for contact in extracted:
                self.contacts.add(contact)
