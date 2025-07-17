from Token import Token
from Tokens import *

class Tokenizer:
    def __init__(self, source):
        self.source = source

        self.start = 0
        self.curr = 0
        
        self.tokens = []
        
    def tokenize(self):
        while (self.curr < len(self.source)):
            char = self.source[self.curr]

            if char ==  '+':
                self.tokens.append(Token(TOKEN_PLUS, char))
            elif char == '-':
                self.tokens.append(Token(TOKEN_MINUS, char))
            elif char == '*':
                self.tokens.append(Token(TOKEN_MUL, char))
            elif char == '/':
                self.tokens.append(Token(TOKEN_DIV, char))

            self.curr += 1

        return self.tokens