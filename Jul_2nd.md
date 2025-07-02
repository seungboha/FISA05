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
"""
from collections import defaultdict

my_playlist = defaultdict(list)

my_playlist['pop'].append('Got_to_Be_Real')
my_playlist['pop'].append('If_I_Run (Astronauts, etc)')
my_playlist['pop'].append('Timeless (Sergio Mendes)')
my_playlist['jpop'].append("Distance (Utada Hikaru)")
my_playlist['jazz(maybe?)'].append('We_are_all_muse')
my_playlist['NewJeans'].extend(['Attention', 
                                'Ditto', 
                                'Hype Boy', 
                                'Just pick any song'])
my_playlist['MichaelJackson'].append('Prove me wrong')
"""

my_playlist = dict()
my_playlist['pop'] = ['If I Run (Astronauts, etc)', 
                      'Baby I (Ariana Grande)']
my_playlist['jpop'] = ['Distance (Utada Hikaru)']
my_playlist['jazz(maybe?)'] = ['Timeless (Sergio Mendes)',
                               'We are all muse (Yerin Baek)']
my_playlist['pop'].append('When can I see you again')
my_playlist['NewJeans'] = ['Attention', 
                            'Ditto', 
                            'Hype Boy', 
                            'Just pick any song']
my_playlist['MichaelJackson'] = ["Just every song", "Prove me wrong"]
```

### Deep vs shallow copy
**0. This is shallow copy**
```python
greetings = ['Hello', 'Bye', 'Hi', ['GoodNight', 'GoodBye']]
greetings2 = greetings[-1]
greetings2[0] = 'GoorMorning'
print(greetings)
```
- We get ['Hello', 'Bye', 'Hi', ['GoorMorning', 'GoodBye']]
- To keep the original value, there are several methods. (Honestly, these are all I know)

**1. Library**
```python
import copy

greetings = ['Hello', 'Bye', 'Hi', ['GoodNight', 'GoodBye']]
greetings2 = copy.deepcopy(greetings[3])
greetings2[0] = 'GoodMorning'
print(greetings)
```

**2. When importing is not allowed, keep this syntax in mind.**
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