from Token import Token
from Tokens import *

class Tokenizer:
    def __init__(self, source):
        self.start = 0
        self.curr = 0

        self.tokens = []
        self.source = source

    def forward(self):
        self.curr += 1
    
    def peek(self):
        return self.source[self.curr + 1]
    
    def current(self):
        return self.source[self.curr]
    
    def add_token(self, token):
        self.tokens.append(Token(token, self.source[self.start : self.curr + 1]))

    def match(self, char):
        if self.current() == char: return True
        else: return False

    def peek_match(self, char):
        if (self.peek() == char): return True
        else: return False

    def match_forward(self, char):
        if self.peek() == char:
            self.forward()
            return True
        return False

    def tokenize(self):
        
        while (self.curr < len(self.source)):
            self.start = self.curr
            char = self.current()

            if self.match(' '):
                pass

            elif self.match(','):
                self.add_token(COMMA)

            elif self.match(';'):
                self.add_token(SEMICOLON)

            elif self.match('('):
                self.add_token(OPEN_PAREN)

            elif self.match(')'):
                self.add_token(CLOSE_PAREN)

            elif self.match( '+'):
                self.add_token(PLUS)

            elif self.match('-'):
                if self.peek() == '-':
                    while (self.current() != '\n'): self.forward()
                else:
                    self.add_token(MINUS)

            elif self.match('*'):
                self.add_token(MUL)

            elif self.match('/'):
                self.add_token(DIV)

            elif self.match(':'):
                if self.match_forward('='):
                    self.add_token(ASSIGNMENT)
                else:
                    self.add_token(UNKNOWN)

            elif self.match('='):
                if self.match_forward('='):
                    self.add_token(EQUAL)
                else:
                    self.add_token(UNKNOWN)
                    
            elif self.match('~'):
                if self.match_forward('='):
                    self.add_token(NOT_EQUAL)
                else:
                    self.add_token(NOT)

            elif self.match('<'):
                if self.match_forward('='):
                    self.add_token(LESS_OR_EQUAL)
                else:
                    self.add_token(LESS_THAN)

            elif self.match('>'):
                if self.match_forward('='):
                    self.add_token(GREATER_OR_EQUAL)
                else:
                    self.add_token(GREATER_THAN)

            elif char.isdigit():
                while self.peek().isdigit(): self.forward()

                if self.match_forward('.'):
                    while self.peek().isdigit(): self.forward()
                    self.add_token(FLOAT)
                else:
                    self.add_token(INTEGER)

            elif self.match("\"") or self.match("'"):
                self.forward()
                self.start = self.curr

                while not(self.peek_match(char)): self.forward()
                self.add_token(STRING)

                self.forward()

            elif char.isalpha() or char == '_':
                while self.peek().isalnum() or self.peek_match('_'): self.forward()
                token = self.source[self.start : self.curr + 1]

                if (keywords.get(token) != None):
                    self.add_token(keywords[token])
                else:
                    self.add_token(IDENTIFIER)
            
            self.forward()

        return self.tokens
    