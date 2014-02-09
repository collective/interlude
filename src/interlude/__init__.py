#
# Copyright 2006-2014, BlueDynamics Alliance, Austria - http://bluedynamics.com
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

BANNER = """
Interlude DocTest Interactive Console - (c) BlueDynamics Alliance
Note: You have the same locals available as in your test-case.
Ctrl-D ends session and continues testing.
"""

def interact(locals=None, use_ipython=True, doctest_prompt=True):
    """Provides an interactive shell aka console inside your testcase.

    It looks exact like in a doctestcase and you can copy and paste
    code from the shell into your doctest. The locals in the testcase are
    available, because you are _in_ the testcase.

    In your testcase or doctest you can invoke the shell at any point by
    calling::

        >>> interact( locals() ) #doctest: +SKIP

    locals
        locals available in shell

    use_ipython
        enabled/disable ipython (only if module installed)

    doctest_prompt
        use doctest style prompt in ipython (only if module installed)
    """
    savestdout = sys.stdout
    sys.stdout = sys.stderr
    sys.stderr.write('\n' + '=' * 78)

    if use_ipython and HAS_IPYTHON:
        # from IPython.lib.deepreload import reload as dreload
        # locals.append(dreload)
        try:
            from IPython.Shell import IPShellEmbed
            ipshell = IPShellEmbed(user_ns=locals)
            ipshell(argv=ipython_argv)
        except ImportError:
            try:
                from IPython.terminal.embed import InteractiveShellEmbed
            except ImportError:
                # not sure if this is needed for bbb
                from IPython.terminal.frontend.embed import InteractiveShellEmbed
            from IPython.config.loader import Config
            cfg = Config()
            shell_config = cfg.InteractiveShellEmbed
            shell_config.prompt_in1 = '    >>> '
            shell_config.prompt_in2 = '    ... '
            shell_config.prompt_out = '    '
            ipshell = InteractiveShellEmbed(user_ns=locals, config=cfg)
            ipshell(BANNER)
    else:
        sys.stdout.write(BANNER)
        console = code.InteractiveConsole(locals)
        console.interact()

    sys.stdout.write('\nEnd of Interlude DocTest Interactive Console session\n')
    sys.stdout.write('=' * 78 + '\n')
    sys.stdout = savestdout
