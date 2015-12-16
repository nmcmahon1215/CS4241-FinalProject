import BaseHandler
import TrackingSheet

import datetime
import time

from google.appengine.ext import db

class TrackingSheetHandler(BaseHandler.BaseHandler):

    def post(self):
        ts = TrackingSheet.TrackingSheet(
            email=self.user.email_address,
            name=self.request.get("sheetName"),
            date=datetime.datetime.now(),
        )

        db.put(ts)

        time.sleep(1);

        self.redirect("/secured/userHome.html")