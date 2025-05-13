from typing import List


class HistoryManager:
    """Manage calculation history."""
    MAX_HISTORY = 5

    def __init__(self):
        """Initialize the history manager."""
        self.history: List[str] = []

    def add_entry(self, entry: str) -> None:
        """Add a history entry.

        Args:
            entry (str): The calculation or result to add.
        """
        self.history.append(entry)

    def get_history(self) -> str:
        """Return the last MAX_HISTORY entries as a string."""
        return "\n".join(self.history[-self.MAX_HISTORY:])

    def clear_history(self) -> None:
        """Clear all history entries."""
        self.history.clear()
