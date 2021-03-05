from faker import Faker

fake = Faker()


def user():
    return {
        "email": fake.email(),
    }
