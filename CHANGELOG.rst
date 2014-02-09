
Changes
=======

1.3
---

- needs IPython 1.1.0 or better. Skipped support for older versions.
  [jensens, 2014-02-09]

- added extra require, so when ipython is wanted just depend in buildout,
  pip-requirements, setup, (name it) on``interlude[ipython]``
  [jensens, 2014-02-09]

- start IPython shell with a custom doctest prompt, thus it is easier to
  copy-paste from the shell to the doctest (save a typing a ``%doctest_mode``
  each time. Added also option ``doctest_prompt=False`` to disable this.
  [jensens, 2014-02-09]

1.2
---

- make the ipython support work with newer ipython versions. [sunew]

1.1.1
-----

- fix broken release, include ``*.rst`` with MANIFEST.in

1.1
---

- IPython support - alanjds, 2010-12-19

1.0
---

- initial release
