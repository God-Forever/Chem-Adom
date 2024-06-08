"""
Chem-Atom 0.0.5

Author: GodForever
Project: https://pypi.org/project/chem-atom/

Chem-Atom is a library used for storing and editing chemical structural formulas. It provides an easy-to-use class Atom,
which primarily stores atoms to achieve functions such as structure registration, modification, and conversion.

All:
    Atom (class)
    bond (method)
    delete_atom (method)
    from_smiles (method)
    get_all_atoms (method)
    get_atom (method)
    get_atom_id (method)
    get_formula (method)
    get_smiles (method)
    reset_tags (method)
"""
from typing import *

__all__ = ['Atom', 'bond', 'delete_atom', 'from_smiles', 'get_all_atoms', 'get_atom', 'get_formula', 'get_atom_id', 'get_smiles', 'reset_tags']

class Atom:
    """
    The Atom class is used to represent an atom in a structure, containing its elements, charge, lone pair electrons,
    chemical bonds, and unique ID. It also includes some methods to achieve functions such as atomic bonding, breaking
    bonds, and modifying atomic parameters.
    
    Attributes:
        element_info (dict[str, list]): Basic information of elements. (Class attribute)
        id_map (dict[int, Atom]): The mapping relationship between IDs and registered Atom instances. (Class attribute)
        id_pool (List[int]): Available IDs. (Class attribute)
    
        access_tag (bool): A tag used during traversing the structure.
        bonds (List[int] | None): Record the atoms bonded to the current atom.
        charge (int): The charge number of the current atom.
        element (str): The element of the current atom.
        id (int): A unique ID identifies an atom.
        lone_electron (int): The number of lone electrons in the current atom.
    
    Raises:
        AtomError
        BondError
        ChargeError
        ElementError
        IdError
        LoneElectronError
    """
    id_map: Dict[int, 'Atom']
    access_tag: bool
    bonds: Optional[List[int]]
    charge: int
    element: str
    id: int
    lone_electron: int
    def __init__(self, element: str = 'H', bonds: Optional[List[Union[int, 'Atom']]] = None, charge: int = 0, lone_electron: Optional[int] = None, bond_: bool = True, auto_modify: bool = False) -> None:
        """
        Initialize class Atom.
        
        Args:
            element (str): The element of the atom. Default to "H".
            bonds (list[int | Atom] | None): The atoms bonded to the atom. Default to None.
            charge (int): The charge number of the atom. Default to 0.
            lone_electron (int | None): The number of lone electrons in the atom. Default to None (automatically set).
            bond_ (bool): Whether to automatically bond with atoms in bonds. Default to True. (Warning: do not set this
                          parameter to False. Otherwise, it will lead to some unexpected problems)
            auto_modify (bool): Whether to automatically adjust the number of lone electrons. Default to False.
        
        Raises:
            AtomError
            BondError
            ChargeError
            ElementError
            IdError
            LoneElectronError
        """
        ...
    @classmethod
    def bond(cls, atom_1: Union[int, 'Atom'], atom_2: Union[int, 'Atom'], use: Literal['hydro', 'lone_electron', 'all'] = 'hydro', allow_carbene: bool = False) -> None:
        """
        Bond two atoms through hydrogen atoms, lone electrons, or both.
        
        Args:
            atom_1 (int | Atom): The first atom for bonding.
            atom_2 (int | Atom): The second atom for bonding.
            use (Literal['hydro', 'lone_electron', 'both']): If use == "hydro", it means each of the two atoms loses a
                                                             hydrogen atom to form a bond (default). If use ==
                                                             "lone_electron", it means use lone electrons on the two
                                                             atoms to form bonds if possible. If use == "both", it means
                                                             use both.
            allow_carbene (bool): Whether to allow losing two hydrogen atoms on the same atom to form a carbene-like
                                  structure. Default to False.
        
        Raises:
            AtomError
            BondError
            LoneElectronError
        """
        ...
    @classmethod
    def break_bond(cls, atom_1: Union[int, 'Atom'], atom_2: Union[int, 'Atom']) -> None:
        """
        Break a bond between two atoms.
        
        Args:
            atom_1 (int | Atom): The first atom for breaking bond.
            atom_2 (int | Atom): The second atom for breaking bond.
        
        Raises:
            AtomError
            BondError
        """
        ...
    @classmethod
    def delete_atom(cls, atom: Union[int, 'Atom']) -> None:
        """
        Delete the current atom, Remove it from the list of registered atoms.
        
        Raises:
            AtomError
        """
        ...
    @classmethod
    def from_smiles(cls, smiles: str, top: bool = True, val: Optional[List[any]] = None) -> Union['Atom', Tuple['Atom', int]]:
        """
        Get a structure from a SMILES.
        
        Args:
            smiles (str): The SMILES.
            top (bool): Whether to be the entry point for the recursion. Default to True. (Warning: do not set this
                       parameter to False. Otherwise, it will lead to some unexpected problems)
            val (list | None): Variables passed during recursion. Default to None. (Warning: do not set this parameter
                               to anything else. Otherwise, it will lead to some unexpected problems)
        
        Returns:
            str: An atom in the result structure.
        
        Raises:
            SmilesError
        """
        ...
    @classmethod
    def get_all_atoms(cls) -> List['Atom']:
        """
        Get the list of registered atoms.
        
        Returns:
            list['Atom']: The list of registered atoms.
        """
        ...
    @classmethod
    def get_atom(cls, atom: Union[int, 'Atom']) -> Atom:
        """
        Get an Atom instance through id or instance.
        
        Args:
            atom (int | Atom): An id or an instance represents the atom.
        
        Returns:
            Atom: The instance represents the atom.
        
        Raises:
            AtomError
        """
        ...
    @classmethod
    def get_atom_id(cls, atom: Union[int, 'Atom']) -> int:
        """
        Get the id of an Atom instance through id or instance.
        
        Args:
            atom (int | Atom): An id or an instance represents the atom.
        
        Returns:
            Atom: The id represents the atom.
        
        Raises:
            AtomError
        """
        ...
    @classmethod
    def get_formula(cls, atom: Atom) -> str:
        """
        Convert the structure of an atom into formula with Hill System.
        
        Args:
            atom (Atom): The atom to convert.
        
        Returns:
            str: The result formula.
        
        Raises:
            AtomError
        """
        ...
    @classmethod
    def get_smiles(cls, atom: Atom) -> str:
        """
        Convert the structure of an atom into SMILES.
        
        Args:
            atom (Atom): The atom to convert.
        
        Returns:
            str: The result SMILES.
        
        Raises:
            AtomError
            SmilesError
        """
        ...
    @classmethod
    def reset_tags(cls) -> None:
        """
        Set all the access tags to False.
        """
        ...
    def bond_with(self, atom: Union[int, 'Atom'], bond_back: bool = True, use: Literal['hydro', 'lone_electron', 'both'] = 'hydro', allow_carbene: bool = False) -> None:
        """
        Bond the current atom with another atom through hydrogen atoms, lone electrons, or both.
        
        Args:
            atom (int | Atom): Target atom for bonding.
            bond_back (bool): Whether to bond back. Default to True. (Warning: do not set this parameter to False.
                              Otherwise, it will lead to some unexpected problems)
            use (Literal['hydro', 'lone_electron', 'both']): If use == "hydro", it means each of the two atoms loses a
                                                             hydrogen atom to form a bond (default). If use ==
                                                             "lone_electron", it means use lone electrons on the two
                                                             atoms to form bonds if possible. If use == "both", it means
                                                             use both.
            allow_carbene (bool): Whether to allow losing two hydrogen atoms on the same atom to form a carbene-like
                                  structure. Default to False.
        
        Raises:
            AtomError
            BondError
            LoneElectronError
        """
        ...
    def break_bond_with(self, atom: Union[int, 'Atom'], break_bond_back: bool = True) -> None:
        """
        Break a bond between the current atom and another atom.
        
        Args:
            atom (int | Atom): Target atom for breaking bond.
            break_bond_back (bool): Whether to break bond back. Default to True. (Warning: do not set this parameter to
                                    False. Otherwise, it will lead to some unexpected problems)
        
        Raises:
            AtomError
            BondError
        """
        ...
    def delete(self) -> None:
        """
        Delete the current atom, Remove it from the list of registered atoms.
        
        Raises:
            AtomError
        """
        ...
    def get_bonds(self) -> List[int]:
        """
        Get the bonds attribute.
        
        Returns:
            list[int]: A list records the atoms bonded to the current atom.
        
        Raises:
            AtomError
        """
        ...
    def get_charge(self) -> int:
        """
        Get the charge attribute.
        
        Returns:
            int: The charge number of the current atom.
        
        Raises:
            AtomError
        """
        ...
    def get_element(self) -> str:
        """
        Get the element attribute.
        
        Returns:
            int: The element of the current atom.
        
        Raises:
            AtomError
        """
        ...
    def get_id(self) -> int:
        """
        Get the id attribute.
        
        Returns:
            int: The ID of the current atom.
        
        Raises:
            AtomError
        """
        ...
    def get_lone_electron(self) -> int:
        """
        Get the lone_electron attribute.
        
        Returns:
            The number of lone electrons in the current atom.
        
        Raises:
            AtomError
        """
        ...
    def set_charge(self, charge: int) -> None:
        """
        Set the charge attribute to a new number.
        
        Args:
            charge (int): New charge number you want to assign to the charge attribute.
        
        Raises:
            AtomError
            BondError
            ChargeError
        """
        ...
    def set_element(self, element: str) -> None:
        """
        Set the element attribute to a new number.
        
        Args:
            element (int): New element you want to assign to the element attribute.
        
        Raises:
            AtomError
            BondError
            ElementError
        """
        ...
    def set_lone_electron(self, lone_electron: int, auto_modify: bool = False) -> None:
        """
        Set the lone_electron attribute to a new number.
        
        Args:
            lone_electron (int): New number of lone electrons you want to assign to the lone_electron attribute.
            auto_modify (bool): Whether to automatically adjust the number of lone electrons. Default to False.
        
        Raises:
            AtomError
            BondError
            LoneElectronError
        """
        ...
    def survive(self) -> None: ...
    def to_formula(self, top: bool = True, val: Optional[List[any]] = None) -> str:
        """
        Convert the structure of the current atom into formula with Hill System.
        
        Args:
            top (bool): Whether to be the entry point for the recursion. Default to True. (Warning: do not set this
                       parameter to False. Otherwise, it will lead to some unexpected problems)
            val (list | None): Variables passed during recursion. Default to None. (Warning: do not set this parameter
                               to anything else. Otherwise, it will lead to some unexpected problems)
        
        Returns:
            str: The result formula.
        
        Raises:
            AtomError
        """
        ...
    def to_smiles(self, top: bool = True, val: Optional[List[any]] = None) -> str:
        """
        Convert the structure of the current atom into SMILES.
        
        Args:
            top (bool): Whether to be the entry point for the recursion. Default to True. (Warning: do not set this
                       parameter to False. Otherwise, it will lead to some unexpected problems)
            val (list | None): Variables passed during recursion. Default to None. (Warning: do not set this parameter
                               to anything else. Otherwise, it will lead to some unexpected problems)
        
        Returns:
            str: The result SMILES.
        
        Raises:
            AtomError
            SmilesError
        """
        ...

class AtomError(Exception):
    atom: int
    message: str
    def __init__(self, message: str, atom: int) -> None: ...

class BondError(Exception):
    atom: int
    message: str
    def __init__(self, message: str, atom: int) -> None: ...

class ChargeError(Exception):
    atom: int
    message: str
    def __init__(self, message: str, atom: int) -> None: ...

class ElementError(Exception):
    atom: int
    message: str
    def __init__(self, message: str, atom: int) -> None: ...

class IdError(Exception):
    message: str
    def __init__(self, message: str) -> None: ...

class LoneElectronError(Exception):
    atom: int
    message: str
    def __init__(self, message: str, atom: int) -> None: ...

class SmilesError(Exception):
    atom: Optional[int]
    message: str
    def __init__(self, message: str, atom: Optional[int]) -> None: ...

bond: Callable
delete_atom: Callable
from_smiles: Callable
get_all_atoms: Callable
get_atom: Callable
get_atom_id: Callable
get_formula: Callable
get_smiles: Callable
reset_tags: Callable
