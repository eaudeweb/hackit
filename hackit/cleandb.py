from time import time
import logging
from OFS.Uninstalled import BrokenClass

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

"""
>>> from hackit import cleandb
>>> import transaction
>>> cleandb.remove_portals(app, keep=['chm_nl'])
>>> transaction.commit()
>>> cleandb.pack(cleandb.get_db(app))
"""

def remove_portals(parent, keep=None):
    """
    Remove all portals in `parent`. `keep` is a list of portal IDs that should
    not be removed.
    """

    from Products.Naaya.NySite import NySite

    to_remove = []

    for name, obj in parent.objectItems():
        if name in keep:
            continue

        if isinstance(obj, (NySite, BrokenClass)):
            to_remove.append(name)

    for name in to_remove:
        log.info('removing %r', name)
        parent._delObject(name, suppress_events=True)

def make_cookie_crumbler(ob):
    """ create a cookie crumbler in `ob` (typically the application root) """
    from Products.CookieCrumbler.CookieCrumbler import manage_addCC
    manage_addCC(ob, 'login', create_forms=True)
    log.info("created %r", ob['login'])

def get_db(ob):
    return ob._p_jar._db

def pack(db):
    t0 = time()
    db.pack()
    log.info("packed in %.2f seconds", time() - t0)

def auto(app, keep=None):
    """
    Shorthand for::

        remove_portals(app, keep)
        import transaction; transaction.commit()
        pack(get_db(app))
    """
