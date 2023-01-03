def vote(bday_year):
    from datetime import datetime
    today = datetime.now()
    age = today.year - bday_year
    if 16 <= age < 18 or age > 65:
        print(f'Age: {age}. Your vote is optional.')
    elif age < 16:
        print(f"Age: {age}. You don't vote.")
    else:
        print(f'Age: {age}. You must vote.')


vote(int(input('Enter your year of birth: ')))



