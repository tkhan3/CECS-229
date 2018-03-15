## A Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(str(alien_0) + "\n")

# Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print('Alien1: ' + str(alien_1))

# Modifying Values in a Dictionary
alien_2 = {'color': 'green'}
print("The alien is " + alien_2['color'] + ".")
alien_2['color'] = 'yellow'
print("The alien is now " + alien_2['color'] + ".")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(str(alien_0) + "\n")

# Looping Through a Dictionary
# Looping Through All Key-Value Pairs
user_0 = {
'username': 'efermi',
'first'   : 'enrico',
'last'    : 'fermi',
}

for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)








































































