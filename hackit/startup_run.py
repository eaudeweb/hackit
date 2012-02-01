def run_user_script():
    try:
        from App.config import getConfiguration
    except ImportError:
        return
    run_path = getConfiguration().environment.get('HACKIT_RUN', '')
    if not run_path:
        return
    execfile(run_path)


def run_once():
    print 'HACKIT'
    run_user_script()
