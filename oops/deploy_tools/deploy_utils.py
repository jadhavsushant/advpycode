import random
import string

PASSWORD_LENGTH = 25


class Genpassword:
    '''this class is build for generate password'''

    def __init__(self):
        self.password_lengh = PASSWORD_LENGTH

    def get_secret(self,):
        '''generate password'''
        lw_letters = string.ascii_letters
        up_letters = string.ascii_uppercase
        digit = string.digits
        str_concat = lw_letters + up_letters + digit
        raw_pass = "".join(random.sample(str_concat, self.password_lengh))
        return raw_pass


class Args():
    def __init__(self,kwargs):
        self.first_name = kwargs['fname']
        self.last_name = kwargs['lname']
        pass
    
    def load(self):
        data = self.first_name, self.last_name
        print(str(data))
        # print(str(self.first_name, self.last_name))


new_args = Args({'fname': 'Sushant', 'lname':'Jadhav'})

print(type(new_args.load()))
