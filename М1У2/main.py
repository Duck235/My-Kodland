import random
eliments = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
quest = int(input('Какой длины вы хотите сделать пароль?'))


password = ''
for i in range(quest):
    password += random.choice(eliments)


print(password)