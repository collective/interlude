#
# Copyright 2006-2014, BlueDynamics Alliance, Austria - http://bluedynamics.com
#
# GNU Lesser General Public Licence

import code
import sys

try:
    from IPython.terminal.embed import InteractiveShellEmbed
    from IPython.config.loader import Config
    HAS_IPYTHON = True
except ImportError:
    HAS_IPYTHON = False

DELIMITER = '\n' + '=' * 78 + '\n'

START_BANNER = """\
Interlude DocTest Interactive Console - (c) BlueDynamics Alliance
Note: You have the same local variables available as in your test-case.
Ctrl-D ends session and continues testing.
"""

END_BANNER = '\nEnd of Interlude DocTest Interactive Console session'

def interact(locals=None, use_ipython=True, doctest_prompt=True):
    """Provides an interactive shell aka console inside your testcase.

    It looks exact like in a doctestcase and you can copy and paste
    code from the shell into your doctest. The locals in the testcase are
    available, because you are _in_ the testcase.

    In your testcase or doctest you can invoke the shell at any point by
    calling::

        >>> interact( locals() )

    locals
        locals available in shell

    use_ipython
        enabled/disable ipython (only if module installed)

    doctest_prompt
        use doctest style prompt in ipython (only if module installed)
    """
    savestdout = sys.stdout
    sys.stdout = sys.stderr
    sys.stdout.write(DELIMITER)
    if use_ipython and HAS_IPYTHON:
        cfg = Config()
        cfg.TerminalInteractiveShell.confirm_exit = False
        if doctest_prompt:
            cfg.PromptManager.in_template = u'>>> '
            cfg.PromptManager.in2_template = u'... '
            cfg.PromptManager.out_template = u''
            cfg.PromptManager.justify = False
        ipshell = InteractiveShellEmbed(user_ns=locals, config=cfg)
        ipshell(DELIMITER + START_BANNER)
    else:
        sys.stdout.write(START_BANNER + '\n')
        console = code.InteractiveConsole(locals)
        console.interact()

    sys.stdout.write(END_BANNER + DELIMITER)
    sys.stdout = savestdout
