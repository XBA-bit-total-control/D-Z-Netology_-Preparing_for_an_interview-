from main import Stack
import pytest


@pytest.fixture
def get_this_stack():
    this_stack = Stack()
    for el in "(((([{}]))))":
        this_stack.push(el)
    return this_stack.show_stack()


@pytest.fixture
def get_two_stack():
    two_stack = Stack()
    for el in "{{[()]}}":
        two_stack.push(el)
    return two_stack.show_stack()


@pytest.fixture
def get_final_stack():
    final_stack = Stack()
    for el in "[([])((([[[]]])))]{()}":
        final_stack.push(el)
    return final_stack.show_stack()


@pytest.fixture
def get_bad_stack():
    bad_stack = Stack()
    for el in "}{}":
        bad_stack.push(el)
    return bad_stack.show_stack()


@pytest.fixture
def get_very_bad_stack():
    very_bad_stack = Stack()
    for el in "{{[(])]}}":
        very_bad_stack.push(el)
    return very_bad_stack.show_stack()


@pytest.fixture
def get_not_balans_stack():
    not_balans_stack = Stack()
    for el in "[[{())}]":
        not_balans_stack.push(el)
    return not_balans_stack.show_stack()