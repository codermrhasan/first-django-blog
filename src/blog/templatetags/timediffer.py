from django import template
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

register = template.Library()

@register.filter
def timediffer(now, posttime):
    posttime = posttime.replace(tzinfo=None)
    timedif= now -posttime
    timestr=""
    if timedif.days >= 365:
        gettime = (int)(timedif.days/365)
        if gettime==1:
            timestr = f"about {gettime} year ago"
        else:
            timestr = f"about {gettime} years ago"

    elif timedif.days >= 30 and timedif.days < 365:
        gettime = (int)(timedif.days/30)
        if gettime==1:
            timestr= f"about {gettime} month ago"
        else: 
            timestr= f"about {gettime} months ago"
            
    elif timedif.days>=7 and timedif.days < 30:
        gettime = (int)(timedif.days/7)
        if gettime==1:
            timestr=f"about {gettime} week ago"
        else:
            timestr=f"about {gettime} weeks ago"
            
    elif timedif.days>=1 and timedif.days < 7:
        gettime = (int)(timedif.days)
        if gettime==1:
            timestr=f"about {gettime} day ago"
        else:
            timestr=f"about {gettime} days ago"

    elif timedif.seconds>=3600 and timedif.days < 1:
        gettime = (int)(timedif.seconds/3600)
        if gettime==1:
            timestr=f"about {gettime} hour ago"
        else: 
            timestr=f"about {gettime} hours ago"
    
    elif timedif.seconds>=60 and timedif.seconds < 3600:
        gettime = (int)(timedif.seconds/60)
        if gettime==1:
            timestr = f"about {gettime} minute ago"
        else:
            timestr = f"about {gettime} minutes ago"
        
    elif timedif.seconds>=1 and timedif.seconds < 60:
        gettime = (int)(timedif.seconds)
        if gettime==1:
            timestr = f"about {gettime} second ago"
        else:
            timestr = f"about {gettime} seconds ago"

    else:
        timestr='now'

    return timestr