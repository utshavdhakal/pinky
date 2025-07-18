from Token import Token
from Tokens import *

class Tokenizer:
    def __init__(self, source):
        
        self.curr = 0

        self.tokens = []
        self.source = source

    def forward(self):
        self.curr += 1
    
    def peek(self, offset=1):
        return self.source[self.curr + offset]
        
    def tokenize(self):
        while (self.curr < len(self.source)):
            char = self.peek(offset=0)

            if char == ' ':
                pass
            elif char ==  '+':
                self.tokens.append(Token(TOKEN_PLUS, char))
            elif char == '-':
                if self.peek() == '-':
                    while (self.peek(offset=0) != '\n'): self.forward()
                else:
                    self.tokens.append(Token(TOKEN_MINUS, char))
            elif char == '*':
                self.tokens.append(Token(TOKEN_MUL, char))
            elif char == '/':
                self.tokens.append(Token(TOKEN_DIV, char))
            
            self.forward()

        return self.tokens