# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Resume Builder',_class="text-info"),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href=URL('default','index'))
response.title = 'Job Hunting?'
response.subtitle = 'Create an impressive resume in minutes!'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = []

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    
    response.menu += [
        	(B('New Resume'), False, URL('default','templates'),[]),
        (B('My Resumes'), False, URL('default','myresume'),[]),
        (B('Marked'), False, URL('default','markedresume'),[]),
        (B('All Resumes'), False, URL('default','allresume'),[]),
        (B('Search'), False, URL('default','findresume'),[]),
        (B('My Profile'), False, URL('default','seeprofile'),[])
        ]
    
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
