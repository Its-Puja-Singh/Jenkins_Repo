import unittest
from myapp import UserDetails, User

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

if __name__ == '__main__':
    unittest.main()
