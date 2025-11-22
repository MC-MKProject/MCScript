from src.lexer import Lexer
from src.parser import Parser

def run(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    print("[MCS] Running:", file_path)
    tokens = Lexer(code).tokenize()
    print("Tokens:", tokens)

    ast = Parser(tokens).parse()
    print("AST:", ast)

if __name__ == "__main__":
    run("examples/hello.mc")
