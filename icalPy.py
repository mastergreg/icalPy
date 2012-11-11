#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : icalPy.py
# Creation Date : 15-09-2012
# Last Modified : Sun 11 Nov 2012 12:29:24 PM EET
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from icalendar import Calendar, Event
from sys import stdin, stderr, argv
from string import maketrans, translate

def safe_get_na(c, evaluated):
    try:
        a = eval(evaluated)
    except KeyError:
        a = u"NA"
    return a

def main():
    text = stdin.read().decode('utf-8')
    text = text.encode('utf-8')
    cal = Calendar.from_ical(text)
    for c in cal.walk():
        if c.name == 'VEVENT':
            print u"Organizer:\t\t", safe_get_na(c, u"c['ORGANIZER'][7:]")
            print u"Summary:\t\t", safe_get_na(c, u"c['SUMMARY']").encode('utf-8')
            print u"Attendee(s):"
            attend = safe_get_na(c, u"c['ATTENDEE']")
            if type(attend) == list:
                for a in attend:
                    print u"\t\t\t", a[7:]
            else:
                print u"\t\t\t", attend
            print u"From:\t\t\t", safe_get_na(c, u"c['DTSTART'].dt")
            print u"To:\t\t\t", safe_get_na(c, u"c['DTEND'].dt")
            print u"Where:\t\t\t", safe_get_na(c, u"c['LOCATION']")
            print u"Description:\t\t", safe_get_na(c, u"c['DESCRIPTION'].encode('latin-1', 'ignore')")

if __name__=="__main__":
    main()

