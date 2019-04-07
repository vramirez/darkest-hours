import datetime as dt
from pytz import timezone

def diff_time():
    tz = timezone('America/Bogota')
    ''' 
    FEBRUARY 1, 2019 / 3:35 PM '
    Time according to https://www.reuters.com/article/us-colombia-venezuela/colombias-duque-says-venezuelan-maduros-hours-are-numbered-idUSKCN1PQ5RF
    '''
    duque_time = dt.datetime(2019,2,1,15,35,0,0) 
    today = dt.datetime.now()
    elapsed = today - duque_time
    return elapsed


def pretty_time_delta(seconds):
    seconds = int(seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        return '%d dias, %d horas, %d minutos, %d segundos' % (days, hours, minutes, seconds)
    elif hours > 0:
        return '%d horas, %d minutos, %d segundos' % (hours, minutes, seconds)
    elif minutes > 0:
        return '%d minutos, %d segundos' % (minutes, seconds)
    else:
        return '%d segundos' % (seconds,)


def pretty_message(str):
    msg=f'Van {str} desde que @IvanDuque dijo que @NicolasMaduro tenía las horas contadas http://bit.ly/horasmaduro'
    return msg