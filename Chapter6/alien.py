aliens  = []

for alien_number in range(30):
    new_alien = {'color':'green','points':'5','speed':'low'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 20
        alien['speed'] = 'fast'


for alien in aliens[:5]:
    print(alien)


print('...')
print(f'Create {len(aliens)} aliens')
