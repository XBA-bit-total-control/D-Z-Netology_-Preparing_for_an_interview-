# Задание № 1
class Stack:
    """
    Создаст вам стек с небольшим функционалом
    по взаимодействию с ним
    """
    def __init__(self):
        self.__stack = ''

    def is_empty(self):
        return not bool(self.__stack)

    def push(self, n_item):
        if n_item in ['[', '(', '{', '}', ')', ']']:
            self.__stack += n_item
            return
        else:
            raise ValueError("Такое тебе не добавить в стек!")

    def pop(self):
        if not self.is_empty():
            self.rem = self.__stack[-1]
            self.__stack = self.__stack[:-1]
            return self.rem
        else:
            return None

    def peek(self):
            return self.__stack[-1] if not self.is_empty() else None

    def size(self):
        return len(self.__stack)

    def show_stack(self):
        return self.__stack


# Задание № 2
def check_balance(cons,  sqr = 0, mer = 0, crl = 0):
    """
    Рекурсивная функция проверки сбалансированности поданного стека
    """
    if len(cons) == 0:
        return not any([sqr, mer, crl])

    if sqr < 0 or mer < 0 or crl < 0:
        return False

    if cons[0] == '[':
        return check_balance(cons[1:], sqr + 1, mer, crl)
    elif cons[0] == '{':
        return check_balance(cons[1:], sqr, mer + 1, crl)
    elif cons[0] == '(':
        return check_balance(cons[1:], sqr, mer, crl + 1)
    elif cons[0] == ')':
        return check_balance(cons[1:], sqr, mer, crl - 1)
    elif cons[0] == '}':
        return check_balance(cons[1:], sqr, mer -1, crl)
    elif cons[0] == ']':
        return check_balance(cons[1:], sqr - 1, mer, crl)
    else:
        return check_balance(cons[1:], sqr, mer, crl)