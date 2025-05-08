Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> alien_0 = {'olor':'green','points':5}
>>> print(alien_0['olor'])
green
>>> print(alien_0['points'])
5
>>> 
>>> alien_0={'color':'green','points':5}
>>> new_points=alien_0['points']
>>> print(f"You just earned {new_points} points!")
You just earned 5 points!
>>> 
>>> alien_0 = {'color':'green','points':5}
>>> print(alien_0)
{'color': 'green', 'points': 5}
>>> alien_0['x_position'] = 0
>>> alien_0['y_position'] = 25
>>> print(alien_0)
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
>>> 
>>> alien_0 = {'color':'green'}
>>> print(f"The alien is {alien_0['color']}.")
The alien is green.
>>> alien_0['color'] = 'yellow'
>>> print(f"The alien is now {alien_0['color']}.")
The alien is now yellow.
>>> 
>>> KeyboardInterrupt
>>> alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
>>> print(f"Original position: {alien_0['x_position']}")
Original position: 0
>>> if alien_0['speed'] == 'slow':
...     x_increment = 1
... elif alien_0['speed'] == 'medium':
...     x_increment = 2
... else:
...     x_increment = 3
... #The new position is the old position plus the increment.
... alien_0['x_position'] = alien_0['x_position'] + x_increment
... print(f"New position: {alien_0['x_position']}")
SyntaxError: invalid syntax
>>> print(f"New position: {alien_0['x_position']}")
New position: 0
>>> 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
{'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)
{'color': 'green'}

KeyboardInterrupt
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    
KeyboardInterrupt
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'rust',
        }
    
language = favorite_languages['sarah'].title()
    
print(f"Sarah's favorite language is {language}.")
    
Sarah's favorite language is C.

alien_0 = {'color': 'green', 'speed': 'slow'}
    
print(alien_0['points'])
    
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(alien_0['points'])
KeyError: 'points'
alien_0={'color':'green','speed':'slow'}
    
print(alien_0['points'])
    
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(alien_0['points'])
KeyError: 'points'

alien_0 = {'color': 'green', 'speed': 'slow'}
    
point_value = alien_0.get('points', 'No point value assigned.')
    
print(point_value)
    
No point value assigned.


