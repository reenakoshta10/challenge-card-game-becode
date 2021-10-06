class Symbol:
    """This class will store symbol of the card in cards game"""

    def __init__(self, color: str, icon: str) -> None:
        self.color: str = color
        self.icon: str = icon

    def __str__(self) -> str:
        if self.color == 'Red':
            return "\033[1;31m"+self.icon+"\033[0;0m"
        else:
            return "\033[1;37m" + self.icon +"\033[0;0m"


class Card(Symbol):
    """This class will store the value of the card in cards game"""

    def __init__(self, color: str, icon: str, value: int) -> None:
        super().__init__(color, icon)
        self.value: str = value

    def __str__(self) -> str:
        return self.value + super().__str__() 
