from typing import Tuple, Set, Iterable, List


class IFCImportOptions:
    def __init__(self): ...
    @property
    def Intent(self) -> IFCImportIntent: ...
    @Intent.setter
    def Intent(self, Intent: IFCImportIntent) -> None: ...
    @property
    def AutoJoin(self) -> bool: ...
    @AutoJoin.setter
    def AutoJoin(self, AutoJoin: bool) -> None: ...
    @property
    def AutocorrectOffAxisLines(self) -> bool: ...
    @AutocorrectOffAxisLines.setter
    def AutocorrectOffAxisLines(self, AutocorrectOffAxisLines: bool) -> None: ...
    @property
    def Action(self) -> IFCImportAction: ...
    @Action.setter
    def Action(self, Action: IFCImportAction) -> None: ...
    @property
    def ForceImport(self) -> bool: ...
    @ForceImport.setter
    def ForceImport(self, ForceImport: bool) -> None: ...
    @property
    def CreateLinkInstanceOnly(self) -> bool: ...
    @CreateLinkInstanceOnly.setter
    def CreateLinkInstanceOnly(self, CreateLinkInstanceOnly: bool) -> None: ...
    @property
    def RevitLinkFileName(self) -> str: ...
    @RevitLinkFileName.setter
    def RevitLinkFileName(self, RevitLinkFileName: str) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def GetConversionData(self) -> LinkConversionData: ...
    def GetExtraOptions(self) -> IDictionary: ...
    def SetExtraOptions(self, options: IDictionary) -> None: ...
    def Dispose(self) -> None: ...


class IFCImportIntent:
    Parametric = 0
    Reference = 1


class IFCImportAction:
    Open = 0
    Link = 1
