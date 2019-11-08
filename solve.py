class IncorrectREException(Exception):
    pass


def apply_or_operator(first_remainder_set, second_remainder_set, operands_stack):
    operands_stack.append(first_remainder_set.union(second_remainder_set))


class Solver:
    regexp = ""
    letter = ""
    letters_count = 0

    __CONCAT_OPERATOR = "."

    __OR_OPERATOR = "+"

    __REPEAT_OPERATOR = "*"

    __EMPTY_WORD = "1"

    __ALPHABET = {'a', 'b', 'c'}

    def __init__(self, regexp, letter, letters_count):
        self.regexp = regexp
        self.letter = letter
        self.letters_count = int(letters_count)

    @staticmethod
    def is_binary_operator(symbol):
        return symbol == Solver.__CONCAT_OPERATOR or symbol == Solver.__OR_OPERATOR

    @staticmethod
    def is_repeat_operator(symbol):
        return symbol == Solver.__REPEAT_OPERATOR

    @staticmethod
    def is_letter(symbol):
        return symbol in Solver.__ALPHABET

    @staticmethod
    def is_empty_word(symbol):
        return symbol == Solver.__EMPTY_WORD

    def apply_repeat_operator(self, remainder_set, operands_stack):
        new_set = set(remainder_set)
        old_set = set()
        while new_set != old_set:
            old_set = set(new_set)
            for element1 in old_set:
                for element2 in old_set:
                    new_set.add((element1 + element2) % self.letters_count)

        operands_stack.append(new_set)

    def apply_or_operator(self, first_remainder_set, second_remainder_set, operands_stack):
        operands_stack.append(first_remainder_set.union(second_remainder_set))

    def apply_concat_operator(self, first_remainder_set, second_remainder_set, operands_stack):
        tmp_set = set()
        for first_set_element in first_remainder_set:
            for second_set_element in second_remainder_set:
                tmp_set.add((first_set_element + second_set_element) % self.letters_count)
        operands_stack.append(tmp_set)

    def solve(self):
        if self.letter not in Solver.__ALPHABET:
            raise IncorrectREException("Wrong character")

        operands_stack = []
        for token in list(self.regexp):
            if self.is_empty_word(token):
                operands_stack.append({0})

            elif self.is_letter(token):
                operands_stack.append({int(token == self.letter)})

            elif self.is_repeat_operator(token):
                if len(operands_stack) >= 1:
                    operand = operands_stack.pop(len(operands_stack) - 1)
                    self.apply_repeat_operator(operand, operands_stack)
                else:
                    raise IncorrectREException("Not enough elements on stack (less than 1)")

            elif self.is_binary_operator(token):
                if len(operands_stack) >= 2:
                    first_operand = operands_stack.pop(len(operands_stack) - 1)
                    second_operand = operands_stack.pop(len(operands_stack) - 1)
                    if token == Solver.__CONCAT_OPERATOR:
                        self.apply_concat_operator(first_operand, second_operand, operands_stack)
                    else:
                        self.apply_or_operator(first_operand, second_operand, operands_stack)
                else:
                    raise IncorrectREException("Not enough elements on stack (less than 2)")

            else:
                raise IncorrectREException("Wrong character: {}".format(token))

        if len(operands_stack) != 1:
            raise IncorrectREException()
        else:
            if 0 in operands_stack[0]:
                print("YES")
            else:
                print("NO")
