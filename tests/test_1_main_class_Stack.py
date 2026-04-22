from main import Stack
import pytest


# Фикстура в коде / подготовительные данные
this_stack = Stack()
two_stack = Stack()
final_stack = Stack()

bad_stack = Stack()
very_bad_stack = Stack()
not_balans_stack = Stack()


@pytest.mark.parametrize(
    "stack",
    [
        this_stack, two_stack, final_stack,
        bad_stack, very_bad_stack, not_balans_stack,
    ]
)
def test_method_is_empty_without_elements(stack):
    assert stack.is_empty() == True, "Стек должен быть пуст"


@pytest.mark.parametrize(
    "element, expected",
    [("}", "}"),
     ("{", "{"),
     ("}", "}")]
)
def test_additions_non_balanced_stacks_by_elements(element, expected):
    bad_stack.push(element)
    assert bad_stack.peek() == expected, "Не верный элемент добавлен!"


def test_additions_balanced_stacks_fully_1():
    for el in "(((([{}]))))":
        this_stack.push(el)
    assert this_stack.show_stack() == "(((([{}]))))", "Конечный стек не совпадает с заданным"


def test_additions_balanced_stacks_fully_2():
    for el in "{{[()]}}":
        two_stack.push(el)
    assert two_stack.show_stack() == "{{[()]}}", "Конечный стек не совпадает с заданным"


def test_additions_balanced_stacks_fully_3():
    for el in "[([])((([[[]]])))]{()}":
        final_stack.push(el)
    assert final_stack.show_stack() == "[([])((([[[]]])))]{()}", "Конечный стек не совпадает с заданным"


def test_additions_non_balanced_stacks_fully_1():
    for el in "{{[(])]}}":
        very_bad_stack.push(el)
    assert very_bad_stack.show_stack() == "{{[(])]}}", "Конечный стек не совпадает с заданным"


def test_additions_non_balanced_stacks_fully_2():
    for el in "[[{())}]":
        not_balans_stack.push(el)
    assert not_balans_stack.show_stack() == "[[{())}]", "Конечный стек не совпадает с заданным"


def test_additions_unsuitable_elements():
    try:
        try:
            bad_stack.push("Б")
        except ValueError:
            bad_stack.push("Слово")
        else:
            raise AssertionError("Буквы и иные символы не должны добавляться")

    except ValueError:
        pass

    except (Exception, AssertionError):
        raise AssertionError("Не верная ошибка при исполнении")

    else:
        raise AssertionError("Последовательность или слово добавляться не должны")


@pytest.mark.parametrize(
    "stack, expected",
    [(bad_stack, 3),
     (two_stack, 8),
     (final_stack, 22)]
)
def test_method_size(stack, expected):
    assert stack.size() == expected, f"Длина стека равная '{expected}' не верная"


@pytest.mark.parametrize(
    "expected",
    ["}", "{", "}"]
)
def test_method_pop(expected):
    assert bad_stack.pop() == expected, "Элемент не удалён или удален не верно"


@pytest.mark.parametrize(
    "stack",
    [
        this_stack, two_stack, final_stack,
        very_bad_stack, not_balans_stack,
    ]
)
def test_method_is_empty_with_elements(stack):
    assert stack.is_empty() == False, "Стек не заполнен"


@pytest.mark.parametrize(
    "stack, expected",
    [
        (this_stack, "(((([{}]))))"),
        (two_stack, "{{[()]}}"),
        (final_stack, "[([])((([[[]]])))]{()}"),
        (bad_stack, ""),
        (very_bad_stack, "{{[(])]}}"),
        (not_balans_stack, "[[{())}]"),
    ]
)
def test_method_show_stack(stack, expected):
    assert stack.show_stack() == expected, f"Стек '{expected}' не корректный"