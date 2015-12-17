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

            entity.iqp_cb = []

            for i in range(3):
                condition = bool(self.request.get("iqp_cb" + str(i)))
                entity.iqp_cb.append(condition)


            entity.mqp_title = self.request.get("mqp_title")

            entity.mqp_cb = []

            for i in range(3):
                condition = bool(self.request.get("mqp_cb" + str(i)))
                entity.mqp_cb.append(condition)



            coursePrefix = ['hua', 'pe', 'ss', 'elective', 'cs', 'math', 'science']
            courseLength = [6, 4, 2, 3, 15, 7, 5]

            for i in range(len(coursePrefix)):
                courseName = coursePrefix[i]

                courseList = []
                cbList = []

                for j in range(courseLength[i]):
                    course = self.request.get(courseName + "_course" + str(j))
                    cb = bool(self.request.get(courseName + "_cb" + str(j)))
                    courseList.append(course)
                    cbList.append(cb)
                    print course
                    print courseList

                setattr(entity, courseName + "_course", courseList)
                setattr(entity, courseName + "_cb", cbList)

            entity.put()