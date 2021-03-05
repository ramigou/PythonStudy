import random

user_name = input('Enter your name: ')
print('Hello,', user_name)
rule = input()
print("Okay, let's start")

# get score from rating.txt
rating = open('rating.txt', 'r')
rating_dict = {}
for line in rating.readlines():
    name, score = line.strip('\n').split()
    rating_dict[name] = int(score)

if user_name in rating_dict.keys():
    user_score = rating_dict.get(user_name)
else:
    user_score = 0

hard_rule = 'rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire'
normal_rule = ''

winning_cases_normal = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
winning_cases_hard = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
normal_option = ['rock', 'paper', 'scissors']
hard_option = ['rock', 'paper', 'scissors', 'dragon', 'devil', 'gun', 'water', 'fire', 'snake', 'human', 'tree', 'wolf',
               'sponge', 'air', 'lightning']

while True:
    user_option = input()

    if user_option == '!rating':
        print('Your rating:', user_score)
    elif user_option in normal_option and rule == normal_rule:
        option = random.choice(normal_option)
        if user_option == option:
            print(f'There is a draw ({option})')
            user_score += 50
        elif winning_cases_normal[user_option] == option:
            print(f'Well done. The computer chose {option} and failed')
            user_score += 100
        else:
            print(f'Sorry, but the computer chose {option}')
    elif user_option in hard_option and rule == hard_rule:
        option = random.choice(hard_option)
        if user_option == option:
            print(f'There is a draw ({option})')
            user_score += 50
        elif option in winning_cases_hard[user_option]:
            print(f'Well done. The computer chose {option} and failed')
            user_score += 100
        else:
            print(f'Sorry, but the computer chose {option}')
    elif user_option == '!exit':
        print('Bye!')
        break
    else:
        print('Invalid input')

rating.close()
