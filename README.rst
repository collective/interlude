Provides an interactive shell aka console inside your doctest case.
    
The console looks exact like in a doctest-case and you can copy and paste
code from the shell into your doctest. It feels as you are in the test case 
itself. Its not pdb, it's a python shell. 

In your doctest you can invoke the shell at any point by calling::
        
    >>> interact( locals() )        

To make your testrunner interlude aware following is needed:

1) import interlude

2) suite = DocFileSuite( ..., globs=dict(interact=interlude.interact), ...) 

License
=======

`interlude` is copyright 2006-2010 by BlueDynamics Alliance, Klein & Partner KG,
Austria. It is under the `GNU Lesser General Public License (LGPLv3). 
<http://opensource.org/licenses/lgpl-3.0.html>`_

- code repository at `github collective <http://github.com/collective/interlude>`_

- written by `Jens Klein <mailto:jens@bluedynamics.com>`_ 

- IPython support contributed by `Alan Justino <http://github.com/alanjds>`_ 
