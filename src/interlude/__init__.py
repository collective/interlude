#
# Copyright 2006-2009, BlueDynamics Alliance, Austria - http://bluedynamics.com
#
# GNU Lesser General Public Licence

__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plaintext'

import code
import sys

try:
    import IPython
    HAS_IPYTHON = True
except ImportError:
    HAS_IPYTHON = False

def interact(locals=None, use_ipython=True):
    """Provides an interactive shell aka console inside your testcase.

    It looks exact like in a doctestcase and you can copy and paste
    code from the shell into your doctest. The locals in the testcase are
    available, because you are _in_ the testcase.

    In your testcase or doctest you can invoke the shell at any point by
    calling::

        >>> interact( locals() ) #doctest: +SKIP

    locals -- passed to InteractiveInterpreter.__init__()
    """
    savestdout = sys.stdout
    sys.stdout = sys.stderr
    sys.stderr.write('\n'+'='*78)
    sys.stdout.write("""
Interlude DocTest Interactive Console - (c) BlueDynamics Alliance
Note: You have the same locals available as in your test-case.
Ctrl-D ends session and continues testing.
""")

    if use_ipython and HAS_IPYTHON:
        try:
            from IPython.Shell import IPShellEmbed
            ipshell = IPShellEmbed(user_ns=locals)
            ipshell()
        except ImportError:
            from IPython.frontend.terminal.embed import InteractiveShellEmbed
            ipshell = InteractiveShellEmbed(user_ns=locals)
            ipshell()
    else:
        console = code.InteractiveConsole(locals)
        console.interact()

    sys.stdout.write('\nend of Interlude DocTest Interactive Console session\n')
    sys.stdout.write('='*78+'\n')
    sys.stdout = savestdout
