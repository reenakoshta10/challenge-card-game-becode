class Symbol:
    """This class will store symbol of the card in cards game"""

    def __init__(self, color: str, icon: str, icon_rank: int) -> None:
        self.color: str = color
        self.icon: str = icon
        self.icon_rank = icon_rank

    def __str__(self) -> str:
        return "symbol: " + self.color + " " + self.icon


class Card(Symbol):
    """This class will store the value of the card in cards game"""

    def __init__(self, color: str, icon: str, value: str, rank: int, icon_rank: int) -> None:
        super().__init__(color, icon, icon_rank)
        self.value: str = value
        self.rank: int = rank

    def __str__(self) -> str:
        return super().__str__() + " value: " + self.value
