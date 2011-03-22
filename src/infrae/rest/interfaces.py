# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$


from zope.publisher.interfaces.browser import IBrowserPublisher


class IRESTComponent(IBrowserPublisher):
    """A REST component
    """


class MethodNotAllowed(Exception):
    """This method is not allowed.
    """

