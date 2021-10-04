class Symbol:
    """This class will store symbol of the card in cards game"""

    def __init__(self, color: str, icon: str) -> None:
        self.color: str = color
        self.icon: str = icon

    def __str__(self) -> str:
        return "symbol: " + self.color + " " + self.icon


class Card(Symbol):
    """This class will store the value of the card in cards game"""

    def __init__(self, color: str, icon: str, value: int) -> None:
        super().__init__(color, icon)
        self.value: str = value

    def __str__(self) -> str:
        return super().__str__() + " value: " + self.value
