def readable_time(time,new=0):
	if not time:
		return "Weird Time"
	now = datetime.now()	
	if new:
		diff=time-now
	else:
		diff=now-time
	
	if diff.days > 30:
		return "Long time"

	if diff.days > 0:
		if diff.days==1:
			return "A day"
		else:
			return str(diff.days)+" days"

	if diff.seconds < 60:
		return "Few seconds"
	
	if diff.seconds < 120:
		return "A minute"
		
	if diff.seconds < 3600:
		return str(diff.seconds/60)+" minutes"
	
	if diff.seconds < 7200:
		return "An hour"
	
	if diff.seconds < 3600 * 24:
		return str(diff.seconds/3600)+" hours"
	
	return time
