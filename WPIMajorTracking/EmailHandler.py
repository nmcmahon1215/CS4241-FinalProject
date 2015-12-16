import BaseHandler
import logging

from google.appengine.api import mail

class EmailHandler(BaseHandler.BaseHandler):

  def post(self):
    advisor_email_address = self.request.get('advisor_email').lower()

    receiverString = "<" + advisor_email_address + ">";
    email_body = user.name + """ has invited you to take a look at the tracking sheet. """ # + link

    message = mail.EmailMessage(sender="<WPI.MajorTracking@gmail.com>",
                                subject="Major Tracking Sheet Edit Invitation")

    message.to = receiverString
    message.body = email_body
    message.send()