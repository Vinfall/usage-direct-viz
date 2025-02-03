usage-direct-viz
================

Visualization of exported `usageDirect`_ SQLite3 database.

.. _usageDirect: https://codeberg.org/fynngodau/usageDirect

.. hint:: It's so painful to add hyperlink in rst...

Intro
------

This is mainly a silly little project to add some charts to:

#. personal OKR
#. personal monthly activity report

.. tip:: Chances are you won't find it useful.

I use it to learn the standard library `sqlite3` in Python, *basic visualization in Plotly*,
and **grammer of reStructuredText**.

.. note:: Although so far I only find sidebar and built-in admonitions useful.
    The benefits are so marginal [#f1]_ I can't be convinced to learn it any further.
    Probably org mode is better.
    Let alone Markdown.

.. [#f1] The ranting is caused by my not using extension. reStructuredText is much more powerful with that.

Usage
-----

.. code-block:: python

    pip install -r requirements.txt
    python visualize.py

    # it's easier with uv, not need to manage venv yourself
    uv run visualize.py

Now check files in `output` directory.

Caveats
~~~~~~~

The `database schema`_ of usageDirect is kinda weird, especially the `epochDay`_ part,
    and I have no intention to sanitize those as I only intend to run this once a month.

.. _database schema: https://codeberg.org/fynngodau/usageDirect/src/branch/main/Application/schemas/godau.fynn.usagedirect.persistence.HistoryDatabase/5.json
.. _epochDay: https://docs.oracle.com/javase/8/docs/api/java/time/LocalDate.html#ofEpochDay-long-

License
-------

usage-direct-viz is released into Public Domain under `The Unlicense`_.

.. _The Unlicense: https://unlicense.org