# About This Django App

[👉 Click For Hosted Version][bc2mbhosted]

## How it works

![Bandcamp 2 MusicBrainz helper](./bc2mb.gif)

This application scrapes a Bandcamp album page & outputs scraped data in a MusicBrainz friendly format.
In the future I will try to implement an automatic post to MusicBrainz assuming their API allows it.

## About BandCamp Scraper

This project has a clean and reusable scraper module, check it out at `bmbhelper.utils.bandcamp_parser.py`
Tests for this module are found under `tests.test_utils.py`

## Nerdy part of the project

* uses `unittest'ing`
* uses coverage for testing
* uses mock for faking scraped html
* usages of type annotations
* custom `__str__` method [implementation][2] | `__str__ > __repr__`
* custom `__getitem__` implementation
* file load hack for unit tests:  create a python variable.
* shows how to override a python `FormObject.is_valid()` method
* shows that I know how write regexes
* implements custom dict class
* added custom css to django form widget
* is completely dockerized for production and development
* has automatic builds as soon as source is pushed to github master branch
* uses `decouple` package for storing of secrets
* uses `settings_prod.py` for simple config value overrides

[1]: https://archive.fo/4GpAc "django testing 101"
[2]: https://pythonprogramming.net/__str__-__repr__-intermediate-python-tutorial/
[3]: https://chriskief.com/2012/12/16/override-django-form-is_valid/
[4]: https://github.com/konradhalas/dacite
[4.1]: https://stackoverflow.com/questions/53376099/python-dataclass-from-dict
[5]: https://stackoverflow.com/questions/35282222/in-python-how-do-i-cast-a-class-object-to-a-dict
[6]: https://andrearobertson.com/2017/06/17/django-example-creating-a-custom-form-field-widget/ "render widget"
[7]: https://github.com/django/django/tree/master/django/forms/templates/django/forms/widgets
[8]: https://stackoverflow.com/questions/11047621/is-it-safe-to-use-os-environ-setdefault
[9]: https://stackoverflow.com/questions/43570838/how-do-you-use-python-decouple-to-load-a-env-file-outside-the-expected-paths
[10]: https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html
[11]: https://medium.com/machine-learning-world/deploying-on-aws-free-tire-with-docker-and-fabric-d9eca7c629e6
[bc2mbhosted]: https://me.dovydas.xyz/bc2mb