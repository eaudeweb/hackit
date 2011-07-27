from time import time
from OFS.Uninstalled import BrokenClass
from Products.Naaya.NySite import NySite

"""
>>> from hackit import cleandb
>>> import transaction
>>> cleandb.remove_portals(app, keep=['chm_nl'])
>>> transaction.commit()
>>> cleandb.pack(cleandb.get_db(app))
"""

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

def get_db(ob):
    return ob._p_jar._db

def pack(db):
    t0 = time()
    db.pack()
    print "packed in %.2f seconds" % (time()-t0,)
