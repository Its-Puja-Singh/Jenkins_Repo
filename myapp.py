class User:
    __Count = 0

    def __init__(self, role=None, name=None, salary=None):
        if role is not None:
            self.__role = role
            self.__username = name
            self.__salary = salary
            User.__Count += 1

    def getCount(self):
        return User.__Count

    def getSalary(self):
        return self.__salary

    def getUser(self):
        print("Role : ", self.__role, ", Name : ", self.__username, ", Salary: ", self.__salary)


class UserDetails:
    def __init__(self, user=None):
        self.user = user or User()
        self.big_User = 20
        self.small_User = 5

    def checkTotalUser(self):
        count = self.user.getCount()
        if count > self.big_User:
            return 'Most Power'
        elif count < self.small_User:
            return "Least Power"
        else:
            return "All good"
if __name__ == '__main__':
    user1 = User(1, 'Puja', 101)
    user2 = User(2, 'Shivam', 102)
    user3 = User(3, 'Bhawana', 103)
    userdetail = UserDetails()
    print(userdetail.checkTotalUser())
    print(f'Total users are {user3.getCount()}')
