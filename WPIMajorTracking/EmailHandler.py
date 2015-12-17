import BaseHandler
import logging

from google.appengine.api import mail

class EmailHandler(BaseHandler.BaseHandler):
	def post(self, *args, **kwargs):
		advisor_name = self.request.get('advisor_name')
		advisor_email_address = self.request.get('advisor_email').lower()
		user_name = self.request.get('user_name')
		sheet_id = self.request.get('sheet_id')

		sheet_url = self.request.host_url + "/api/trackingsheet/" + sheet_id

		receiverString = advisor_name + "<" + advisor_email_address + ">"
		email_body = user_name + """ has invited you to take a look at the tracking sheet. """ + sheet_url

		message = mail.EmailMessage(sender="<WPI.MajorTracking@gmail.com>",
		                            subject="Major Tracking Sheet Edit Invitation")

		message.to = receiverString
		message.body = email_body
		message.send()