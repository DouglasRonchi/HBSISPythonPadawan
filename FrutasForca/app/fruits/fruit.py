class Fruit:
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def get_length(self) -> int:
        return len(self._name)

    def __str__(self):
        return f"Name: {self.get_name().capitalize()} - Length: {self.get_length()}"
