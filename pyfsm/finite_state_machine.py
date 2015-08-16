class NotValidTransitionException(Exception):
    pass


class ImplementFSMException(Exception):
    pass


class NotCurrentStateException(Exception):
    pass


class FiniteStateMachine(object):

    def __init__(self):
        if not self.fsm:
            raise ImplementFSMException()
        if not self.current_state or self.current_state not in self.fsm.keys():
            raise NotCurrentStateException()
        self.states = self.fsm.keys()
        self.initial_state = self.current_state

    def event(self, event_name, msg):
        if not self.is_valid_transition(event_name):
            raise NotValidTransitionException()
        self.make_transition(event_name, msg)

    def is_valid_transition(self, event_name):
        transitions = self.fsm[self.current_state]
        for transition in transitions:
            if event_name == transition['event']:
                return True
        return False

    def make_transition(self, event_name, msg):
        transitions = self.fsm[self.current_state]
        for transition in transitions:
            if event_name == transition['event']:
                self.make_callbacks(self.current_state, transition['dest'], msg)
                self.current_state = transition['dest']
                break

    def make_callbacks(self, leaving_state, new_state, msg):
        try:
            eval('self.onleave_'+leaving_state.lower()+'(msg)')
        except AttributeError as e:
            pass
        try:
            eval('self.on_'+new_state.lower()+'(msg)')
        except AttributeError as e:
            pass

    def reset_initial_state(self):
        self.current_state = self.initial_state
