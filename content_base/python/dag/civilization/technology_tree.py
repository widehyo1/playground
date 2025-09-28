from dataclasses import dataclass
from typing import Optional, List
from tech_status import (
    TechStatus,
)

done = TechStatus.RESEARCHED 
working = TechStatus.CURRENTLY_RESEARCHING 
available = TechStatus.AVALIABLE 
not_avaliable = TechStatus.NOT_YET_AVAILABLE 

@dataclass
class Technology:
    name: str
    parents: Optional[List["Technology"]] = None
    children: Optional[List["Technology"]] = None
    status: Optional[TechStatus] = None

    def __post_init__(self):
        self.parents = self.parents or []
        self.children = self.children or []
        self.status = self.status or not_avaliable

    @property
    def done_parent_technologies(self):
        return [parent for parent in self.parents if parent.status == done]

    @property
    def done_children_technologies(self):
        return [child for child in self.children if child.status == done]

    def __repr__(self):
        parent_count = len(self.parents)
        children_count = len(self.children)

        done_parent_technology_count = len(self.done_parent_technologies)
        done_children_technology_count = len(self.done_children_technologies)

        return f"< Technology {self.name}: {self.status}\n" \
                f"parent status: {done_parent_technology_count}/{parent_count}\n" \
                f"children status: {done_children_technology_count}/{children_count} >"

@dataclass
class TechnologyTree:
    root: Optional[Technology] = None

    def __post_init__(self):
        self.root = self.root or Technology('dummy')

    def __repr__(self):
        return f"< TechnologyTree\n" \
                f"root: {self.root}\n" \
                ">"


if __name__ == '__main__':
    agriculture = Technology('Agriculture')
    print(agriculture)
    technology_tree = TechnologyTree()
    technology_tree.root = agriculture
    print(technology_tree)

