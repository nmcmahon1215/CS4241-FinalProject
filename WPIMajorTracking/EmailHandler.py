import BaseHandler
import logging

from google.appengine.api import mail

class EmailHandler(BaseHandler.BaseHandler):
	def post(self, *args, **kwargs):
		advisor_name = self.request.get('advisor_name')
		advisor_email_address = self.request.get('advisor_email').lower()
		user_name = self.request.get('user_name')
		sheet_id = self.request.get('sheet_id')

		verification_url = self.uri_for('trackingsheet', sheet_id=sheet_id, _full=True)

		receiverString = advisor_name + "<" + advisor_email_address + ">"
		email_body = user_name + """ has invited you to take a look at the tracking sheet. """ + verification_url

		message = mail.EmailMessage(sender="<WPI.MajorTracking@gmail.com>",
		                            subject="Major Tracking Sheet Edit Invitation")

		message.to = receiverString
		message.body = email_body
		message.send()
		logging.info(verification_url)