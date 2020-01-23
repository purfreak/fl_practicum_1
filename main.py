from solve import *


def main(regexp, word, number):
    try:
        solver = Solver(regexp, word, number)
        if solver.solve():
            print("YES")
        else:
            print("NO")
    except IncorrectREException as e:
        print(f"Incorrect Regular expression: {e}")
    except Exception as e:
        print(f"Unknown exception: {e}")


if __name__ == "__main__":
    main(*input().split())
