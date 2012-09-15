#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : icalPy.py
# Creation Date : 15-09-2012
# Last Modified : Sat 15 Sep 2012 05:37:46 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from icalendar import Calendar, Event
from sys import stdin, argv

def main():
    cal = Calendar.from_ical(stdin.read())
    for c in cal.walk():
        if c.name == 'VEVENT':
            print "Organizer:\t\t", c['ORGANIZER'][7:]
            print "Summary:\t\t", c['SUMMARY']
            print "Attendee(s):"
            for a in c['ATTENDEE']:
                print "\t\t\t", a[7:]
            print "From:\t\t\t", c['DTSTART'].dt
            print "To:\t\t\t", c['DTEND'].dt
            print "Where:\t\t\t", c['LOCATION']
            print "Description:\t\t", c['DESCRIPTION'].encode('latin-1', 'ignore')

if __name__=="__main__":
    main()

