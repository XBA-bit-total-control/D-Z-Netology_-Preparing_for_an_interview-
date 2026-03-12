from main import check_balance


def test_func_check_balance_this_stack(get_this_stack):
    assert check_balance(get_this_stack) == True,\
        f"Сбалансированность {get_this_stack} стека проверена не верно"


def test_func_check_balance_two_stack(get_two_stack):
    assert check_balance(get_two_stack) == True,\
        f"Сбалансированность {get_two_stack} стека проверена не верно"


def test_func_check_balance_final_stack(get_final_stack):
    assert check_balance(get_final_stack) == True,\
        f"Сбалансированность {get_final_stack} стека проверена не верно"


def test_func_check_balance_bad_stack(get_bad_stack):
    assert check_balance(get_bad_stack) == False,\
        f"Сбалансированность {get_bad_stack} стека проверена не верно"


def test_func_check_balance_very_bad_stack(get_very_bad_stack):
    assert check_balance(get_very_bad_stack) == False,\
        f"Сбалансированность {get_very_bad_stack} стека проверена не верно"


def test_func_check_balance_not_balans_stack(get_not_balans_stack):
    assert check_balance(get_not_balans_stack) == False,\
        f"Сбалансированность {get_not_balans_stack} стека проверена не верно"