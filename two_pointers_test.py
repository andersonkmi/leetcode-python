from two_pointers import pair_sum_sorted_brute_force, pair_sum_sorted

def test_when_array_empty_return_empty():
    numbers = []
    target = 7
    result = pair_sum_sorted_brute_force(numbers, target)
    assert result == []

def test_pair_sum_when_array_empty_return_empty():
    numbers = []
    target = 7
    result = pair_sum_sorted(numbers, target)
    assert result == []

def test_with_single_item_array():
    numbers = [2]
    target = 3
    result = pair_sum_sorted_brute_force(numbers, target)
    assert result == []

def test_pair_sum_with_single_item_array():
    numbers = [2]
    target = 3
    result = pair_sum_sorted(numbers, target)
    assert result == []

def test_with_two_numbers_not_reachable_target():
    numbers = [3, 3]
    target = 7
    result = pair_sum_sorted_brute_force(numbers, target)
    assert result == []

def test_pair_sum_with_two_numbers_not_reachable_target():
    numbers = [3, 3]
    target = 7
    result = pair_sum_sorted(numbers, target)
    assert result == []

def test_with_two_numbers_reachable_target():
    numbers = [3, 4]
    target = 7
    result = pair_sum_sorted_brute_force(numbers, target)
    assert result == [0, 1]

def test_pair_sum_with_two_numbers_reachable_target():
    numbers = [3, 4]
    target = 7
    result = pair_sum_sorted(numbers, target)
    assert result == [0, 1]

def test_with_multiple_numbers_not_reachable_target():
    numbers = [3, 4, 5]
    target = 20
    result = pair_sum_sorted_brute_force(numbers, target)
    assert result == []

def test_pair_sum_with_multiple_numbers_not_reachable_target():
    numbers = [3, 4, 5]
    target = 20
    result = pair_sum_sorted(numbers, target)
    assert result == []

def test_with_multiple_numbers_reachable_target():
    numbers = [3, 4, 5]
    target = 9
    result = pair_sum_sorted_brute_force(numbers, target)
    assert result == [1, 2]

def test_pair_sum_with_multiple_numbers_reachable_target():
    numbers = [3, 4, 5]
    target = 9
    result = pair_sum_sorted(numbers, target)
    assert result == [1, 2]

def test_with_multiple_numbers_reachable_target_multiple_pairs():
    numbers = [3, 4, 5, 6, 7]
    target = 11
    result = pair_sum_sorted_brute_force(numbers, target)
    assert result == [1, 4]

def test_pair_sum_with_multiple_numbers_reachable_target_multiple_pairs():
    numbers = [3, 4, 5, 6, 7]
    target = 11
    result = pair_sum_sorted(numbers, target)
    assert result == [1, 4]
