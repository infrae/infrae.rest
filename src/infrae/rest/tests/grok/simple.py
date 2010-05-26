"""

  Let's first grok our test first:

   >>> grok('infrae.rest.tests.grok.simple')

  Now, if we have a folder we can use our REST component:

    >>> root = getRootFolder()
    >>> root.manage_addProduct['OFS'].manage_addFolder('folder', 'Folder')
    >>> print http('GET /folder/++rest++testsimple HTTP/1.0')
    HTTP/1.0 200 OK
    Content-Length: 7
    Content-Type: plain/text
    <BLANKLINE>
    Nothing

  However we don't have PUT, POST, DELETE, HEAD actions:

    >>> print http('PUT /folder/++rest++testsimple HTTP/1.0')
    Traceback (most recent call last):
       ...
    MethodNotAllowed: PUT

    >>> print http('POST /folder/++rest++testsimple HTTP/1.0')
    Traceback (most recent call last):
       ...
    MethodNotAllowed: POST

    >>> print http('DELETE /folder/++rest++testsimple HTTP/1.0')
    Traceback (most recent call last):
       ...
    MethodNotAllowed: DELETE

    >>> print http('DELETE /folder/++rest++testsimple HTTP/1.0')
    Traceback (most recent call last):
       ...
    MethodNotAllowed: DELETE

    >>> print http('HEAD /folder/++rest++testsimple HTTP/1.0')
    Traceback (most recent call last):
       ...
    MethodNotAllowed: HEAD


"""

from OFS.Folder import Folder
from five import grok
from infrae.rest import REST


class TestSimple(REST):
    grok.context(Folder)

    def GET(self):
        self.response.setHeader('Content-Type', 'plain/text')
        return "Nothing"
