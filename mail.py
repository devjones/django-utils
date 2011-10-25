from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.core.validators import email_re
from django.http import HttpResponseRedirect, HttpResponse,Http404, HttpRequest


def validate_email(email):
    return True if email_re.match(email) else False

class Email(object):
    def __init__(self, *args, **kwargs):
        self.from_email = None
        self.to = [] #To should be a list.  Make sure single emails are put in a list before sending
        self.subject = None
        self.text_content = None
        self.html_content = None

        for key in kwargs:
            self.__data__[key] = kwargs.get(key,None)

    def send(self):
        #Validate Email object before sending
        if not self.validate():
            raise

        try:
            msg = EmailMultiAlternatives(self.subject, self.text_content, self.from_email, self.to)

            if self.html_content:
                msg.attach_alternative(self.html_content, 'text/html')
            msg.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return HttpResponse('Your email has been successfully sent')

    def validate(self):
        #Consider validating before attribute saved also
        if validate_email(self.from_email):
            return True

        return False



