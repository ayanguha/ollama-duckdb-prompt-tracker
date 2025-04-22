Prompt Manager 
====================

Usage  
------------------------

.. automodule:: prompt_manager
    :members:
    :member-order: bysource
    :undoc-members:
    :show-inheritance:
    :noindex:
    :special-members: __init__, __call__
    :exclude-members: __module__, __dict__, __weakref__, __doc__

Installation  
------------------------

Ollama Installation: https://ollama.com/download 

Ollama CLI commands: https://github.com/ollama/ollama?tab=readme-ov-file#quickstart ::

    ollama 
    Usage
        ollama [flags]
        ollama [command]

    Available Commands
    serve       Start ollama
    create      Create a model from a Modelfile
    show        Show information for a model
    run         Run a model
    pull        Pull a model from a registry
    push        Push a model to a registry
    list        List models
    ps          List running models
    cp          Copy a model
    rm          Remove a model
    help        Help about any command

    Flags:
    -h, --help      help for ollama
    -v, --version   Show version information

    Use "ollama [command] --help" for more information about a command.


Ollama Python Package

.. code-block:: bash

    pip install ollama 