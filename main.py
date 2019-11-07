from solve import *


def main():
    regexp, word, number = input().split()

    try:
        solver = Solver(regexp, word, number)
        solver.solve()
    except IncorrectREException as e:
        print(e)


if __name__ == "__main__":
    main()
