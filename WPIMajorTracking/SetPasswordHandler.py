import BaseHandler
import WPIMajorTracking

class SetPasswordHandler(BaseHandler.BaseHandler):

  @BaseHandler.user_required
  def post(self):
    password = self.request.get('password')
    old_token = self.request.get('t')

    if not password or password != self.request.get('confirm_password'):
      self._serve_page(True)
      return

    user = self.user
    user.set_password(password)
    user.put()

    # remove signup token, we don't want users to come back with an old link
    self.user_model.delete_signup_token(user.get_id(), old_token)

    self._serve_page(updated_password=True)

  def _serve_page(self, mismatch=False, updated_password=False):
    email_address = self.request.get('email_address')
    params = {
      'email_address': email_address,
      'mismatch': mismatch,
      'updated_password': updated_password
    }
    self.render_template('resetpassword.html', params)