class chess:

    def __init__(self, xLetter, yNumber, name, color, IsWhite):
        self.xLetter = xLetter
        self.yNumber = yNumber
        self.name = name
        self.color = color
        self.IsWhite = True

    def returnxletter(self, xLetter):
        return xLetter
    def returnyNumber(self, yNumber):
        return yNumber
    def __repr__(self):
        self.name = self.name.lower()
        self.IsWhite = True
        if self.name == "pawn" and self.IsWhite:
            return "♙"
        elif self.name == "horse" and self.IsWhite:
            return "♘"
        elif self.name == "bishop" and self.IsWhite:
            return "♗"
        elif self.name == "king" and self.IsWhite:
            return "♔"
        elif self.name == "queen" and self.IsWhite:
            return "♕"
        elif self.name == "rook" and self.IsWhite:
            return "♖"
        elif self.name == "pawn" and self.IsWhite == False:
            return "♟️"
        elif self.name == "rook" and self.IsWhite == False:
            return "♜"
        elif self.name == "knight" and self.IsWhite == False:
            return "♞"
        elif self.name == "bishop" and self.IsWhite == False:
            return "♝"
        elif self.name == "queen" and self.IsWhite == False:
            return "♛"
        elif self.name == "king" and self.IsWhite == False:
            return "♚"
        else:
            return "Hi"

        
        
chessPiece = chess("a",1, "rook", "white", True)
print(chessPiece)