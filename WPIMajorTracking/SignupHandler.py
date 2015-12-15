import BaseHandler

import os

from google.appengine.api import mail

class SignupHandler(BaseHandler.BaseHandler):
  def get(self):
    self._serve_page()

  def post(self):
    email = self.request.get('email_address').lower()
    name = self.request.get('name')
    password = self.request.get('password')
    last_name = self.request.get('lastname')
    major = self.request.get_all('major')
    resendEmail = self.request.get('resendEmail')
    resendVerification = self.request.get('resendVerification')

    if not resendEmail:
      unique_properties = None
      user_data = self.user_model.create_user(email,
        unique_properties,
        email_address=email, name=name, password_raw=password,
        last_name=last_name, major=major[0], verified=False)

      if not user_data[0]: #user_data is a tuple
        self._serve_page(duplicate=True, duplicateKeys=user_data[1])
        return

      user = user_data[1]
      user_id = user.get_id()

      token = self.user_model.create_signup_token(user_id)

      verification_url = self.uri_for('verification', type='v', user_id=user_id,
        signup_token=token, _full=True)

    if resendVerification:
      verification_url = resendVerification

    receiverString = name + " " + last_name + "<" + email + ">";
    email_body = """Hello new user,\n\nPlease verify your account by going to this link: """ + verification_url;

    message = mail.EmailMessage(sender="<WPI.MajorTracking@gmail.com>",
                                subject="Account Verification")
    message.to = receiverString
    message.body = email_body
    message.send()

    self._serve_page(email_sent=True, verification_url=verification_url, resendEmail=resendEmail)

  def _serve_page(self, email_sent=False, verification_url='', duplicate=False, duplicateKeys='', resendEmail=''):
    email_address = self.request.get('email_address')
    params = {
      'development_mode': os.environ['SERVER_SOFTWARE'].startswith('Development'),
      'email_address': email_address,
      'email_sent': email_sent,
      'verification_url': verification_url,
      'duplicate': duplicate,
      'duplicateKeys': duplicateKeys,
      'resendEmail': resendEmail
    }
    self.render_template('signup.html', params)