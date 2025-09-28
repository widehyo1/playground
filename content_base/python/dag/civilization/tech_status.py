from enum import Enum

class TechStatus(Enum):
    RESEARCHED = 1
    CURRENTLY_RESEARCHING = 2
    AVALIABLE = 3
    NOT_YET_AVAILABLE = 4

if __name__ == '__main__':
    print(TechStatus.RESEARCHED)
    print(TechStatus.CURRENTLY_RESEARCHING)
    print(TechStatus.AVALIABLE)
    print(TechStatus.NOT_YET_AVAILABLE)
