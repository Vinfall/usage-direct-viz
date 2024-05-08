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

.. sidebar:: Ranting
    Although so far I only find sidebar and built-in admonitions useful.
    The benefits are so marginal I can't be convinced to learn it any further.
    Probably org mode is better.
    Let alone Markdown.

I use it to learn the standard library `sqlite3` in Python, *basic visualization in Plotly*,
    and **grammer of reStructuredText**.

Usage
-----

.. code-block:: python
    :linenos:
    :emphasize-lines: 2

    pip install -r requirements.txt
    python visualize.py

Now check files in `output` directory.

Ceveats
~~~~~~~

The `database schema`_ of usageDirect is kinda weird, especially the `epochDay`_ part,
    and I have no intention to sanitize those as I only intend to run this once a month.

.. _database schema: https://codeberg.org/fynngodau/usageDirect/src/branch/main/Application/schemas/godau.fynn.usagedirect.persistence.HistoryDatabase/5.json
.. _epochDay: https://docs.oracle.com/javase/8/docs/api/java/time/LocalDate.html#ofEpochDay-long-

License
-------

usage-direct-viz is released into Public Domain under `The Unlicense`_.

.. _The Unlicense: https://unlicense.org
