===========
infrae.rest
===========

``infrae.rest`` provide a simple way to write REST APIs in Zope 2.

API
===

``infrae.rest`` provides mainly a base class ``REST`` which behave a
lot like a Grok view::

   from infrae.rest import REST

   class MyAction(REST):
       """My action REST API.
       """

       def POST(self, name, value):
           # Called by POST /content/++rest++myaction&name=foo?value=bar
           return 'Success'

       def GET(self):
           # Called by GET /content/++rest++myaction
           values = self.context.something()
           return self.json_response(values)


You just have to grok your package to make it available.

- You can provide: ``POST``, ``GET``, ``HEAD``, ``DELETE`` requests.

- You can use the directives ``grok.name``, ``grok.require`` and
  ``grok.context`` to configure your REST API. They work exactly like
  on a ``grok.View``.




