# pylint: disable=invalid-name
from zcatalyst.types import (
    ICatalystCron,
    ICatalystGResponse
)


class ICatalystCronReq(ICatalystCron):
    pass


class ICatalystCronUpdateReq(ICatalystCron):
    id: str


class ICatalystCronRes(ICatalystCron, ICatalystGResponse):
    id: str
    success_count: int
    failure_count: int
