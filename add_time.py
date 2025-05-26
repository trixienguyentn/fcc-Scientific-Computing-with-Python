def add_time(start, duration, *args):
    week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    # Split the start time into the hours, mins and format
    hours, mins_and_format = start.split(':')
    mins, format = mins_and_format.split(' ')

    # Change to 24 hours format for parsing
    hours = int(hours)
    if format == 'PM':
        hours = hours + 12

    # Split the duration
    addHours, addMins = duration.split(':')
    # Start to parse the return string properly
    newMin = int(mins) + int(addMins)
    remainingMins = newMin % 60
    overflowHours = int((newMin - remainingMins) / 60)

    newHour = hours + int(addHours) + overflowHours
    remainingHours = newHour % 24
    daysPassed = int((newHour - remainingHours) / 24)

    # Revert back to AM / PM and format the numbers
    sign = 'AM'
    if remainingHours >= 12:
        sign = 'PM'
        remainingHours -= 12
    if remainingHours == 0:
        remainingHours += 12
    remainingHours = str(remainingHours)
    remainingMins = str(remainingMins)
    if len(remainingMins) == 1:
        remainingMins = '0{}'.format(remainingMins)

    # Set up the basic return string of HH:MM {AM/PM}
    returnStr = '{}:{} {}'.format(remainingHours, remainingMins, sign)

    # Add the day info if required
    if len(args) != 0:
        startDay = args[0].capitalize()
        if startDay in week:
            index = week.index(startDay)
            newDay = index + daysPassed
            newDay = newDay % 7
            returnStr += ', {}'.format(week[newDay])
        else:
            return 'Error: Name of day is not clear.'

    # Add the next x days info if daysPassed > 0
    if daysPassed > 0:
        if daysPassed == 1:
            returnStr += ' (next day)'
        else:
            returnStr += ' ({} days later)'.format(daysPassed)

    return returnStr

# Test cases:
print(f'1. {add_time("3:30 PM", "2:12")}')
print(f'2. {add_time('11:55 AM', '3:12')}')
print(f'3. {add_time('2:59 AM', '24:00')}')
print(f'4. {add_time('11:59 PM', '24:05')}')
print(f'5. {add_time('8:16 PM', '466:02')}')
print(f'6. {add_time('3:30 PM', '2:12', 'Monday')}')
print(f'7. {add_time('2:59 AM', '24:00', 'Saturday')}')
print(f'8. {add_time('11:59 PM', '24:05', 'Wednesday')}')
print(f'9. {add_time('8:16 PM', '466:02', 'tuesday')}')


