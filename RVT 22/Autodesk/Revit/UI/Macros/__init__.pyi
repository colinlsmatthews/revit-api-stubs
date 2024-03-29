from typing import Tuple, Set, Iterable, List


class ApplicationEntryPoint(UIApplication):
    def __init__(self): ...
    def Initialize(self, obj: Object, addinFolder: str) -> None: ...
    def FinishInitializationEO(self) -> None: ...
    def OnShutdownEO(self) -> None: ...
    @property
    def AddinFolder(self) -> str: ...
    def CreateRibbonTab(self, tabName: str) -> None: ...
    @overload
    def CreateRibbonPanel(self, tab: Tab, panelName: str) -> RibbonPanel: ...
    @overload
    def CreateRibbonPanel(self, panelName: str) -> RibbonPanel: ...
    @overload
    def CreateRibbonPanel(self, tabName: str, panelName: str) -> RibbonPanel: ...
    @overload
    def GetRibbonPanels(self, tabName: str) -> List: ...
    @overload
    def GetRibbonPanels(self, tab: Tab) -> List: ...
    @overload
    def GetRibbonPanels(self) -> List: ...


class DocumentEntryPoint(UIDocument):
    def __init__(self): ...
    def Initialize(self, obj: Object, addinFolder: str) -> None: ...
    def FinishInitializationEO(self) -> None: ...
    def OnShutdownEO(self) -> None: ...
    @property
    def AddinFolder(self) -> str: ...
