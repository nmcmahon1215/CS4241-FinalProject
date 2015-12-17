import BaseHandler
import TrackingSheet

import datetime
import time

from google.appengine.ext import db

class TrackingSheetHandler(BaseHandler.BaseHandler):

    def get(self, *args, **kwargs):
        sheetId = self.request.path[19:]
        sheet = TrackingSheet.get_sheet_by_id(sheetId)

        self.render_template('majorsheet.html', { 'directory': 'secured', 'id': sheetId, 'sheet': sheet })

    def delete(self, *args, **kwargs):
        sheetId = self.request.path[19:]
        TrackingSheet.delete_sheet(sheetId)

    def post(self, *args, **kwargs):
        ts = TrackingSheet.TrackingSheet(
            email=self.user.email_address,
            name=self.request.get("sheetName"),
            date=datetime.datetime.now(),
        )

        db.put(ts)

        time.sleep(1);

        self.redirect("/secured/userHome.html")
