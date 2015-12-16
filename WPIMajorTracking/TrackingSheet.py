
from google.appengine.ext import db

class TrackingSheet(db.Model):
    email = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    date = db.DateTimeProperty(required=True)

def get_sheets_by_email(email):
    q = db.GqlQuery("SELECT * FROM TrackingSheet WHERE email = '" + email + "' ORDER BY date DESC")

    result = []

    for item in q.run():
        result.append(item)

    return result