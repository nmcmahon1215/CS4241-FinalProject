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

        sheetId= self.request.path[19:]

        if len(sheetId) == 0:
            ts = TrackingSheet.TrackingSheet(
                email=self.user.email_address,
                name=self.request.get("sheetName"),
                date=datetime.datetime.now(),
            )

            db.put(ts)

            time.sleep(1);

            self.redirect("/secured/userHome.html")

        else:

            entity = TrackingSheet.get_sheet_by_id(sheetId)

            entity.iqp_title = self.request.get("iqp_title")

            ctr = 0
            condition = self.request.get("iqp_cb" + str(ctr))

            while (condition != ""):
                entity.iqp_cb[ctr] = condition
                ctr = ctr + 1
                condition = self.request.get("iqp_cb" + str(ctr))

            entity.mqp_title = self.request.get("mqp_title")

            ctr = 0
            condition = self.request.get("mqp_cb" + str(ctr))

            while (condition != ""):
                entity.iqp_cb[ctr] = condition
                ctr = ctr + 1
                condition = self.request.get("mqp_cb" + str(ctr))


            courseList = ['hua', 'pe', 'ss', 'elective', 'cs', 'math', 'science']

            for courseName in courseList:
                ctr = 0
                course = self.request.get(courseName + "_course" + str(ctr))
                cb = self.request.get(courseName + "_cb" + str(ctr))

                while (course != "" and cb != ""):
                    setattr(entity, courseName + "_course" + str(ctr), course)
                    setattr(entity, courseName + "_cb" + str(ctr), cb)
                    ctr = ctr + 1
                    course = self.request.get(courseName + "_course" + str(ctr))
                    cb = self.request.get(courseName + "_cb" + str(ctr))
