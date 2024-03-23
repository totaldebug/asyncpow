.. _quickstart:

**************
🚀 Quick Start
**************

This quick start guide will take you through the easiest way to get up and running.

Installation
############

This package is distributed on PyPI and can be installed with `pip`:

.. code-block:: shell
   :linenos:
   pip install asyncpow


To use the package in your Python project, you will need to import the required modules from below:

.. code-block:: python
   :linenos:

   from asyncpow import Overseerr

   async with OverseerrAPI(
       host="OVERSEERR_HOST",
       port="5055",
       ssl=True,
       base_url="overseerr/",
       api_key="OVERSEER_KEY",
    ) as api:
       # Inside the context, you can use the API wrapper as needed
       status = await api.status.get_status()
       print("Status:", status)
