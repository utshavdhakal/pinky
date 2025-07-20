import sys
sys.path.append('src')

from Tokenizer import Tokenizer

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError("Usage: python main.py [script.pinky]")

    file = sys.argv[1]
    print(file)

    with open(file, 'r') as file:
        source = file.read()
        print(source)

    tokens = Tokenizer(source).tokenize()
    
    for token in tokens:
        print(token)