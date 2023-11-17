import unittest
import datetime

#symbol: capitalized, 1-7 alpha characters
class Test1(unittest.TestCase):
    def symbol_test(self):
        test = ['ABC', '123', 'TEST', 'aBC', '']
        results = [True, False, True, False, False]

        for symbol, expected in zip(test, results):
            result = symbol.isupper() and symbol.isalpha()
            self.assertEqual(result, expected)


#chart type: 1 numeric character, 1 or 2
class Test2(unittest.TestCase):
    def chart_type_test(self):
        test = ['0', '1', '2', 'x', '']
        results = [False, True, True, False, False]

        for chart_type, expected in zip(test, results):
            result = chart_type in ['1', '2']
            self.assertEqual(result, expected)


#time series: 1 numeric character, 1 - 4
class Test3(unittest.TestCase):
    def time_series_test(self):
        test = ['0', '1', '2', '3', '4', 'x', '']
        results = [False, True, True, True, True, False, False]

        for time_series, expected in zip(test, results):
            result = time_series in ['1', '2', '3', '4']
            self.assertEqual(result, expected)


#start date: date type YYYY-MM-DD
class Test4(unittest.TestCase):
    def test_start_date(self):
        test = ['2023-01-01', '2023/01/01', '23-1-1','']
        results = [True, False, False]

        for date, expected in zip(test, results):
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
                result = True
            except ValueError:
                result = False
            self.assertEqual(result, expected)


#end date: date type YYYY-MM-DD
class Test5(unittest.TestCase):
    def test_end_date(self):
        test = ['2023-01-01', '2023/01/01', '23-1-1','']
        results = [True, False, False]

        for date, expected in zip(test, results):
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
                result = True
            except ValueError:
                result = False
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()