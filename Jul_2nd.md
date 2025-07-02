# Today's Notes

> tuple is immutable  

- ```==``` : element-wise comparison is possible!!  

```python
a = [1, [1, 2, 3], 3]
b = [1, [1, 2, 3], 3]
a == b
```

---
### Recall  
- defaultdict
```python
from collections import defaultdict

my_playlist = defaultdict(list)

my_playlist['pop'].append('Got_to_Be_Real')
my_playlist['pop'].append('If_I_Run (Astronauts, etc)')
my_playlist['jpop'].append("Distance (Utada Hikaru)")
my_playlist['jazz(maybe?)'].append('We_are_all_muse')
```

### Deep vs shallow copy
- Using library

```python
greetings = ['Hello', 'Bye', 'Hi', ['GoodNight', 'GoodBye']]
greetings2 = greetings[-1]
greetings2[0] = 'GoorMorning'
print(greetings)
```

- We get ['Hello', 'Bye', 'Hi', ['GoorMorning', 'GoodBye']]
- To keep the original value, there are several methods. (These are all I know)

1. Library

```python
import copy

greetings = ['Hello', 'Bye', 'Hi', ['GoodNight', 'GoodBye']]
greetings2 = copy.deepcopy(greetings[3])
greetings2[0] = 'GoodMorning'
print(greetings)
```

2. When importing is not allowed, keep this syntax in mind.

```python
greetings = ['Hello', 'Bye', 'Hi', ['GoodNight', 'GoodBye']]
greetings2 = []
for ele in greetings[-1]:
    greetings2.append(ele)
greetings2[0] = "GoodMorning"
print(greetings)
print(greetings2)
```

We can keep the original values