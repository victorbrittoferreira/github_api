from typing import Dict, List, NewType, Tuple

Repository = NewType("Repository", Dict)
Repositories = NewType("Repositories", List[Repository])


UserBasicData = NewType("UserBasicData", Dict)

GroupedUserData = NewType(
    "GroupedUserData", Tuple[UserBasicData, Repositories]
)

DataSifted = NewType("DataSifted", Dict[str, str | int | list])
