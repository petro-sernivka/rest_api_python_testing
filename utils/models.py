from faker import Faker

fake = Faker()


def user():
    return {
        "username": fake.user_name(),
        "email": fake.email(),
    }
