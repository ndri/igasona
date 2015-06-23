# igasona
Estonian version of the [@everyword](https://twitter.com/everyword) Twitter bot. It tweets every word from [ÕS 2013](http://www.eki.ee/dict/qs/).

It uses the [python-twitter](https://github.com/bear/python-twitter) Python API.

I have a cronjob that runs igasona.py every 30 minutes. So far it has run for about a year without any problems, except you cannot tweet "d" or "D", because they're commands for a direct message.

The words were scraped using [this](http://www.eki.ee/dict/xp/index.cgi?dictid=eos) and a wildcard. I apologise to whomever hosts that.
