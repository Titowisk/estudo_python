birthdays = {'Alice': 'Apr 01', 'Bob': 'Dec 12', 'Carol': 'Mar 04'}

while True:
    name = input('Enter a name: (blank to quit) ')
    if name == '':
        break

    if name in birthdays:
        print('{} is the birthday of {}'.format(birthdays[name], name))
    else:
        print('I do not have a birthday information for {}'.format(name))
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
