from django.apps import AppConfig
from django.core.signals import request_finished 


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from . import signals
        from django.contrib.auth import get_user_model
        request_finished.connect(receiver=signals.handle_registered_user,sender=get_user_model())

        # DOES REQUEST_FINISH KNOW ITS POST SAVE OR OTHERS?
        # THE SENDER PARAMETER FOR CONNECT AND THE SENDER PARAMTER IN RECEIVER DECORATOR FUNCTION AND THE SENDER PARAMETER IN THE RECEIVER FUNCTION THE SAME THING? 
        # WHY PASS IT THREE TIMES  IF THEY ARE THE SAME MODEL...
        # CAN ONE REQUEST_FINISH CONNECT MULTIPLE SENDERS? OR ITS DONE BY ONE?
        #   
        return super().ready()
