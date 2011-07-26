from OFS.Uninstalled import BrokenClass
from Products.Naaya.NySite import NySite

def remove_portals(parent, keep=None):
    """ remove all portals except the one named in `keep` """

    to_remove = []

    for name, obj in parent.objectItems():
        if name in keep:
            continue

        if isinstance(obj, (NySite, BrokenClass)):
            to_remove.append(name)

    for name in to_remove:
        print 'removing %r' % name
        parent._delObject(name, suppress_events=True)
