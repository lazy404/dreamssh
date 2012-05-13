from zope.interface import Interface


class IConfig(Interface):
    """
    A marker interface for configuration objects.

    This interface is what is used to query the global registry for
    configuration instances.
    """