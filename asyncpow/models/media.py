"""
 AsyncPOW - https://github.com/totaldebug/asyncpow

 Copyright (c) 2024 Steven Marks, Total Debug

 Permission is hereby granted, free of charge, to any person obtaining a copy of
 this software and associated documentation files (the "Software"), to deal in
 the Software without restriction, including without limitation the rights to
 use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 the Software, and to permit persons to whom the Software is furnished to do so,
 subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 """

from dataclasses import dataclass
from enum import Enum

from asyncpow.models.common import PageInfoModel, UserModel


class MediaFilterOptions(Enum):
    """
    Enum class for media filter options.
    """

    ALL = "all"
    AVAILABLE = "available"
    PARTIAL = "partial"
    ALLAVAILABLE = "allavailable"
    PENDING = "pending"
    PROCESSING = "processing"


class MediaStatusOptions(Enum):
    """
    Enum class representing media status options.
    """

    AVAILABLE = "available"
    PARTIAL = "partial"
    PENDING = "pending"
    PROCESSING = "processing"
    UNKNOWN = "unknown"


@dataclass
class MediaRequestModel:
    """
    Data class representing a media request model.
    """

    id: int
    status: int
    media: dict
    createdAt: str
    updatedAt: str
    requestedBy: UserModel
    modifiedBy: list[UserModel]
    is4k: bool
    serverId: int
    profileId: int
    rootFolder: str


@dataclass
class MediaInfoModel:
    """
    Data class representing media information model.
    """

    id: int
    tmdbId: int
    tvdbId: int
    status: int
    requests: MediaRequestModel
    createdAt: str
    updatedAt: str


@dataclass
class MediaModel:
    """
    Data class representing a media model.
    """

    pageInfo: PageInfoModel
    results: MediaInfoModel


@dataclass
class MediaModel2:
    """
    Data class representing a secondary media model.
    """

    id: int
    tmdbId: int
    tvdbId: int
    status: int
    requests: list[MediaInfoModel]
