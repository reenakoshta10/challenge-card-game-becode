class Symbol:
    """This class will store symbol of the card in cards game"""

    def __init__(self, color: str, icon: str, icon_rank: int) -> None:
        self.color: str = color
        self.icon: str = icon
        self.icon_rank = icon_rank

    def __str__(self) -> str:
        if self.color == 'Red':
            return "\033[1;31m"+self.icon+"\033[0;0m" # print symbol in Red color
        else:
            return "\033[1;37m" + self.icon +"\033[0;0m" # print symbol in white color


class Card(Symbol):
    """This class will store the value of the card in cards game"""

    def __init__(
        self, color: str, icon: str, value: str, rank: int, icon_rank: int
    ) -> None:
        super().__init__(color, icon, icon_rank)
        self.value: str = value
        self.rank: int = rank

    def __str__(self) -> str:
        return self.value + super().__str__() 
