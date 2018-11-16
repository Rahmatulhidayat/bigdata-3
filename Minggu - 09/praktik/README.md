
Cek dan Upgrade versi Pip

    Pip –version

       (base) C:\Users\Doto Baliga>pip --version
            pip 18.1 from c:\users\doto baliga\miniconda3\lib\site-packages\pip (python 3.7)
            
Pip install –upgrade pip

       (base) C:\Users\Doto Baliga>Pip install --upgrade pip
            Requirement already up-to-date: pip in c:\users\doto baliga\miniconda3\lib\site-packages (18.1)
            
Pip install jupyter
            
    (base) C:\Users\Doto Baliga>Pip install jupyter
    Requirement already satisfied: jupyter in c:\users\doto baliga\miniconda3\lib\site-packages (1.0.0)
    Requirement already satisfied: qtconsole in c:\users\doto baliga\miniconda3\lib\site-packages (from jupyter) (4.4.3)
    Requirement already satisfied: notebook in c:\users\doto baliga\miniconda3\lib\site-packages (from jupyter) (5.7.0)
    Requirement already satisfied: ipywidgets in c:\users\doto baliga\miniconda3\lib\site-packages (from jupyter) (7.4.2)
    Requirement already satisfied: ipykernel in c:\users\doto baliga\miniconda3\lib\site-packages (from jupyter) (5.1.0)
    Requirement already satisfied: nbconvert in c:\users\doto baliga\miniconda3\lib\site-packages (from jupyter) (5.4.0)
    Requirement already satisfied: jupyter-console in c:\users\doto baliga\miniconda3\lib\site-packages (from jupyter) (6.0.0)
    Requirement already satisfied: jupyter-client>=4.1 in c:\users\doto baliga\miniconda3\lib\site-packages (from qtconsole->jupyter)   (5.2.3)
    Requirement already satisfied: jupyter-core in c:\users\doto baliga\miniconda3\lib\site-packages (from qtconsole->jupyter) (4.4.0)
    Requirement already satisfied: traitlets in c:\users\doto baliga\miniconda3\lib\site-packages (from qtconsole->jupyter) (4.3.2)
    Requirement already satisfied: ipython-genutils in c:\users\doto baliga\miniconda3\lib\site-packages (from qtconsole->jupyter) (0.2.0)
    Requirement already satisfied: pygments in c:\users\doto baliga\miniconda3\lib\site-packages (from qtconsole->jupyter) (2.2.0)
    Requirement already satisfied: prometheus-client in c:\users\doto baliga\miniconda3\lib\site-packages (from notebook->jupyter) (0.4.2)
    Requirement already satisfied: tornado>=4 in c:\users\doto baliga\miniconda3\lib\site-packages (from notebook->jupyter) (5.1.1)
    Requirement already satisfied: jinja2 in c:\users\doto baliga\miniconda3\lib\site-packages (from notebook->jupyter) (2.10)
    Requirement already satisfied: terminado>=0.8.1 in c:\users\doto baliga\miniconda3\lib\site-packages (from notebook->jupyter) (0.8.1)
    Requirement already satisfied: pyzmq>=17 in c:\users\doto baliga\miniconda3\lib\site-packages (from notebook->jupyter) (17.1.2)
    Requirement already satisfied: nbformat in c:\users\doto baliga\miniconda3\lib\site-packages (from notebook->jupyter) (4.4.0)
    Requirement already satisfied: Send2Trash in c:\users\doto baliga\miniconda3\lib\site-packages (from notebook->jupyter) (1.5.0)
    Requirement already satisfied: widgetsnbextension~=3.4.0 in c:\users\doto baliga\miniconda3\lib\site-packages (from ipywidgets->jupyter) (3.4.2)
    Requirement already satisfied: ipython>=4.0.0; python_version >= "3.3" in c:\users\doto baliga\miniconda3\lib\site-packages (from ipywidgets->jupyter) (7.1.1)
    Requirement already satisfied: testpath in c:\users\doto baliga\miniconda3\lib\site-packages (from nbconvert->jupyter) (0.4.2)
    Requirement already satisfied: entrypoints>=0.2.2 in c:\users\doto baliga\miniconda3\lib\site-packages (from nbconvert->jupyter) (0.2.3)
    Requirement already satisfied: defusedxml in c:\users\doto baliga\miniconda3\lib\site-packages (from nbconvert->jupyter) (0.5.0)
    Requirement already satisfied: mistune>=0.8.1 in c:\users\doto baliga\miniconda3\lib\site-packages (from nbconvert->jupyter) (0.8.4)
    Requirement already satisfied: pandocfilters>=1.4.1 in c:\users\doto baliga\miniconda3\lib\site-packages (from nbconvert->jupyter) (1.4.2)
    Requirement already satisfied: bleach in c:\users\doto baliga\miniconda3\lib\site-packages (from nbconvert->jupyter) (3.0.2)
    Requirement already satisfied: prompt-toolkit<2.1.0,>=2.0.0 in c:\users\doto baliga\miniconda3\lib\site-packages (from jupyter-console->jupyter) (2.0.7)
    Requirement already satisfied: python-dateutil>=2.1 in c:\users\doto baliga\miniconda3\lib\site-packages (from jupyter-client>=4.1->qtconsole->jupyter) (2.7.5)
    Requirement already satisfied: six in c:\users\doto baliga\miniconda3\lib\site-packages (from traitlets->qtconsole->jupyter) (1.11.0)
    Requirement already satisfied: decorator in c:\users\doto baliga\miniconda3\lib\site-packages (from traitlets->qtconsole->jupyter) (4.3.0)
    Requirement already satisfied: MarkupSafe>=0.23 in c:\users\doto baliga\miniconda3\lib\site-packages (from jinja2->notebook->jupyter) (1.1.0)
    Requirement already satisfied: pywinpty>=0.5; os_name == "nt" in c:\users\doto baliga\miniconda3\lib\site-packages (from terminado>=0.8.1->notebook->jupyter) (0.5.4)
    Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in c:\users\doto baliga\miniconda3\lib\site-packages (from nbformat->notebook->jupyter) (2.6.0)
    Requirement already satisfied: colorama; sys_platform == "win32" in c:\users\doto baliga\miniconda3\lib\site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (0.4.0)
    Requirement already satisfied: pickleshare in c:\users\doto baliga\miniconda3\lib\site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (0.7.5)
    Requirement already satisfied: backcall in c:\users\doto baliga\miniconda3\lib\site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (0.1.0)
    Requirement already satisfied: setuptools>=18.5 in c:\users\doto baliga\miniconda3\lib\site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (40.2.0)
    Requirement already satisfied: jedi>=0.10 in c:\users\doto baliga\miniconda3\lib\site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (0.13.1)
    Requirement already satisfied: webencodings in c:\users\doto baliga\miniconda3\lib\site-packages (from bleach->nbconvert->jupyter) (0.5.1)
    Requirement already satisfied: wcwidth in c:\users\doto baliga\miniconda3\lib\site-packages (from prompt-toolkit<2.1.0,>=2.0.0->jupyter-console->jupyter) (0.1.7)
    Requirement already satisfied: parso>=0.3.0 in c:\users\doto baliga\miniconda3\lib\site-packages (from jedi>=0.10->ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (0.3.1)            
    
    
Menjalankan Notebook  "jupyter notebook"

    (base) C:\Users\Doto Baliga>jupyter notebook
    [W 01:40:06.945 NotebookApp] Terminals not available (error was No module named 'winpty.cywinpty')
    [I 01:40:06.954 NotebookApp] Serving notebooks from local directory: C:\Users\Doto Baliga
    [I 01:40:06.955 NotebookApp] The Jupyter Notebook is running at:
    [I 01:40:06.955 NotebookApp] http://localhost:8888/?token=4e3a428fe74790753e70656bcdbec02fe08e9543f94b6a19
    [I 01:40:06.955 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 01:40:07.114 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=4e3a428fe74790753e70656bcdbec02fe08e9543f94b6a19
    [I 01:40:07.572 NotebookApp] Accepting one-time-token-authenticated connection from ::1
    