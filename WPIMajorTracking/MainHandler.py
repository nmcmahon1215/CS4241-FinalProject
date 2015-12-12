
import BaseHandler

class MainHandler(BaseHandler.BaseHandler):
  def get(self, *args, **kwargs):
    filePath = self.request.path[8:]

    if self.user is not None:
        self.redirect("/secured")

    if filePath == "":
        filePath = "home.html"

    self.render_template(filePath)