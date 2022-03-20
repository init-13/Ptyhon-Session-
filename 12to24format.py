# Program to convert 12 hour to 24 hour time format .

'4 condition'

'''
1. 12 AM -> AM remove       12->00

2.  1-11 AM -> AM remove

3. 12 PM -> PM remove

4, 1-11 PM -> PM remove   n->n+12 (1->1+12)


time => '12:34:45 AM'  -> '00:34:45 '
'''

def convertime(time):

    if(time[-2:]=='AM' and time[:2]=="12"):
        return "00"+time[2:-2]

    elif(time[-2:]=='AM' ):
        return time[:-2]

    elif (time[:-2]=='PM' and time[:2]=='12'):
        return time[:-2]

    else:
        hour = int(time[:2])+12
        hour = str(hour)

        return hour+time[2:-2]

print("TIME IN 24 HOUR IS:",convertime('12:34:45 AM'))
