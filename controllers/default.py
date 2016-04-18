# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@auth.requires_login()
def myresume():
    f=db(db.namess.uploadedby==auth.user.id).select(db.namess.ALL);
    return dict(message=T('Your Resumes'),f=f)

@auth.requires_login()
def uploadresume():
    return locals()

@auth.requires_login()
def my_action():
    db.namess.insert(name=request.vars.name,email=request.vars.email,summary=request.vars.summ,works=request.vars.works,education=request.vars.edu,addinfo=request.vars.addinfo,skills=request.vars.works2,phone=request.vars.phone,gpa=request.vars.edu2,uploadedby=auth.user.id);
    return "Sucess"

def findresume():
    return locals()

def editresume():
   record = db.namess(request.args(0)) or redirect(URL('index'))
   form = SQLFORM(db.namess, record)
   if form.process().accepted:
       response.flash = 'form accepted'
   elif form.errors:
       response.flash = 'form has errors'
   return dict(req=request.args(0),form=form)

def deleteresume():
    res = (db.namess.id==request.args(0))
    db(res).delete()
    redirect(URL('myresume'));

#@auth.requires_login()
def allresume():
    f=db(db.namess.id>0).select(db.namess.ALL);
    return dict(message=T('All Resumes'),f=f)

#@auth.requires_login()
def moreresume():
    f=db(db.namess.id==request.args(0)).select(db.namess.ALL);
    commenta=db(db.comments.resumeid==request.args(0)).select()
    db.comments.userid.default=auth.user.id
    db.comments.resumeid.default=request.args(0)
    db.comments.userid.readable=False
    db.comments.userid.writable=False
    db.comments.resumeid.readable=False
    db.comments.resumeid.writable=False
    form = SQLFORM(db.comments)
    if form.process().accepted:
        response.flash="response recorded"
        redirect(URL('moreresume',args=request.args(0)))
    return dict(message=T('More Info'),f=f,commenta=commenta,form=form)

@auth.requires_login()
def markresume():
    check=db((db.mark.resumeid==request.args(0)) & (db.mark.userid==auth.user.id)).count()
    if check == 0:
         ret = db.mark.insert(resumeid = request.args(0) , userid=auth.user.id)
         response.flash="Marked The Resume!"
    else:
        already_liked = (db.mark.userid==auth.user.id)&(db.mark.resumeid==request.args(0))
        db(already_liked).delete()
        response.flash="UNmarked The Resume!"
    return "Sucess"

@auth.requires_login()
def markedresume():
    f=db( (db.mark.userid==auth.user.id) & (db.namess.id==db.mark.resumeid) ).select(db.namess.ALL)
    return locals()

@auth.requires_login()
def unmark():
    already_liked = (db.mark.userid==auth.user.id)&(db.mark.resumeid==request.args(0))
    db(already_liked).delete()
    redirect(URL('markedresume'));

@auth.requires_login()
def deletecomment():
    already_liked = (db.comments.id==request.args(0))
    db(already_liked).delete()
    redirect(URL('moreresume',args=request.args(1)))
    
@auth.requires_login()
def findresume():
        return locals()

def templates():
        return locals()

@auth.requires_login()
def callback():
     "an ajax callback that returns a <ul> of links to wiki pages"
     query = db.namess.name.contains(request.vars.keyword)
     query1 = db.namess.email.contains(request.vars.keyword1)
     query2 = db.namess.skills.contains(request.vars.keyword2)
     if request.vars.task == "as":
         pages = db(query & query1 & query2 ).select(orderby=db.namess.name)
     elif request.vars.task=="des":
        pages = db(query & query1 & query2 ).select(orderby=~db.namess.name)
     elif request.vars.task=="sortcg":
        pages = db(query & query1 & query2 ).select(orderby=db.namess.gpa)
     links=[]
     for p in pages:
         links += [ [ DIV( A(p.name, _href=URL('moreresume',args=p.id)),XML('&nbsp &nbsp'),DIV(p.email),DIV(p.gpa)) ] ]
     return UL(*links)

@auth.requires_login()
def seeprofile():
    dat=db(db.auth_user.id==auth.user.id).select()
    response.flash = T("My Profile")
    return dict(message=T('Viewing my Profile!'),dat=dat)

@auth.requires_login() 
def info():
    dat=db( db.auth_user.id ==  request.args(0)  ).select()
    response.flash = T("Requested Profile")
    return dict(message=T('Viewing requested Profile!'),dat=dat)
