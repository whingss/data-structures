class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return str(self.data)
