class Action:
    def __init__(self):
        self.actions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

    def get_actions(self):
        return self.actions