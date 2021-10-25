import unittest
from unittest.mock import MagicMock, patch, Mock
from user.User import User, UserDetails
import user.User

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user1 = User(1, 'Rahul', 3500)
        cls.user2 = User(2, 'Rohit', 2200)

    def setUp(self):
        self.userDetails = UserDetails()

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

    def test_user(self):
        sal1 = self.user1.getSalary()
        self.assertEqual(sal1, 3500)

    def test_user_details(self):
        user = User()
        #print (user.getCount())
        #print (self.userDetails.checkTotalUser())
        self.assertEqual(self.userDetails.checkTotalUser(), "Least Power")

    @patch('user.User.User')
    def test_usercount_with_mock(self, MockUser):
        user = MockUser()
        user.getCount.return_value = 155
        self.user_detail = UserDetails(user)
        #print (user.getCount())
        #print(self.user_detail.checkTotalUser())
        self.assertEqual(self.user_detail.checkTotalUser(), "All good")

    def test_with_magicmock(self):
        user = User()
        user.getCount = MagicMock(return_value=1500)
        print(user.getCount())
        self.userdetail = UserDetails(user)
        self.assertEqual(self.userdetail.checkTotalUser(), "More Power")

if __name__ == '__main__':
    unittest.main()
