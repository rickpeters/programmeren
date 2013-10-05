#Learn to Program: The Fundamentals
Cursus op coursera.org: https://www.coursera.org/course/programming1

Samen met Sander vanaf 19 augustus 2013

Doel: ervaring opdoen met Python, een mooie algemene moderne webtaal

##week 1: installatie en andere zaken
Python handige locaties:
Python programming FAQ: http://docs.python.org/3/faq/programming.html#faq-argument-vs-parameter
Python visualizer: http://pythontutor.com/visualize.html#
Python Documentation: http://docs.python.org/3

Python tutorial op Codecademy: http://www.codecademy.com/tracks/python

##week 2: functions

Hoe bedien je de interactieve help functie
**TODO**

* functie definitie
```python
def foo (number):
    """ (number) -> int

    description
    >>> foo(4.0)
    4
    """
    return int(number)
```

types:
* `int`, `float`, number (een int of een float, voor type contract, geen echt type)

operators:
* `//` : integer deling (`10 // 3 -> 3`)
* `%` : module, integer rest van deling (`10 % 4 -> 2`)
* stop je er een float in, dan krijg je als resultaat een float

design-recipe:
* examples
* type contract
* header
* description
* body
* test

pycharm zaken:
* working directory wordt niet geappend aan sys.path bij opstarten console
* print (sys.path) laat dit zien
* sys.path.append("/Users/rickpeters/Documents/programmeren/python/week2/assignment") lost dit op!
* vervolgens moet je nog wel een 'import {module}' en/of een 'from {module} import *' doen
* issue aangemaakt bij Jetbrains: Request #9772 "Python console : sys.path n..." created
** conform specs, je kunt wel in project settings de content root aan passen of sourcefiles toevoegen
** makkelijker is om de directory met de opdracht zelfstandig te openen (file open directory...) in zelfde window en
toe te voegen aan huidige projectlijst. Als je dan een console opent vanuit een file in dit (sub)project dan wordt
deze als content root geopend. Buiten het specifieke project worden alle project directories als content root geopend

week 3: boolean en if
* boolean: `True` en `False`
* operators en volgorde: ```not```, ```and```, ```or```
* python syntax eigenschap, let op : aan einde regel voor markeren blok bij een if, elif en else
```python
if change == True:
    # block
elif change == False:
    # block
else:
    # block
```

