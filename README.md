# Chem-Atom 0.0.5

- Author: GodForever

- Project: https://pypi.org/project/chem-atom

Chem-Atom is a library used for storing and editing chemical structural formulas. It provides an easy-to-use class Atom,which primarily stores atoms to achieve functions such as structure registration, modification, and conversion. 

## How to start

- Ensure that you have Python versions between 3.8 and 3.12. If not, please go to https://www.python.org/downloads/ to download or use conda virtual environment.

- Using the pip tool to obtain Chem-Atom:
```cmd
pip install Chem-Atom==0.0.5
```

- Import the module. A possible import statement is:
```python
import Atom
```

- Or you can use "from ... import ..." statement:
```python
from Atom import *
```

- Start!
```python
# example
import Atom
C = Atom.Atom("C")
print(C)
# <Atom id=1234, element=C, bonds=[6616(H), 9832(H), 8182(H), 4138(H)], charge=0, lone_electron=0>
```
