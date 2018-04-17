import unittest
import homework3
import itertools


class UnitTests(unittest.TestCase):
    def test_invalid_path(self):
        """
        Test if ValueError is raised for invalid paths.
        """
        path = '../does/not/exist.db'
        with self.assertRaises(ValueError):
            homework3.create_dataframe(path)

    def test_column_names(self):
        """
        Test if the dataframe only contains the expected columns.
        """
        path = '../LectureNotes/Data-Essentials/class.db'
        df = homework3.create_dataframe(path)
        requiredCols = ['language', 'video_id', 'category_id']
        self.assertSetEqual(set(df.columns), set(requiredCols))

    def test_row_count(self):
        """
        Test if the dataframe contains the expected no. of rows.
        """
        path = '../LectureNotes/Data-Essentials/class.db'
        df = homework3.create_dataframe(path)
        self.assertEqual(len(df), 75005)

    def test_check_key(self):
        """
        Test if none of the cols in the dataframe form a key.
        """
        path = '../LectureNotes/Data-Essentials/class.db'
        df = homework3.create_dataframe(path)
        combs = []

        # generate all possible combinations of keys
        for size in range(1, len(df.columns)):
            combs += list(itertools.combinations(df.columns, size))

        # Since there are duplicate rows in the df, we
        # would expect none of the column combinations to
        # be a key.
        for c in combs:
            grouping = df.groupby(c)
            self.assertNotEqual(len(grouping), len(df))


suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
