# pyfsm

This is a library aimed to help to implement Finite State Machines. It's not stable yet

## Requirements
```
pip install -r requirements.txt
```

## Usage
Finite State Machines must be defined in json. See example provided.

```python
from pyfsm.finite_state_machine import FiniteStateMachine
import json


class ExampleFST(FiniteStateMachine):
    def __init__(self, fsm_filepath):

        with open(fsm_filepath, 'r') as f:
            content = f.read()
        self.fsm = json.loads(content)
        self.current_state = self.fsm.keys()[-1]
        super(ExampleFST, self).__init__()


    # State callbacks
    def on_created(self, msg):
        print 'Entering CREATE'

    def onleave_created(self, msg):
        print 'Leaving CREATE'

    def on_state1(self, msg):
        print 'Entering STATE1'

    def onleave_state1(self, msg):
        print 'Leaving STATE1'

    def on_state2(self, msg):
        print 'Entering STATE2'

    def onleave_state2(self, msg):
        print 'Leaving STATE2'


if __name__ == '__main__':
    fsm = ExampleFST('./example.json')
    print fsm.current_state
    fsm.event('move_to_1', {})
    fsm.event('move_to_2', {})
    fsm.event('move_to_1', {})
    fsm.event('move_to_created', {})
    print fsm.current_state
```

## Testing
PyFSM uses tox to manage tests.

```
pip install tox
tox -r
```


## TODO

- Add fsm generator
- Add json docs
- Add loaders for other formats
- Add callbacks docs