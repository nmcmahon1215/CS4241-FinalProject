#Skeleton from https://github.com/abahgat/webapp2-user-accounts
#!/usr/bin/env python

import BaseHandler
import MainHandler
import SignupHandler
import ForgotPasswordHandler
import VerificationHandler
import SetPasswordHandler
import SecuredHandler
import JSHandler
import LoginHandler
import LogoutHandler

import logging
import os.path
import webapp2
import jinja2

from webapp2_extras import auth
from webapp2_extras import sessions

from webapp2_extras.auth import InvalidAuthIdError
from webapp2_extras.auth import InvalidPasswordError

from google.appengine.ext import ndb
from google.appengine.api import mail

config = {
  'webapp2_extras.auth': {
    'user_model': 'models.User',
    'user_attributes': ['name']
  },
  'webapp2_extras.sessions': {
    'secret_key': 'YOUR_SECRET_KEY'
  }
}

app = webapp2.WSGIApplication([
    webapp2.Route('/', webapp2.RedirectHandler, defaults={'_uri': '/public'}, name='home'),
    webapp2.Route(r'/public<:.*>', MainHandler.MainHandler),
    webapp2.Route('/api/signup', SignupHandler.SignupHandler),
    webapp2.Route('/api/<type:v|p>/<user_id:\d+>-<signup_token:.+>',
      handler=VerificationHandler.VerificationHandler, name='verification'),
    webapp2.Route('/api/password', SetPasswordHandler.SetPasswordHandler),
    webapp2.Route('/api/login', LoginHandler.LoginHandler, name='login'),
    webapp2.Route('/api/forgot', ForgotPasswordHandler.ForgotPasswordHandler, name='forgot'),
    webapp2.Route('/api/logout', LogoutHandler.LogoutHandler, name='logout'),
    webapp2.Route(r'/secured<:.*>', SecuredHandler.SecuredHandler, name='secured'),
    webapp2.Route('/js', JSHandler.JSHandler, name='javascript')
], debug=True, config=config)

logging.getLogger().setLevel(logging.DEBUG)
