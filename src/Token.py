class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.value = lexeme

    def __repr__(self):
        return f"({self.token_type}, {self.value})"