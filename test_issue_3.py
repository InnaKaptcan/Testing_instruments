import unittest
from typing import List, Tuple


class TestOneHotEncoder(unittest.TestCase):
    def test_ft(self):
        actual = fit_transform('Moscow', 'New York', 'Moscow', 'London')
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_one_unique(self):
        actual = fit_transform('Moscow', 'Moscow', 'Moscow', 'Moscow')
        expected = [
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1]),
        ]
        self.assertEqual(actual, expected)

    def test_output_type(self):
        result = fit_transform('a', 'b', 'c')
        self.assertTrue(isinstance(result, list))


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


if __name__ == '__main__':
    pass
