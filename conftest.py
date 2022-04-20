import pytest
from pytest_factoryboy import register

# from core_apps.profiles.tests.factories import ProfileFactory
from core_apps.users.tests.factories import UserFactory

register(UserFactory)
# register(ProfileFactory)


@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    print(new_user)
    return new_user

@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user