# coding=utf-8

from faker import Faker

faker = Faker()
print(faker.provider('faker.providers.credit_card')._generate_number('410000', 16))

print(faker.credit_card_number())
#print(faker._generate_number('410000', 16))
