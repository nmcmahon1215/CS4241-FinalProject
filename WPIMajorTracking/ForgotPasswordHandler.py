import BaseHandler

class ForgotPasswordHandler(BaseHandler.BaseHandler):
  def get(self):
    self._serve_page()

  def post(self):
    email_address = self.request.get('email_address').lower()

    user = self.user_model.get_by_auth_id(email_address)
    if not user:
      logging.info('Could not find any user entry for email address %s', email_address)
      self._serve_page(not_found=True)
      return

    user_id = user.get_id()
    token = self.user_model.create_signup_token(user_id)

    verification_url = self.uri_for('verification', type='p', user_id=user_id,
      signup_token=token, _full=True)

    receiverString = user.name + " " + user.last_name + "<" + user.email_address + ">";
    email_body = """Hello user,\n\nPlease reset your password by going to: """ + verification_url;

    message = mail.EmailMessage(sender="<WPI.MajorTracking@gmail.com>",
                                subject="Reset Password")

    message.to = receiverString
    message.body = email_body
    message.send()

    self._serve_page(email_sent=True, verification_url=verification_url)

  def _serve_page(self, not_found=False, email_sent=False, verification_url=''):
    email_address = self.request.get('email_address')
    params = {
      'email_address': email_address,
      'not_found': not_found,
      'email_sent': email_sent,
      'verification_url': verification_url
    }
    self.render_template('forgot.html', params)