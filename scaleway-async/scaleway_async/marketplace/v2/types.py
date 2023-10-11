# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListImagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLocalImagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVersionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class LocalImageType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    INSTANCE_LOCAL = "instance_local"
    INSTANCE_SBS = "instance_sbs"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Category:
    description: str

    name: str

    id: str


@dataclass
class Image:
    label: str
    """
    Typically an identifier for a distribution (ex. "ubuntu_focal").
    """

    categories: List[str]
    """
    List of categories this image belongs to.
    """

    logo: str
    """
    URL of this image's logo.
    """

    description: str
    """
    Text description of this image.
    """

    name: str
    """
    Name of the image.
    """

    id: str
    """
    UUID of this image.
    """

    created_at: Optional[datetime]
    """
    Creation date of this image.
    """

    updated_at: Optional[datetime]
    """
    Date of the last modification of this image.
    """

    valid_until: Optional[datetime]
    """
    Expiration date of this image.
    """


@dataclass
class LocalImage:
    type_: LocalImageType
    """
    Type of this local image.
    """

    label: str
    """
    Image label this image belongs to.
    """

    zone: Zone
    """
    Availability Zone where this local image is available.
    """

    arch: str
    """
    Supported architecture for this local image.
    """

    compatible_commercial_types: List[str]
    """
    List of all commercial types that are compatible with this local image.
    """

    id: str
    """
    Version you will typically use to define an image in an API call.
    """


@dataclass
class Version:
    name: str
    """
    Name of this version.
    """

    id: str
    """
    UUID of this version.
    """

    created_at: Optional[datetime]
    """
    Creation date of this image version.
    """

    updated_at: Optional[datetime]
    """
    Date of the last modification of this version.
    """

    published_at: Optional[datetime]
    """
    Date this version was officially published.
    """


@dataclass
class GetCategoryRequest:
    category_id: str


@dataclass
class GetImageRequest:
    image_id: str
    """
    Display the image name.
    """


@dataclass
class GetLocalImageRequest:
    local_image_id: str


@dataclass
class GetVersionRequest:
    version_id: str


@dataclass
class ListCategoriesRequest:
    page_size: Optional[int]

    page: Optional[int]


@dataclass
class ListCategoriesResponse:
    total_count: int

    categories: List[Category]


@dataclass
class ListImagesRequest:
    include_eol: bool
    """
    Choose to include end-of-life images.
    """

    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to display.
    """

    order_by: Optional[ListImagesRequestOrderBy]
    """
    Ordering to use.
    """

    arch: Optional[str]
    """
    Choose for which machine architecture to return images.
    """

    category: Optional[str]
    """
    Choose the category of images to get.
    """


@dataclass
class ListImagesResponse:
    total_count: int

    images: List[Image]


@dataclass
class ListLocalImagesRequest:
    page_size: Optional[int]

    page: Optional[int]

    order_by: Optional[ListLocalImagesRequestOrderBy]

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    type_: Optional[LocalImageType]

    image_id: Optional[str]

    version_id: Optional[str]

    image_label: Optional[str]


@dataclass
class ListLocalImagesResponse:
    total_count: int

    local_images: List[LocalImage]


@dataclass
class ListVersionsRequest:
    image_id: str

    page_size: Optional[int]

    page: Optional[int]

    order_by: Optional[ListVersionsRequestOrderBy]


@dataclass
class ListVersionsResponse:
    total_count: int

    versions: List[Version]
