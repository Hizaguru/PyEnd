import unittest
from project.database.db import connect_to_database, if_user_exists

class TestSum(unittest.TestCase):

    def test_if_user_exist(self):
        connection = connect_to_database()
        user_exist = if_user_exists(connection, "tests", "test")
        self.assertEqual(user_exist, None)



if __name__ == '__main__':
    unittest.main()
