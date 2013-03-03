#!/usr/bin/python
"""usage: %prog [options] DATE1 [DATE2]

Prints out the difference between the two dates. If DATE2 is ommited then it is
substituted by today.

Date format is like "01jan2013". Accepts months abbreviations in english and portuguese.
"""
import re
from datetime import date
from optparse import OptionParser


def parse_options():
    """
    Parse command line options.

    @return: a 2-tuple, where the first object contains the options as
        attributes and the second contains the positional arguments.
    @rtype: tuple(object, object)
    """

    parser = OptionParser(usage=__doc__)
    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.error('incorrect number of arguments')

    return (options, args)

MONTHS_ABBREVIATIONS = [
    ('jan',),
    ('fev', 'feb',),
    ('mar',),
    ('abr', 'apr',),
    ('mai', 'may',),
    ('jun',),
    ('jul',),
    ('ago',),
    ('set', 'sep',),
    ('out', 'oct',),
    ('nov',),
    ('dez', 'dec',),
]

MONTH_TO_NUMBER = dict(
    (a, i + 1)
    for (i, abbrs) in enumerate(MONTHS_ABBREVIATIONS)
    for a in abbrs
)

DATE_REGEX = r'(\d\d?)([a-z][a-z][a-z])(\d\d\d\d)'


def str_to_date(s):
    match = re.findall(DATE_REGEX, s, re.IGNORECASE)[0]
    day = int(match[0])
    month = MONTH_TO_NUMBER[match[1].lower()]
    year = int(match[2])

    return date(year, month, day)


def main():
    options, args = parse_options()

    date1 = str_to_date(args[0])
    if len(args) >= 2:
        date2 = str_to_date(args[1])
    else:
        date2 = date.today()

    print (date1 - date2).days

if __name__ == '__main__':
    main()
