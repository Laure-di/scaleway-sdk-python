# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListPinsRequestOrderBy,
    ListVolumesRequestOrderBy,
    PinStatus,
    CreatePinByCIDRequest,
    CreatePinByURLRequest,
    CreateVolumeRequest,
    ListPinsResponse,
    ListVolumesResponse,
    Pin,
    PinOptions,
    ReplacePinRequest,
    ReplacePinResponse,
    UpdateVolumeRequest,
    Volume,
)
from .content import (
    PIN_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Pin,
    unmarshal_Volume,
    unmarshal_ListPinsResponse,
    unmarshal_ListVolumesResponse,
    unmarshal_ReplacePinResponse,
    marshal_CreatePinByCIDRequest,
    marshal_CreatePinByURLRequest,
    marshal_CreateVolumeRequest,
    marshal_ReplacePinRequest,
    marshal_UpdateVolumeRequest,
)


class IpfsV1Alpha1API(API):
    """
    IPFS Pinning service API.
    """

    async def create_volume(
        self,
        *,
        name: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> Volume:
        """
        Create a new volume.
        Create a new volume from a Project ID. Volume is identified by an ID and used to host pin references.
        Volume is personal (at least to your organization) even if IPFS blocks and CID are available to anyone.
        Should be the first command you made because every pin must be attached to a volume.
        :param name: Volume name.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = await api.create_volume(
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/ipfs/v1alpha1/regions/{param_region}/volumes",
            body=marshal_CreateVolumeRequest(
                CreateVolumeRequest(
                    name=name,
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    async def get_volume(
        self,
        *,
        volume_id: str,
        region: Optional[Region] = None,
    ) -> Volume:
        """
        Get information about a volume.
        Retrieve information about a specific volume.
        :param volume_id: Volume ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = await api.get_volume(
                volume_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "GET",
            f"/ipfs/v1alpha1/regions/{param_region}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    async def list_volumes(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListVolumesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListVolumesResponse:
        """
        List all volumes by a Project ID.
        Retrieve information about all volumes from a Project ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID, only volumes belonging to this project will be listed.
        :param order_by: Sort the order of the returned volumes.
        :param page: Page number.
        :param page_size: Maximum number of volumes to return per page.
        :return: :class:`ListVolumesResponse <ListVolumesResponse>`

        Usage:
        ::

            result = await api.list_volumes()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/ipfs/v1alpha1/regions/{param_region}/volumes",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVolumesResponse(res.json())

    async def list_volumes_all(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListVolumesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Volume]:
        """
        List all volumes by a Project ID.
        Retrieve information about all volumes from a Project ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID, only volumes belonging to this project will be listed.
        :param order_by: Sort the order of the returned volumes.
        :param page: Page number.
        :param page_size: Maximum number of volumes to return per page.
        :return: :class:`List[Volume] <List[Volume]>`

        Usage:
        ::

            result = await api.list_volumes_all()
        """

        return await fetch_all_pages_async(
            type=ListVolumesResponse,
            key="volumes",
            fetcher=self.list_volumes,
            args={
                "region": region,
                "project_id": project_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def update_volume(
        self,
        *,
        volume_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Volume:
        """
        Update volume information.
        Update volume information (tag, name...).
        :param volume_id: Volume ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Volume name.
        :param tags: Tags of the volume.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = await api.update_volume(
                volume_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "PATCH",
            f"/ipfs/v1alpha1/regions/{param_region}/volumes/{param_volume_id}",
            body=marshal_UpdateVolumeRequest(
                UpdateVolumeRequest(
                    volume_id=volume_id,
                    region=region,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    async def delete_volume(
        self,
        *,
        volume_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete an existing volume.
        Delete a volume by its ID and every pin attached to this volume. This process can take a while to conclude, depending on the size of your pinned content.
        :param volume_id: Volume ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_volume(
                volume_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "DELETE",
            f"/ipfs/v1alpha1/regions/{param_region}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)

    async def create_pin_by_url(
        self,
        *,
        pin_options: PinOptions,
        url: str,
        volume_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
    ) -> Pin:
        """
        Create a pin by URL.
        Will fetch and store the content pointed by the provided URL. The content must be available on the public IPFS network.
        The content (IPFS blocks) will be host by the pinning service until pin deletion.
        From that point, any other IPFS peer can fetch and host your content: Make sure to pin public or encrypted content.
        Many pin requests (from different users) can target the same CID.
        A pin is defined by its ID (UUID), its status (queued, pinning, pinned or failed) and target CID.
        :param pin_options: Pin options.
        :param url: URL containing the content you want to pin.
        :param volume_id: Volume ID on which you want to pin your content.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Pin name.
        :return: :class:`Pin <Pin>`

        Usage:
        ::

            result = await api.create_pin_by_url(
                pin_options=PinOptions(),
                url="example",
                volume_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/ipfs/v1alpha1/regions/{param_region}/pins/create-by-url",
            body=marshal_CreatePinByURLRequest(
                CreatePinByURLRequest(
                    pin_options=pin_options,
                    url=url,
                    volume_id=volume_id,
                    region=region,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Pin(res.json())

    async def create_pin_by_cid(
        self,
        *,
        pin_options: PinOptions,
        cid: str,
        volume_id: str,
        region: Optional[Region] = None,
        origins: Optional[List[str]] = None,
        name: Optional[str] = None,
    ) -> Pin:
        """
        Create a pin by CID.
        Will fetch and store the content pointed by the provided CID. The content must be available on the public IPFS network.
        The content (IPFS blocks) will be host by the pinning service until pin deletion.
        From that point, any other IPFS peer can fetch and host your content: Make sure to pin public or encrypted content.
        Many pin requests (from different users) can target the same CID.
        A pin is defined by its ID (UUID), its status (queued, pinning, pinned or failed) and target CID.
        :param pin_options: Pin options.
        :param cid: CID containing the content you want to pin.
        :param volume_id: Volume ID on which you want to pin your content.
        :param region: Region to target. If none is passed will use default region from the config.
        :param origins: Node containing the content you want to pin.
        :param name: Pin name.
        :return: :class:`Pin <Pin>`

        Usage:
        ::

            result = await api.create_pin_by_cid(
                pin_options=PinOptions(),
                cid="example",
                volume_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/ipfs/v1alpha1/regions/{param_region}/pins/create-by-cid",
            body=marshal_CreatePinByCIDRequest(
                CreatePinByCIDRequest(
                    pin_options=pin_options,
                    cid=cid,
                    volume_id=volume_id,
                    region=region,
                    origins=origins,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Pin(res.json())

    async def replace_pin(
        self,
        *,
        pin_options: PinOptions,
        cid: str,
        volume_id: str,
        pin_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        origins: Optional[List[str]] = None,
    ) -> ReplacePinResponse:
        """
        :param pin_options: Pin options.
        :param cid: New CID you want to pin in place of the old one.
        :param volume_id: Volume ID.
        :param pin_id: Pin ID whose information you wish to replace.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: New name to replace.
        :param origins: Node containing the content you want to pin.
        :return: :class:`ReplacePinResponse <ReplacePinResponse>`

        Usage:
        ::

            result = await api.replace_pin(
                pin_options=PinOptions(),
                cid="example",
                volume_id="example",
                pin_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_pin_id = validate_path_param("pin_id", pin_id)

        res = self._request(
            "POST",
            f"/ipfs/v1alpha1/regions/{param_region}/pins/{param_pin_id}/replace",
            body=marshal_ReplacePinRequest(
                ReplacePinRequest(
                    pin_options=pin_options,
                    cid=cid,
                    volume_id=volume_id,
                    pin_id=pin_id,
                    region=region,
                    name=name,
                    origins=origins,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ReplacePinResponse(res.json())

    async def get_pin(
        self,
        *,
        volume_id: str,
        pin_id: str,
        region: Optional[Region] = None,
    ) -> Pin:
        """
        Get pin information.
        Retrieve information about the provided **pin ID**, such as status, last modification, and CID.
        :param volume_id: Volume ID.
        :param pin_id: Pin ID of which you want to obtain information.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Pin <Pin>`

        Usage:
        ::

            result = await api.get_pin(
                volume_id="example",
                pin_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_pin_id = validate_path_param("pin_id", pin_id)

        res = self._request(
            "GET",
            f"/ipfs/v1alpha1/regions/{param_region}/pins/{param_pin_id}",
            params={
                "volume_id": volume_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Pin(res.json())

    async def wait_for_pin(
        self,
        *,
        volume_id: str,
        pin_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Pin, Union[bool, Awaitable[bool]]]] = None,
    ) -> Pin:
        """
        Get pin information.
        Retrieve information about the provided **pin ID**, such as status, last modification, and CID.
        :param volume_id: Volume ID.
        :param pin_id: Pin ID of which you want to obtain information.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Pin <Pin>`

        Usage:
        ::

            result = await api.get_pin(
                volume_id="example",
                pin_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in PIN_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_pin,
            options=options,
            args={
                "volume_id": volume_id,
                "pin_id": pin_id,
                "region": region,
            },
        )

    async def list_pins(
        self,
        *,
        volume_id: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        order_by: Optional[ListPinsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[PinStatus] = None,
    ) -> ListPinsResponse:
        """
        List all pins within a volume.
        Retrieve information about all pins within a volume.
        :param volume_id: Volume ID of which you want to list the pins.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID.
        :param organization_id: Organization ID.
        :param order_by: Sort order of the returned Volume.
        :param page: Page number.
        :param page_size: Maximum number of volumes to return per page.
        :param status: List pins by status.
        :return: :class:`ListPinsResponse <ListPinsResponse>`

        Usage:
        ::

            result = await api.list_pins(
                volume_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/ipfs/v1alpha1/regions/{param_region}/pins",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
                "volume_id": volume_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPinsResponse(res.json())

    async def list_pins_all(
        self,
        *,
        volume_id: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        order_by: Optional[ListPinsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[PinStatus] = None,
    ) -> List[Pin]:
        """
        List all pins within a volume.
        Retrieve information about all pins within a volume.
        :param volume_id: Volume ID of which you want to list the pins.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID.
        :param organization_id: Organization ID.
        :param order_by: Sort order of the returned Volume.
        :param page: Page number.
        :param page_size: Maximum number of volumes to return per page.
        :param status: List pins by status.
        :return: :class:`List[Pin] <List[Pin]>`

        Usage:
        ::

            result = await api.list_pins_all(
                volume_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListPinsResponse,
            key="pins",
            fetcher=self.list_pins,
            args={
                "volume_id": volume_id,
                "region": region,
                "project_id": project_id,
                "organization_id": organization_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "status": status,
            },
        )

    async def delete_pin(
        self,
        *,
        volume_id: str,
        pin_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Create an unpin request.
        An unpin request means that you no longer own the content.
        This content can therefore be removed and no longer provided on the IPFS network.
        :param volume_id: Volume ID.
        :param pin_id: Pin ID you want to remove from the volume.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_pin(
                volume_id="example",
                pin_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_pin_id = validate_path_param("pin_id", pin_id)

        res = self._request(
            "DELETE",
            f"/ipfs/v1alpha1/regions/{param_region}/pins/{param_pin_id}",
            params={
                "volume_id": volume_id,
            },
        )

        self._throw_on_error(res)
