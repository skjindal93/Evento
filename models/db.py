# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from random import choice
#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

db.define_table('events',
    Field('name','string'),
    Field('description','string'),
    Field('image_url','string'),
    Field('start_time','datetime',default=datetime.now),
    Field('end_time','datetime'),
    Field('venue','string'),
    Field('street_address','string'),
    Field('institute','string'),
    Field('state_','string'),
    Field('city','string'),
    Field('pincode','string'),
    Field('organisers','string'),
    Field('o_phone','string'),
    Field('o_email','string'),
    Field('o_website','string'),
    Field('fees','integer'),
    Field('buzz','double'),
    fake_migrate=True)

# db.events.insert(name="Hack U",description="""The festival of unrestrained innovation, learning, coding, camaraderie, demos, awards, fun & food is back! After successful HackUs in 2012, it's time for all you coders to team up and emerge with cool, interesting hacks. So register now. Click here to register.""", image_url=URL('static','images/hacku.png'),start_time=datetime.now(),end_time=datetime.now()-timedelta(days=-4),venue="Seminar Hall",street_address="IIT Delhi, Hauz Khas",state_="New Delhi",city="New Delhi",pincode="110016",organisers="Yahoo",o_phone="8800576534",o_email="hackuindia@yahoo.com",o_website="in.hacku.yahoo.com",fees=0, institute="IIT Delhi", buzz=4.9)

# db.events.insert(name="Hackthon",description="""A hackathon (also known as a hack day, hackfest or codefest) is an event in which computer programmers and others involved in software development, including graphic designers, interface designers and project managers, collaborate intensively on software projects.[1] Occasionally, there is a hardware component as well. Hackathons typically last between a day and a week in length. Some hackathons are intended simply for educational or social purposes, although in many cases the goal is to create usable software. Hackathons tend to have a specific focus, which can include the programming language used, the operating system, an application, an API, the subject and the demographic group of the programmers. In other cases, there is no restriction on the type of software being created.""", image_url=URL('static','images/hackathon.png'),start_time=datetime.now(),end_time=datetime.now()-timedelta(days=-4),venue="Dogra Hall",street_address="IIT Delhi, Hauz Khas",state_="New Delhi",city="New Delhi",pincode="110016",organisers="Microsoft",o_phone="8800576534",o_email="hackthon@microsoft.com",o_website="hackthon.microsoft.com",fees=1000, institute="IIT Delhi", buzz=4.1)

# db.events.insert(name="Indian Open",description="""The India Open is an annual tennis event that has been held in India since 1981. In 2011, the tournament was lifted as part of the BWF Super Series tournament, after four years as part of Grand Prix Gold tournament. In 2013, the event is being organised at Siri Fort Indoor Badminton Complex, New Delhi from April 23 to 28 and is called Yonex Sunrise Indian Open 2013. The prize money is over USD 200,000""", image_url=URL('static','images/indian_open.png'),start_time=datetime.now(),end_time=datetime.now()-timedelta(days=-4),venue="R K Khanna Tennis Stadium",street_address="Africa avenue, Ram krishna puram",state_="New Delhi",city="New Delhi",pincode="110094",organisers="Indian Tennis federation",o_phone="8800576534",o_email="indianopen@itf.com",o_website="indianopen.itf.com",fees=1500, institute="Indian Govt.", buzz=2.0)

# db.events.insert(name="Indo-french fashion festival",description="""France–India relations have traditionally been close and friendly. With the establishment of the strategic partnership in 1998, there has been a significant progress in all areas of bilateral cooperation through regular high-level exchanges at the Head of State/Head of Government levels and growing commercial exchanges including in strategic areas such as defence, nuclear energy and space. France was the first country with which India entered into an agreement on nuclear energy following the waiver given by International Atomic Energy Agency and the Nuclear Suppliers’ Group enabling India to resume full civil nuclear cooperation with the international community. There is also a growing and wide-ranging cooperation in areas such as trade and investment, culture, science & technology and education.France has consistently supported India’s permanent membership of the UNSC.""", image_url=URL('static','images/indofrench.png'),start_time=datetime.now(),end_time=datetime.now()-timedelta(days=-4),venue="Gopal Banquet Hall",street_address="Green Park",state_="New Delhi",city="New Delhi",pincode="110062",organisers="DLF",o_phone="8800576534",o_email="indofrench@gmail.com",o_website="infofrenchcooking.com",fees=0, institute="Delhi University, Gargi college", buzz=4.0)

# db.events.insert(name="Counter Strike Event",description="""Counter-Strike is a tactical first-person shooter video game developed by Valve Corporation which originated from a Half-Life modification by Minh "Gooseman" Le and Jess "Cliffe" Cliffe. By the fourth beta version, Valve Software, the developer who created Half-Life, began assisting in the development of Counter-Strike.[1] In 2000, Valve bought the rights to Counter-Strike, and would publish the title for Microsoft Windows that year, and later in 2003 for the Xbox. OS X and Linux ports were available in January 2013.""", image_url=URL('static','images/counterstrike.png'),start_time=datetime.now(),end_time=datetime.now()-timedelta(days=-4),venue="Exibition Hall",street_address="Delhi Technical University",state_="New Delhi",city="New Delhi",pincode="110062",organisers="NSD Gamers",o_phone="8800576534",o_email="counterstrike@gmail.com",o_website="langamecs.com",fees=0, institute="Delhi Technical University", buzz=5.0)

db.define_table('bookmarks',
    Field('user_',db.auth_user),
    Field('event_',db.events),
    migrate=True)

db.define_table('notifications',
    Field('user_',db.auth_user),
    Field('description','string'),
    Field('time_','datetime',default=datetime.now),
    migrate=True)

db.define_table('reviews',
    Field('event_',db.events),
    Field('user_',db.auth_user),
    Field('rating','double'),
    Field('description','string'),
    Field('time_','datetime'),
    migrate=True)

db.define_table('image',
    Field('title'),
    Field('filee', 'upload'),
    format = '%(title)s')


db.define_table('tags',
    Field('event_',db.events),
    Field('tags','string'),
    migrate=True)


db.define_table('buzzz',
    Field('eventid', 'integer'),
    Field('d3GlHits', 'integer'),
    Field('d3_7dGlHits', 'integer'),
    Field('remGlHits', 'integer'),
    Field('GlAttend', 'integer'),
    Field('GlNattend', 'integer'),
    Field('FrAttend', 'integer'),
    Field('FrNattend', 'integer'),
    Field('distance', 'integer'),
    Field('category', 'integer'),
    migrate=True)


#db.buzzz.insert(eventid="1", d3GlHits="1000", d3_7dGlHits="800", remGlHits="400", GlAttend="1000", GlNattend="700", FrAttend="50", FrNattend="20", distance="10", category="1")

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
