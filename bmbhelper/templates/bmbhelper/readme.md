## About This App

## How it works

This application scrapes a Bandcamp album page & outputs scraped data in a MusicBrainz friendly format. 
Why ?

About this project

* uses unitesting
* uses coverage for testing
* uses mock for faking scraped html
* uses dataclasses introduced in 3.7
* usage of Type annotations
* custom __str__ method [implementation][2] | __str__ > __repr__
* custrom __getitem__ implementation
* file load hack for unit tests:  create a python variable.
* shows how to ovveride a python FormObject.is_valid() method
* shows rome regex magic
* implements custom dict class
* added custom css to django form widget



[1]: https://archive.fo/4GpAc "django testing 101"
[2]: https://pythonprogramming.net/__str__-__repr__-intermediate-python-tutorial/
[3]: https://chriskief.com/2012/12/16/override-django-form-is_valid/
[4]: https://github.com/konradhalas/dacite
[4.1]: https://stackoverflow.com/questions/53376099/python-dataclass-from-dict
[5]: https://stackoverflow.com/questions/35282222/in-python-how-do-i-cast-a-class-object-to-a-dict
[6]: https://andrearobertson.com/2017/06/17/django-example-creating-a-custom-form-field-widget/ "render widghet"
[7]: https://github.com/django/django/tree/master/django/forms/templates/django/forms/widgets
