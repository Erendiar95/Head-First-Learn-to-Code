def avatar(hair, hair_length, eyes, gender, has_glasses, has_beard):
    if hair == '':
        hair = 'brown'
        
    if hair_length == '':
        hair_length = 'short'

    if eyes == '':
        eyes = 'blue'

    if gender == '':
        gender = 'female'

    if has_glasses == '':
        has_glasses = 'no'

    if has_beard == '':
        has_beard = 'no'
    
    print('You chose', hair)
    print('You chose', hair_length)
    print('You chose', eyes)
    print('You chose', gender)
    print('You chose', has_glasses)
    print('You chose', has_beard)


hair = input('What color hair [brown]? ')
hair_length = input('What hair length [short]? ')
eyes = input('What eye color [blue]? ')
gender = input('What gender [female]? ')
has_glasses = input('Has glasses [no]? ')
has_beard = input('Has beard [no]? ')

avatar(hair, hair_length, eyes, gender, has_glasses, has_beard)
