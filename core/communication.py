from django.conf import settings
from django.core.mail import EmailMessage,send_mail,send_mass_mail,get_connection
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist


class CustomEmail():
    
    def __init__(self,user,sender="support"):
        # THE AVAILABLE SENDERS ARE SUPPORT AND SECURITY

        self.user = user   

        senders = {"support": settings.EMAIL_HOST_SUPPORT,
                   "security": settings.EMAIL_HOST_SECURITY
                   }
        # GET THE NEEDED SENDER FROM THE DICTIONARY
        self.send_from = senders.get(sender,settings.EMAIL_HOST_SUPPORT)
        # self.auth_connection = get_connection()

    SENDER_SUPPORT = "support"  
    SENDER_SECURITY = "security"    

    # MAIN SEND EMAIL METHOD
    def send_email(self,receivers_email_list,subject,message,headers=None):
        default_headers = {"Content-Type": "text/plain"} 
        headers = headers or default_headers
        mail = EmailMessage(subject=subject,
                            body=message,
                            from_email=self.send_from,
                            to=receivers_email_list,
                            headers=headers)
        mail.send()

    def send_html_email(self,receivers_email_list,subject,template=None,context=None,headers=None):
        feedback = {}
       
        try:
            # message = render_to_string(template,context)
            message = "HELLOOOO"
            
        except TemplateDoesNotExist:
            feedback["error_message"] = "Template Does Not Exist"
            feedback["status"] = "failed"

        if feedback.get("status") != "failed":
            
            default_headers = {"Content-Type": "text/plain"} 
            headers = headers or default_headers
            mail = EmailMessage(subject=subject,
                                body=message,
                                from_email=self.send_from,
                                to=receivers_email_list,
                                headers=headers)
            # mail.send()
            # mail.content_subtype = "html"
            mail.send(fail_silently=False)
            print("DONE")

            feedback["status"] = "success"


        return feedback


    def send_registration_email(self):
            context = {"user": self.user}
            subject = "Registration Notification"
            template = "emails/registration-mail.html"
            receiver = [self.user.email]

            print(receiver)
            print(self.send_from)
            
            mail = self.send_html_email(
                 receiver,
                 subject,
                 template,
                 context
            )
    
            return     

