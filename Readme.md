# Readme

## Introduction
This is a Have I been Pwned password check written in Python. It won't save anthing or send information to an other web service than Have I Been Pwned.  
For a more specific API description you can read it on the [API documentation of Have I Been Pwned](https://haveibeenpwned.com/API/v2#PwnedPasswords).

## Requirements
- Python 3.6 or higher
- [urllib3](https://urllib3.readthedocs.io/en/latest/index.html#installing)
- [PySide2](https://wiki.qt.io/Qt_for_Python)

You can install **urllib3** simple over `pip`. Just enter the following line:  
[pip install urllib3](https://pypi.org/project/urllib3/)

**PySide2** can be installed over `pip` as well with [pip install PySide2](https://pypi.org/project/PySide2/)

## How to run the script
You can just execute the module. The `__main__.py` has the full logic to convert and execute the password and the API calls and checks.
