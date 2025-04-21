Overview
===============

The goal of this project is to build a Text2SQL application that can be used to convert natural language queries into SQL queries. The application will be built using a combination of LLMs and traditional database management techniques. The problem is described in `Blog <https://guha-ayan.medium.com/text2sql-evaluation-accelerator-a52774832bdf>`_ 

User Interface and API layers will be standard web development components — to enable functionalities for end users. There are a ton of great examples of such applications. In the demo, I used streamlit and Flask, though I would propose to use any better alternative for streamlit.

Functional view 
------------------------

.. image:: _static/Misc-OverAll\ Idea.jpg
   :width: 600px
   :align: center 

Key aspects of the solution will be

**Database Manager**

A key requirement of the application to have an extensible component to manage all database interactions. Each database/data warehousing solution exposes metadata differently with minor variations. The SQL dialects and available functions are unique. Documentation pages are database specific too. And very importantly, each database reports query performance statistics differently. So it is critical to use an adapter pattern to build out specific database manager — or even better to utilise existing libraries via a thin wrapper on top of them.

**LLM Manager**

Similar to database manager, the idea is to manage a way to standardise how the prompts are collected, tuned and modified over various experimentation and finally able to choose the right one. While I started the basic demo using Ollama to keep things local, it seems Anthropic MCP is designed for this exact purpose and can be adapted to Text2SQL use case

**Result Manager** 

A standard way to store the prompt, system prompt, LLM response (with chain of thought if applicable), SQL generated, SQL run statistics, SQL similarity with a curated set etc. Generally this can be any database — I used local couchdb server as I believe NoSQL databases will be a good choice for this scenario.

MVP view 
------------------------

Here is how the demo version looks like

.. image:: _static/Misc-MVP\ build.jpg
   :width: 600px
   :align: center 

A screen Recording `Youtube Video <https://youtu.be/LADTN3Lj8UU>`_ 
