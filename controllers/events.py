# coding: utf8
# try something like
def event(): 
	if len(request.args)>0:		
		event_name = request.args(0).replace("_"," ")
		event = db(db.events.name==event_name).select()
		if len(event)>0:
			e= event.first()
			gc = gcalender(e.name,(e.description[:100]+"...") if len(e.description[:100])>98 else e.description, str(e.start_time), str(e.end_time), e.venue)
			yc = ycalender(e.name,(e.description[:100]+"...") if len(e.description[:100])>98 else e.description, str(e.start_time), str(e.end_time), e.venue)

			bookmarked = True if auth.is_logged_in() and db(db.bookmarks.user_==auth.user.id)(db.bookmarks.event_==e.id).count()>0 else False
			return dict(event=e,gc=gc,yc=yc,bookmarked=bookmarked)
		else:
			raise HTTP(404)
			pass
	else:
		redirect(URL(''))

def addbookmark():
	if auth.is_logged_in():
		eid = request.vars.eventid
		if str(request.vars.insert)=="1":
			db.bookmarks.insert(user_=auth.user.id,event_=eid)
			return dict(success=True)
		else:
			db(db.bookmarks.user_==auth.user.id)(db.bookmarks.event_==eid).delete()
			return dict(success=False)

def gcalender(eventname,eventdetails,starttime,endtime,venue):
	str1= "https://www.google.com/calendar/render?action=TEMPLATE&text="
	str2 = eventname.replace(' ','%20')
	str3 = "&dates="
	str4 = starttime.split(' ')[0].replace('-','') + "T"
	str5 = starttime.split(' ')[1].replace(':','').split('.')[0] + "Z/"
	str6 = endtime.split(' ')[0].replace('-','') + "T"
	str7 = endtime.split(' ')[1].replace(':','').split('.')[0] + "Z&details="
	str8 = eventdetails.replace(' ','%20') + "&location="
	str9 = venue.replace(' ','%20')
	str10 = "&trp=false&sprop&sprop=name:&sf=true&output=xml"
	return str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10

def ycalender(eventname,eventdetails,starttime,endtime,venue):
	str1= "http://calendar.yahoo.com/?v=60&TITLE="
	str2 = eventname
	str3 = "&DESC="
	str4 = eventdetails + "&ST="
	str5 = starttime.split(' ')[0].replace('-','') + "T"
	str6 = starttime.split(' ')[1].replace(':','').split('.')[0] + "Z&REND="
	str7 = endtime.split(' ')[0].replace('-','') + "T"
	str8 = endtime.split(' ')[1].replace(':','').split('.')[0] + "Z&in_loc="
	str9 = venue + "&in_st=fdgfhg+fdgbn&VIEW=d";
	return str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9
