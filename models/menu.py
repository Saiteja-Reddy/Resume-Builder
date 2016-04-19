# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Resume Builder'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href=URL('default','index'),
                  _id="web2py-logo")
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

response.menu = [
     (T('Search'), False, URL('default','findresume'),[])
]

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
        (T('My Resume'), False, URL('default','myresume'),[]),
        (T('Marked'), False, URL('default','markedresume'),[]),
        (T('All Resume'), False, URL('default','allresume'),[]),
        (T('My Profile'), False, URL('default','seeprofile'),[])
        ]
    
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
