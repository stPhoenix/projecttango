# Project T.A.N.G.O. (game news)
## http://game-news.tk (https://projecttango.herokuapp.com/)
[![Build Status](https://travis-ci.org/stPhoenix/projecttango.svg?branch=master)](https://travis-ci.org/stPhoenix/projecttango)

### Hi
To begin with django, we decided to make simple web site of game news. It's apps are:
 * news( articles, categories, tags);
 * account( user profile with avatar);
 * ads (right now is disabled);
 * comments (commenting articles);
 * journalist (our 'worker' to 'write' news);
 * forum (currently under development);

Also, we practise with bootstrap 4 but without js.

For hoster we choose [heroku](http://heroku.com/) as it's a great hosting which has all our demands.
To practise with CLI(heroku supports) and CI we choose [travis](https://travis-ci.org/) and **it's work wonderful**!

As you have already understand - it's **standalone** website, so we doesn't made it as django app with setup.py.

### Actual libs and versions used in project you can find in *Pipfile* and *Pipfile.lock*

As for now, we still have to do:
* docs;
* ssl(heroku provide paid ssl support, so we need to find free alternative realization);
* forum(it's also works as standalone so we try to modify it to our needs);
* maybe html/css tests;
* better site design;

### If you have something to say - write to *saintdevs@gmail.com*
