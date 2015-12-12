import BaseHandler

class LogoutHandler(BaseHandler.BaseHandler):
  def get(self):
    self.auth.unset_session()
    self.redirect(self.uri_for('home'))