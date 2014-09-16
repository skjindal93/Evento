# coding: utf8
# try something like
def index(): 
	return dict(message="hello from event.py")


def event_add():
	return dict()

def addevent():
	ename=request.post_vars.ename
	edesc=request.post_vars.edesc
	stime=request.post_vars.stime
	etime=request.post_vars.etime
	category=request.post_vars.category
	fest=request.post_vars.fest
	venue=request.post_vars.venue
	saddress=request.post_vars.saddress
	insti=request.post_vars.insti
	city=request.post_vars.city
	state=request.post_vars.state
	pcode=request.post_vars.pcode
	wlink=request.post_vars.wlink
	fee=request.post_vars.fee
	tag=request.post_vars.tag
	oname=request.post_vars.oname
	ophone=request.post_vars.ophone
	eid=request.post_vars.eid
	latest_event_id =db.events.insert(name=ename,
		description=edesc,
		image_url=URL('static','images/hacku.png'),
		start_time=datetime.now(),
		end_time=datetime.now()-timedelta(days=-4),
		venue=venue,
		street_address=saddress,
		state_=state,
		city=city,
		pincode=pcode,
		organisers=oname,
		o_phone=ophone,
		o_email=eid,
		o_website=wlink,
		fees=fee,
		institute=insti)
	
	image_form = FORM(
		INPUT(_name='image_file',_type='file')
		)
	#latest_event_id=1
	image_id = 0
	if image_form.accepts(request.vars,formname='image_form'):
		image = db.image.filee.store(image_form.vars.image_file.file, image_form.vars.image_file.filename)
		image_id = db.image.insert(filee=image,title=latest_event_id)
	#images = db().select(db.image.ALL)
	db(db.events.id==latest_event_id).update(image_url=URL(f='link', args=db(db.image.id==image_id).select().first().filee))
	redirect(URL('events','event/%s'%ename))



def download(): return response.download(request,db)
def link(): return response.download(request,db,attachment=False)
 
def image():
	
	image_form = FORM(
		INPUT(_name='image_title',_type='text'),
		INPUT(_name='image_file',_type='file')
		)
	
	if image_form.accepts(request.vars,formname='image_form'):
		
		image = db.image.filee.store(image_form.vars.image_file.file, image_form.vars.image_file.filename)
		id = db.image.insert(filee=image,title=image_form.vars.image_title)
	
	images = db().select(db.image.ALL)
	
	return dict(images=images)

