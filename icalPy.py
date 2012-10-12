#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : icalPy.py
# Creation Date : 15-09-2012
# Last Modified : Fri 12 Oct 2012 03:32:30 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from icalendar import Calendar, Event
from sys import stdin, argv

def safe_get_na(c, evaluated):
    try:
        a = eval(evaluated)
    except KeyError:
        a = "NA"
    return a

def main():
    cal = Calendar.from_ical(stdin.read())
    for c in cal.walk():
        if c.name == 'VEVENT':
            print "Organizer:\t\t", safe_get_na(c, "c['ORGANIZER'][7:]")
            print "Summary:\t\t", safe_get_na(c, "c['SUMMARY']")
            print "Attendee(s):"
            attend = safe_get_na(c, "c['ATTENDEE']")
            if type(attend) == list:
                for a in attend:
                    print "\t\t\t", a[7:]
            else:
                print "\t\t\t", a
            print "From:\t\t\t", safe_get_na(c, "c['DTSTART'].dt")
            print "To:\t\t\t", safe_get_na(c, "c['DTEND'].dt")
            print "Where:\t\t\t", safe_get_na(c, "c['LOCATION']")
            print "Description:\t\t", safe_get_na(c, "c['DESCRIPTION'].encode('latin-1', 'ignore')")

if __name__=="__main__":
    main()

