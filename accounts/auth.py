from accounts.models import User
from django.contrib.auth.hashers import make_password, check_password

class Authentication:
    def siginup(self, email:str , password:str) -> User| bool:
        user = User.objects.filter(email=email).first()
        
        if user and check_password(password, user.password):
            return user

        return False    


    def siginup(self, name:str ,email:str , password:str) -> User| bool:
        user = User.objects.filter(email=email).exists()
        
        if user:
            return False
        
        user = User.objects.create(
            name=name,
            email=email,
            password=make_password(password)
        )
        return user
