
from google.appengine.ext import db

class TrackingSheet(db.Model):
    email = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    date = db.DateProperty(required=True)

def get_sheets_by_email(email):
    q = db.GqlQuery("SELECT * FROM TrackingSheet WHERE email = '" + email + "'")

    return q.run()