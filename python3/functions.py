import datetime as dt
from pytz import timezone

def diff_time():
    
    ''' 
    FEBRUARY 1, 2019 / 3:35 PM '
    Time according to https://www.reuters.com/article/us-colombia-venezuela/colombias-duque-says-venezuelan-maduros-hours-are-numbered-idUSKCN1PQ5RF
    '''
    tz = timezone('America/Bogota')
    duque_time = dt.datetime(2019,2,1,20,35,0,0,tz) #time in utc -5
    today = dt.datetime.now().replace(tzinfo=tz)
    elapsed = today - duque_time
    return elapsed


def pretty_time_delta(seconds):
    seconds = int(seconds)
    full_hours=seconds//3600
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    
    if days > 0:
        return '%d días, %d horas, %d minutos, %d segundos (o un total de %d horas)' % (days, hours, minutes, seconds, full_hours)
    elif hours > 0:
        return '%d horas, %d minutos, %d segundos (o un total de %d horas)' % (hours, minutes, seconds,full_hours)
    elif minutes > 0:
        return '%d minutos, %d segundos' % (minutes, seconds)
    else:
        return '%d segundos' % (seconds,)


def pretty_message(str):
    msg=f'Van {str} desde que @IvanDuque dijo que @NicolasMaduro tenía las horas contadas http://bit.ly/horasmaduro'
    return msg

def get_only_hours(delta_time):
    return int(delta_time.total_seconds()//3600)