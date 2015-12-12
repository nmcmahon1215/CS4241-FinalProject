import BaseHandler

class LoginHandler(BaseHandler.BaseHandler):
  def get(self):
    self._serve_page()

  def post(self):
    email_address = self.request.get('email_address').lower()
    password = self.request.get('password')
    try:
      u = self.auth.get_user_by_password(email_address, password, remember=True,
        save_session=True)
      self.redirect(self.uri_for('home'))
    except (InvalidAuthIdError, InvalidPasswordError) as e:
      logging.info('Login failed for user %s because of %s', email_address, type(e))
      self._serve_page(True)

  def _serve_page(self, failed=False):
    email_address = self.request.get('email_address')
    params = {
      'email_address': email_address,
      'failed': failed
    }
    self.render_template('home.html', params)