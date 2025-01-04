from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

# Login ke time output mai dega terminal mai. 
def login_success(sender,request,user,**kwargs):
    print("--------------------------------")
    print("logged-in signal..run intro..")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print(f'Kwargs: {kwargs}')
    print("-----------------------------------")
user_logged_in.connect(login_success,sender=User)

# Login out ke time output mai dega terminal mai. 
@receiver(user_logged_out, sender=User)
def log_out(sender,request,user,**kwargs):
    print("--------------------------------")
    print("logged-out signal..run intro..")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print(f'Kwargs: {kwargs}')
    print("----------------------------------")
#user_logged_out.connect(login_out,sender=User)


# jab Login in failed hoga toh yeah output mai dega terminal mai. 
'''@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("--------------------------------")
    print("logged-in signal..run intro..")
    print("Sender:",sender)
    print("Request:",request)
    print("Credentials:",credentials)
    print(f'Kwargs: {kwargs}')
#user_logged_failed.connect(login_failed)'''



