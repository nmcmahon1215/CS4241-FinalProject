
from google.appengine.ext import db
from google.appengine.ext.db import Key

class TrackingSheet(db.Model):
    email = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    date = db.DateTimeProperty(required=True)

    iqp_title = db.StringProperty()
    iqp_cb = db.ListProperty(bool)

    mqp_title = db.StringProperty()
    mqp_cb = db.ListProperty(bool)

    hua_cb = db.ListProperty(bool)
    hua_course = db.ListProperty(str)

    pe_cb = db.ListProperty(bool)
    pe_course = db.ListProperty(str)

    ss_cb = db.ListProperty(bool)
    ss_course = db.ListProperty(str)

    elective_cb = db.ListProperty(bool)
    elective_course = db.ListProperty(str)

    cs_cb = db.ListProperty(bool)
    cs_course = db.ListProperty(str)

    math_cb = db.ListProperty(bool)
    math_course = db.ListProperty(str)

    science_cb = db.ListProperty(bool)
    science_course = db.ListProperty(str)


def get_sheets_by_email(email):
    q = db.GqlQuery("SELECT * FROM TrackingSheet WHERE email = '" + email + "' ORDER BY date DESC")

    result = []

    for item in q.run():
        result.append(item)

    return result

def get_sheet_by_id(id):
    return db.get(Key(id))

def delete_sheet(id):
    db.delete(Key(id))
