import factory
from django.db.models.signals import post_save
from faker import Factory as FakerFactory

from core_apps.profiles.models import Profile
from core_apps.users.tests.factories import UserFactory

faker = FakerFactory.create()

@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    phone_number = factory.LazyAttribute(lambda x: faker.phone_number())
    about_me = factory.LazyAttribute(lambda x: faker.sentence(nb_words=5))
    gender = factory.LazyAttribute(lambda x: faker.country_code() )