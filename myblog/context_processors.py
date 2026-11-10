
from django.utils.timezone import datetime

def greet():
        current_time = datetime.now()
        current_time = current_time.hour
        
        greeting = "MORNING"
        if current_time >= 12 and current_time < 17:
                greeting = "AFTERNOON"

        elif current_time >= 17 and current_time < 20:
                greeting = "EVENING"  

        elif current_time >= 20 or current_time < 4:
                greeting = "NIGHT" 
        else:
            greeting = greeting

        intro_greeting = "GOOD {}".format(greeting)  
        return intro_greeting                      


def global_site_data(request):
    ctx = {
        "c_name" : "FIRST GLOBAL TESTING",
        "c_age"  : 50,
        "greeting": greet(),
        "name" : "Tinho"
    }

    return ctx


    