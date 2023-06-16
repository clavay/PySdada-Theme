PyScada Theme Extension
=======================

This is a extension for PyScada to add a view theme.


What is Working
---------------

 - nothing is test


What is not Working/Missing
---------------------------

 - Documentation

 Installation
 ------------

  - pip install https://github.com/clavay/PyScada-Theme/tarball/master

Create new plugin
-----------------

 - Find "REPLACEME" and replace by the theme name
 - Change the name of :
  - REPLACEME-theme.css
  - logoREPLACEME-gd.png
  - logoREPLACEME.png
  - base_themeREPLACEME.html
  - view_themeREPLACEME.html
  - themeREPLACEMEConfig.py
 - Change templates names in pyscada/theme/templates
 - Edit view (change css theme name) and base (change logo names)
 - zip -r PyScada-Theme.zip PyScada-Theme
 - scp PyScada-Theme.zip user@IP_ADDRESS:.
 - sur OS pyscda : sudo pip3 install PyScada-Theme.zip
 - pstatic
 - pgrestart

Contribute
----------

 - Issue Tracker: https://github.com/clavay/PyScada-Theme/issues
 - Source Code: https://github.com/clavay/PyScada-Theme

License
-------

The project is licensed under the _GNU AFFERO GENERAL PUBLIC LICENSE Version 3 (AGPLv3)_.
-
