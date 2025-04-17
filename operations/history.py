from collections import deque


class History_Manager:
    """Manage calculation history"""
    def __init__(self):
        self.history = deque(maxlen=5)
    
    def add_entry(self, entry):
        """Add history entry to the array"""
        self.history.append(entry)
    
    def get_history(self):
        """Return 5 last history data"""
        return "\n".join(self.history[-5:])
