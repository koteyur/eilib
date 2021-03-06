# Autogenerated file. Do not modify
import typing

from .abstract import EiDatabase, EiDatabaseTable, EiDatabaseTableRow


class Skill(EiDatabaseTableRow):

    __slots__ = (
        "name",
        "code",
        "texture_type_index",
        "base_attributes",
    )

    def __init__(self):
        self.name: str = None
        self.code: str = None
        self.texture_type_index: int = None
        self.base_attributes: typing.List[str] = None
        super().__init__()

    @property
    def _db_type(self):
        return PerksDatabase


class Perk(EiDatabaseTableRow):

    __slots__ = (
        "name",
        "code",
        "texture_type_index",
        "perk",
        "skill",
        "skillid",
        "unk13",
        "skill_level",
        "strength",
        "dexterity",
        "intelligence",
        "cost",
        "modifier",
        "mult",
        "add",
        "active",
        "perk_exclusive",
    )

    def __init__(self):
        self.name: str = None
        self.code: str = None
        self.texture_type_index: int = None
        self.perk: str = None
        self.skill: str = None
        self.skillid: int = None
        self.unk13: int = None
        self.skill_level: int = None
        self.strength: float = None
        self.dexterity: float = None
        self.intelligence: float = None
        self.cost: int = None
        self.modifier: int = None
        self.mult: int = None
        self.add: int = None
        self.active: int = None
        self.perk_exclusive: int = None
        super().__init__()

    @property
    def _db_type(self):
        return PerksDatabase


class Skills(EiDatabaseTable[Skill]):

    _row_type = Skill


class Perks(EiDatabaseTable[Perk]):

    _row_type = Perk


class PerksDatabase(EiDatabase):

    __slots__ = (
        "skills",
        "perks",
    )

    def __init__(self):
        self.skills = Skills()
        self.perks = Perks()
        super().__init__()
