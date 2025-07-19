from Token import Token
from Tokens import *

class Tokenizer:
    def __init__(self, source):
        self.curr = 0

        self.tokens = []
        self.source = source

    def forward(self):
        self.curr += 1
    
    def peek(self):
        return self.source[self.curr + 1]
    
    def current(self):
        return self.source[self.curr]
    
    def add_token(self, token, lexeme):
        self.tokens.append(Token(token, lexeme))

    def match(self, char):
        if self.current() == char: return True
        else: return False

    def match_forward(self, char):
        if self.peek() == char:
            self.forward()
            return True
        return False

    def tokenize(self):
        
        while (self.curr < len(self.source)):
            char = self.current()

            if self.match(' '):
                pass

            elif self.match(';'):
                self.add_token(SEMICOLON, char)

            elif self.match( '+'):
                self.add_token(PLUS, char)

            elif self.match('-'):
                if self.peek() == '-':
                    while (self.current() != '\n'): self.forward()
                else:
                    self.add_token(MINUS, char)

            elif self.match('*'):
                self.add_token(MUL, char)

            elif self.match('/'):
                self.add_token(DIV, char)

            elif self.match(':'):
                if self.match_forward('='):
                    self.add_token(ASSIGNMENT, ':=')
                else:
                    self.add_token(UNKNOWN, char)

            elif self.match('='):
                if self.match_forward('='):
                    self.add_token(EQUAL, '==')
                else:
                    self.add_token(UNKNOWN, char)
                    
            elif self.match('~'):
                if self.match_forward('='):
                    self.add_token(NOT_EQUAL, '~=')
                else:
                    self.add_token(NOT, char)

            elif self.match('<'):
                if self.match_forward('='):
                    self.add_token(LESS_OR_EQUAL, '<=')
                else:
                    self.add_token(LESS_THAN, char)

            elif self.match('>'):
                if self.match_forward('='):
                    self.add_token(GREATER_OR_EQUAL, '<=')
                else:
                    self.add_token(GREATER_THAN, char)
            
            self.forward()

        return self.tokens
    