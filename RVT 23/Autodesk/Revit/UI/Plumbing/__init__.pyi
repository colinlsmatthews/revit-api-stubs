from typing import Tuple, Set, Iterable, List


class IPipeFittingAndAccessoryPressureDropUIServer:
    def GetDBServerId(self) -> Guid: ...
    def ShowSettings(self, data: PipeFittingAndAccessoryPressureDropUIData) -> bool: ...


class PipeFittingAndAccessoryPressureDropUIDataItem:
    @property
    def IsValidObject(self) -> bool: ...
    def GetEntity(self) -> Entity: ...
    def SetEntity(self, entity: Entity) -> None: ...
    def GetPipeFittingAndAccessoryData(self) -> PipeFittingAndAccessoryData: ...
    def Dispose(self) -> None: ...


class PipeFittingAndAccessoryPressureDropUIData:
    @property
    def IsValidObject(self) -> bool: ...
    def GetUnits(self) -> Units: ...
    def GetUIDataItems(self) -> List[PipeFittingAndAccessoryPressureDropUIDataItem]: ...
    def Dispose(self) -> None: ...
