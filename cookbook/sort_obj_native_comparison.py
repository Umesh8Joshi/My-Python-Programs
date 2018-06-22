'''
This class will sort the object by using lambda function
'''
class User:
    '''Class User to sort by user_id'''
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

'''
usage

>>> users = [User(7), User(3), User(87)]
>>> users
[User(7), User(3), User(87)]
>>> sorted(users, key=lambda u: u.user_id)
[User(3), User(7), User(87)]

'''
