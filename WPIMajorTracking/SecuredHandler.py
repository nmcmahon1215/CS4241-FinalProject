import BaseHandler
import WPIMajorTracking
import TrackingSheet

from google.appengine.ext import db

class SecuredHandler(BaseHandler.BaseHandler):
  @BaseHandler.user_required
  def get(self, *args, **kwargs):
    filePath = self.request.path[9:]
    if filePath == "":
        filePath = "userHome.html"

    params = { 'directory': 'secured' }

    if filePath == "userHome.html":
        params['sheets'] = TrackingSheet.get_sheets_by_email(self.user.email_address)

    self.render_template(filePath, params )