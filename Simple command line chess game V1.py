class ChessPiece:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def move(self, new_position):
        self.position = new_position
        
    def __str__(self):
        return f"{self.name} at {self.position}"

class ChessBoard:
    def __init__(self):
        self.board = {}
        
    def add_piece(self, piece, position):
        self.board[position] = piece
        
    def move_piece(self, piece, new_position):
        del self.board[piece.position]
        piece.move(new_position)
        self.board[new_position] = piece
        
    def __str__(self):
        board_str = ""
        for pos, piece in self.board.items():
            board_str += f"{piece}\n"
        return board_str

if __name__ == "__main__":
    board = ChessBoard()
    king = ChessPiece("King", "E1")
    queen = ChessPiece("Queen", "D1")
    board.add_piece(king, king.position)
    board.add_piece(queen, queen.position)
    print(board)
    board.move_piece(queen, "E2")
    print(board)
