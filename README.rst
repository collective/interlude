Interlude - Interactive Doctests
================================

Provides an interactive shell aka console inside your doctest case.

The console looks exact like in a doctest-case and you can copy and paste
code from the shell into your doctest. It feels as you are in the test case
itself. Its not pdb, it's a python shell.

In your doctest you can invoke the shell at any point by calling::

    >>> interact(locals())


To make your testrunner interlude aware, pass ``interact`` as a global to the
``DocFileSuite`` as shown here::

    ...
    import interlude
    ...
    suite = DocFileSuite( ..., globs=dict(interact=interlude.interact), ...)
    ...


If `IPython <http://ipython.org/>`_ is available it opens an IPython prompt.
The prompt is modified and looks like in a doctest. To surpress the
prompt modifications call ``interact`` with additional kwarg
``doctest_prompt=False``.


License
=======

`interlude` is copyright 2006-2014 by BlueDynamics Alliance, Klein & Partner KG,
Austria. It is under the `GNU Lesser General Public License (LGPLv3).
<http://opensource.org/licenses/lgpl-3.0.html>`_

- code repository at `github collective <http://github.com/collective/interlude>`_

- written by `Jens Klein <mailto:jens@bluedynamics.com>`_

- IPython support contributed by `Alan Justino <http://github.com/alanjds>`_

- Upgrade/Bugfixes contributed by `Sune Broendum Woeller <https://github.com/sunew>`_

