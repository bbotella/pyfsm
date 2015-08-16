import unittest
from pyfsm.finite_state_machine import FiniteStateMachine, NotValidTransitionException


class TestFSM(FiniteStateMachine):

    fsm = {
        'CREATED': [
            {
                'event': 'move_to_1',
                'dest': 'STATE1'
            }
        ],
        'STATE1': [
            {
                'event': 'move_to_created',
                'dest': 'CREATED'
            },
            {
                'event': 'move_to_2',
                'dest': 'STATE2'
            }
        ],
        'STATE2': [
            {
                'event': 'move_to_1',
                'dest': 'STATE1'
            },
            {
                'event': 'move_to_created',
                'dest': 'CREATED'
            },
            {
                'event': 'stay_here',
                'dest': 'STATE2'
            }
        ]
    }

    def __init__(self):
        self.current_state = self.fsm.keys()[-1]
        super(TestFSM, self).__init__()


class PyFSMTest(unittest.TestCase):

    def setUp(self):
        self.pyFsm = TestFSM()

    def test_initial_state(self):
        self.assertEqual(self.pyFsm.current_state, 'CREATED')

    def test_invalid_transition(self):
        with self.assertRaises(NotValidTransitionException):
            self.pyFsm.event('Not a valid event', 'Not a valid message')

    def test_transition(self):
        self.pyFsm.event('move_to_1', 'Message')
        self.assertEqual(self.pyFsm.current_state, 'STATE1')
