from typing import List, Optional
from datetime import datetime
from dataclasses import dataclass

@dataclasses
class Demo:
    name : Optional[str] = None
    value : Optional[int] = None
    created_at : Optional[datetime] = None
    modified_at : Optional[datetime] = None


@dataclasses
class DemoWrapper:
    meta_information : Optional[str] = None
    demo : Optional[Demo] = None

    @classmethod
    def to_demo(cls):
        return Demo(
            name = name if name is not None else name,
            value = value if value is not None else value,
            created_at = created_at if created_at is not None else created_at,
            modified_at = modified_at if modified_at is not None else modified_at,
        )
