# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$


from zope.publisher.interfaces.browser import IBrowserPublisher
from zope.location.interfaces import ILocation


class IRESTComponent(IBrowserPublisher, ILocation):
    """A REST component
    """


class MethodNotAllowed(Exception):
    """This method is not allowed.
    """

