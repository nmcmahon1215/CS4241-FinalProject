import BaseHandler
import WPIMajorTracking

class SecuredHandler(BaseHandler.BaseHandler):
  @BaseHandler.user_required
  def get(self, *args, **kwargs):
    filePath = self.request.path[9:]
    if filePath == "":
        filePath = "userHome.html"

    self.render_template(filePath, { 'directory': 'secured' })