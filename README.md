life-graphs
===========

graphs of health, money, and technology

PREREQUISITES
-------------

If you want to do more than view my personal graphs on the Internet you should install these Perl modules (debian packages):

* DateTime (`libdatetime-perl`)
* LWP::Simple (`libwww-perl`)
* JSON (`libjson-perl`)
* Chart::Strip (`libchart-strip-perl`)

DATA COLLECTORS DONE
--------------------

* TECH: dnetc rc5-72
* TECH: Steam profile
* TECH: Steam game hours played
* TECH: ebay

GRAPHS DONE
-----------

* ebay
* Steam
* rc5

TECH TODO
---------

* pick a display system
* write more code
* pull credentials from LastPass
* interactive storable editor instead of ad-hoccery like `edit_storable`

GRAPHS TODO
-----------

There are many graphs that I want to make, but these are data that are ready to graph:

* ogr
* rc5: add blocks per/day to existing chart.  It may need a new chart.
* Steam: a stacked chart of hours per game

DATA COLLECTORS TODO
--------------------

There are many data collectors that I want to make, but these are the top priorities:

* TECH: dnetc ogr summary and history
* FINANCE: Citi balances
* FINANCE: OpenSRS balance
* FINANCE: paypal balances
* FINANCE: mobile balance, minutes used, bytes used
* TECH: gmail inbox size
* TECH: fini inbox size
* TECH: github LoC committed
* HEALTH: miles walked
* HEALTH: pull ups

Email graphs
------------

For each of the various sources of email it would be nice to have things like:

* sent emails per hour and day
* read emails per hour and day (how do you do that with alpine?)
* unread emails
* total emails

Inspirations
------------

* Jehiah's annual reports are beautiful.  For instance: [Jehiah 13](http://jehiah.cz/one-three/)
* Of course Stephen Wolfram was a few years ahead with [The Personal Analytics of My Life](http://blog.stephenwolfram.com/2012/03/the-personal-analytics-of-my-life/).
* [The Feltron Annual Report](http://feltron.com/ar12_01.html) is a beautiful presentation of extensive data

Informative
-----------

* [10 things I learned deployed graphite](http://kevinmccarthy.org/blog/2013/07/18/10-things-i-learned-deploying-graphite/) helped me not relearn those same things.
* thanks to [graphing time based data in perl](http://www.preshweb.co.uk/2011/11/graphing-time-based-data-in-perl/) for publishing a good example of `Chart::Strip` to get me started.
