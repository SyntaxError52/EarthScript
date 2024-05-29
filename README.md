# Earthscript
## A New Python Superset
### A python superset with a 27 line compliler

Python Example
```python
import time as tm
def sayHello(name):
  print(f'Hello, {name}')
  tm.sleep(2)
  print(f'Goodbye, {name}')
# Runs the main function
sayHello('Person')
```

EarthScript Example
```
include time as tm
func sayHello(name)[
  print(f'Hello, <name>')
  tm.sleep(2)
  print(f'Goodbye, <name>')
]
//Runs the main function
sayHello('Person')
```
