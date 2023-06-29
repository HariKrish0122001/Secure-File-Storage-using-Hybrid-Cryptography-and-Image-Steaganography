from io import BufferedReader
from typing import Optional, TypedDict
from zcatalyst.types import (
    ICatalystFile,
    ICatalystFolder,
    ICatalystGResponse,
    ICatalystProject,
    ICatalystSysUser
)


class ICatalystFolderDetails(ICatalystFolder):
    created_time: Optional[str]
    created_by: Optional[ICatalystSysUser]
    project_details: Optional[ICatalystProject]


class ICatalystFileDetails(ICatalystFile, ICatalystGResponse):
    pass


class ICatalystFileInput(TypedDict):
    code: BufferedReader
    name: str
