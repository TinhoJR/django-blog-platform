from django import template
from django.utils.timezone import datetime 


register = template.Library()


# FILTER REGISTRATION

@register.filter(name="separator")
def separator(value):
    return ",".join(value)


@register.filter(name="emojify")
def emojify(value,emoji):
    return str(value) + emoji 


@register.filter(name="caps")
def caps(value):
    return len(value)



# TAG REGISTRATION

@register.simple_tag(name="greeting")
def greeting():
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


@register.simple_tag(name="convert")
def convert(a,b,c):
      pass





