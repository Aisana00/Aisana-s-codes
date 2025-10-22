def all_true(tuple_data):
    return all(tuple_data)

test_tuples = [
    (True, True, True),
    (1, 2, 3),
    ("hello", [1, 2], 5),
    (True, False, True),
    (0, 1, 2),
    ("", "world"),
    (None, 1),
    ()
]

for test_tuple in test_tuples:
    result = all_true(test_tuple)
    print(f"{test_tuple} -> {result}")