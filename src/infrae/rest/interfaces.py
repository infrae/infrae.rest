# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.publisher.interfaces.http import IHTTPRequest


class IRESTLayer(IHTTPRequest):
    """To this layer are registered the REST components.
    """


class MethodNotAllowed(Exception):
    """This method is not allowed.
    """

