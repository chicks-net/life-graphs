life-graphs
===========

graphs of health, money, and technology

PREREQUISITES
-------------

If you want to do more than view my personal graphs on the Internet you should install these
Perl modules (debian packages):

* DateTime (`libdatetime-perl`)
* LWP::Simple (`libwww-perl`)
* JSON (`libjson-perl`)
* Chart::Strip (`libchart-strip-perl`)
* Readonly (`libreadonly-perl`)
* Text::CSV (`libtext-csv-perl`)
* Statistics::Basic (`libstatistics-basic-perl`)

DATA COLLECTORS DONE
--------------------

* TECH: dnetc rc5-72
* TECH: Steam profile
* TECH: Steam game hours played
* TECH: ebay
* TECH: gmail aggregate stats
* TECH: gmail for Citibank balance

GRAPHS DONE
-----------

* ebay
* Steam
* rc5

TECH TODO
---------

* interactive Storable editor instead of ad-hoccery like `edit_storable`
* fix Steam collector bugs, reduce output

GRAPHS TODO
-----------

There are many graphs that I want to make, but these have data that is ready to graph:

* Steam: a stacked chart of hours per game

DATA COLLECTORS TODO
--------------------

There are many data collectors that I want to make, but these are the top priorities:

* TECH: dnetc ogr summary and history
* TECH: github LoC committed
* TECH: fini inbox size
* FINANCE: Citi balances (partially satisfied by gmail collector)
* FINANCE: Fidelity balances
* FINANCE: OpenSRS balance
* FINANCE: paypal balances
* FINANCE: mobile balance, minutes used, bytes used
* HEALTH: fitbit autosync
* HEALTH: pull ups
* HEALTH: sit ups
* HEALTH: push ups

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
* thanks to Aleks Jakulin whose article [Assistance in picking colors and charts](http://andrewgelman.com/2007/11/22/assistance_in_p/) for helping me find [ColorBrewer](http://www.personal.psu.edu/cab38/ColorBrewer/ColorBrewer.html).  This is even more awesome because Aleks wrote his article in 2007, seven years before I found it helpful!  It was neat seeing ColorBrewer get such a thorough introduction in David Kadavy's [Design &lt;for> Hackers](http://smile.amazon.com/Design-Hackers-Reverse-Engineering-Beauty/dp/1119998956/ref=sr_1_1?ie=UTF8&qid=1425264168&sr=8-1&keywords=hackers+design).
* thanks to [Kamil Páral](https://github.com/kparal) for [gkeyring](https://github.com/kparal/gkeyring) to get access to the gnome keyring from the command line.
* thanks to Valve for providing the [Steam API](http://steamcommunity.com/dev).
