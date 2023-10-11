# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Any, Awaitable, Dict, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    DeviceStatus,
    HubProductPlan,
    ListDevicesRequestOrderBy,
    ListHubsRequestOrderBy,
    ListNetworksRequestOrderBy,
    ListRoutesRequestOrderBy,
    NetworkNetworkType,
    CreateDeviceRequest,
    CreateDeviceResponse,
    CreateHubRequest,
    CreateNetworkRequest,
    CreateNetworkResponse,
    CreateRouteRequest,
    CreateRouteRequestDatabaseConfig,
    CreateRouteRequestRestConfig,
    CreateRouteRequestS3Config,
    Device,
    DeviceMessageFilters,
    GetDeviceCertificateResponse,
    GetDeviceMetricsResponse,
    GetHubCAResponse,
    GetHubMetricsResponse,
    Hub,
    HubTwinsGraphiteConfig,
    ListDevicesResponse,
    ListHubsResponse,
    ListNetworksResponse,
    ListRoutesResponse,
    ListTwinDocumentsResponse,
    Network,
    PatchTwinDocumentRequest,
    PutTwinDocumentRequest,
    RenewDeviceCertificateResponse,
    Route,
    RouteSummary,
    SetDeviceCertificateRequest,
    SetDeviceCertificateResponse,
    SetHubCARequest,
    TwinDocument,
    UpdateDeviceRequest,
    UpdateHubRequest,
    UpdateRouteRequest,
    UpdateRouteRequestDatabaseConfig,
    UpdateRouteRequestRestConfig,
    UpdateRouteRequestS3Config,
)
from .content import (
    HUB_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Device,
    unmarshal_Network,
    unmarshal_Hub,
    unmarshal_CreateDeviceResponse,
    unmarshal_CreateNetworkResponse,
    unmarshal_GetDeviceCertificateResponse,
    unmarshal_GetDeviceMetricsResponse,
    unmarshal_GetHubCAResponse,
    unmarshal_GetHubMetricsResponse,
    unmarshal_ListDevicesResponse,
    unmarshal_ListHubsResponse,
    unmarshal_ListNetworksResponse,
    unmarshal_ListRoutesResponse,
    unmarshal_ListTwinDocumentsResponse,
    unmarshal_RenewDeviceCertificateResponse,
    unmarshal_Route,
    unmarshal_SetDeviceCertificateResponse,
    unmarshal_TwinDocument,
    marshal_CreateDeviceRequest,
    marshal_CreateHubRequest,
    marshal_CreateNetworkRequest,
    marshal_CreateRouteRequest,
    marshal_PatchTwinDocumentRequest,
    marshal_PutTwinDocumentRequest,
    marshal_SetDeviceCertificateRequest,
    marshal_SetHubCARequest,
    marshal_UpdateDeviceRequest,
    marshal_UpdateHubRequest,
    marshal_UpdateRouteRequest,
)


class IotV1API(API):
    """
    This API allows you to manage IoT hubs and devices.
    """

    async def list_hubs(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListHubsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListHubsResponse:
        """
        List hubs.
        List all Hubs in the specified zone. By default, returned Hubs are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Hubs to return within a page. Maximum value is 100.
        :param order_by: Sort order of Hubs in the response.
        :param project_id: Only list Hubs of this Project ID.
        :param organization_id: Only list Hubs of this Organization ID.
        :param name: Hub name.
        :return: :class:`ListHubsResponse <ListHubsResponse>`

        Usage:
        ::

            result = await api.list_hubs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/hubs",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListHubsResponse(res.json())

    async def list_hubs_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListHubsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[Hub]:
        """
        List hubs.
        List all Hubs in the specified zone. By default, returned Hubs are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Hubs to return within a page. Maximum value is 100.
        :param order_by: Sort order of Hubs in the response.
        :param project_id: Only list Hubs of this Project ID.
        :param organization_id: Only list Hubs of this Organization ID.
        :param name: Hub name.
        :return: :class:`List[Hub] <List[Hub]>`

        Usage:
        ::

            result = await api.list_hubs_all()
        """

        return await fetch_all_pages_async(
            type=ListHubsResponse,
            key="hubs",
            fetcher=self.list_hubs,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
                "name": name,
            },
        )

    async def create_hub(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        product_plan: Optional[HubProductPlan] = None,
        disable_events: Optional[bool] = None,
        events_topic_prefix: Optional[str] = None,
        twins_graphite_config: Optional[HubTwinsGraphiteConfig] = None,
    ) -> Hub:
        """
        Create a hub.
        Create a new Hub in the targeted region, specifying its configuration including name and product plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Hub name (up to 255 characters).
        :param project_id: Project/Organization ID to filter for, only Hubs from this Project/Organization will be returned.
        :param product_plan: Hub product plan.
        :param disable_events: Disable Hub events.
        :param events_topic_prefix: Topic prefix (default '$SCW/events') of Hub events.
        :param twins_graphite_config: BETA - not implemented yet.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = await api.create_hub()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/hubs",
            body=marshal_CreateHubRequest(
                CreateHubRequest(
                    region=region,
                    name=name or random_name(prefix="hub"),
                    project_id=project_id,
                    product_plan=product_plan,
                    disable_events=disable_events,
                    events_topic_prefix=events_topic_prefix,
                    twins_graphite_config=twins_graphite_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    async def get_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
    ) -> Hub:
        """
        Get a hub.
        Retrieve information about an existing IoT Hub, specified by its Hub ID. Its full details, including name, status and endpoint, are returned in the response object.
        :param hub_id: Hub ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = await api.get_hub(
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    async def wait_for_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Hub, Union[bool, Awaitable[bool]]]] = None,
    ) -> Hub:
        """
        Get a hub.
        Retrieve information about an existing IoT Hub, specified by its Hub ID. Its full details, including name, status and endpoint, are returned in the response object.
        :param hub_id: Hub ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = await api.get_hub(
                hub_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in HUB_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_hub,
            options=options,
            args={
                "hub_id": hub_id,
                "region": region,
            },
        )

    async def update_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        product_plan: Optional[HubProductPlan] = None,
        disable_events: Optional[bool] = None,
        events_topic_prefix: Optional[str] = None,
        enable_device_auto_provisioning: Optional[bool] = None,
        twins_graphite_config: Optional[HubTwinsGraphiteConfig] = None,
    ) -> Hub:
        """
        Update a hub.
        Update the parameters of an existing IoT Hub, specified by its Hub ID.
        :param hub_id: ID of the Hub you want to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Hub name (up to 255 characters).
        :param product_plan: Hub product plan.
        :param disable_events: Disable Hub events.
        :param events_topic_prefix: Topic prefix of Hub events.
        :param enable_device_auto_provisioning: Enable device auto provisioning.
        :param twins_graphite_config: BETA - not implemented yet.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = await api.update_hub(
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "PATCH",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}",
            body=marshal_UpdateHubRequest(
                UpdateHubRequest(
                    hub_id=hub_id,
                    region=region,
                    name=name,
                    product_plan=product_plan,
                    disable_events=disable_events,
                    events_topic_prefix=events_topic_prefix,
                    enable_device_auto_provisioning=enable_device_auto_provisioning,
                    twins_graphite_config=twins_graphite_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    async def enable_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
    ) -> Hub:
        """
        Enable a hub.
        Enable an existing IoT Hub, specified by its Hub ID.
        :param hub_id: Hub ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = await api.enable_hub(
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/enable",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    async def disable_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
    ) -> Hub:
        """
        Disable a hub.
        Disable an existing IoT Hub, specified by its Hub ID.
        :param hub_id: Hub ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = await api.disable_hub(
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/disable",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    async def delete_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
        delete_devices: Optional[bool] = None,
    ) -> None:
        """
        Delete a hub.
        Delete an existing IoT Hub, specified by its Hub ID. Deleting a Hub is permanent, and cannot be undone.
        :param hub_id: Hub ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param delete_devices: Defines whether to force the deletion of devices added to this Hub or reject the operation.

        Usage:
        ::

            result = await api.delete_hub(
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}",
            params={
                "delete_devices": delete_devices,
            },
        )

        self._throw_on_error(res)

    async def get_hub_metrics(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
        start_date: Optional[datetime] = None,
    ) -> GetHubMetricsResponse:
        """
        Get a hub's metrics.
        Get the metrics of an existing IoT Hub, specified by its Hub ID.
        :param hub_id: Hub ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param start_date: Start date used to compute the best scale for returned metrics.
        :return: :class:`GetHubMetricsResponse <GetHubMetricsResponse>`
        :deprecated

        Usage:
        ::

            result = await api.get_hub_metrics(
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/metrics",
            params={
                "start_date": start_date,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetHubMetricsResponse(res.json())

    async def set_hub_ca(
        self,
        *,
        challenge_cert_pem: str,
        ca_cert_pem: str,
        hub_id: str,
        region: Optional[Region] = None,
    ) -> Hub:
        """
        Set the certificate authority of a hub.
        Set a particular PEM-encoded certificate, specified by the Hub ID.
        :param challenge_cert_pem: Challenge is a PEM-encoded certificate that acts as proof of possession of the CA. It must be signed by the CA, and have a Common Name equal to the Hub ID.
        :param ca_cert_pem: CA's PEM-encoded certificate.
        :param hub_id: Hub ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = await api.set_hub_ca(
                challenge_cert_pem="example",
                ca_cert_pem="example",
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/ca",
            body=marshal_SetHubCARequest(
                SetHubCARequest(
                    challenge_cert_pem=challenge_cert_pem,
                    ca_cert_pem=ca_cert_pem,
                    hub_id=hub_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    async def get_hub_ca(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
    ) -> GetHubCAResponse:
        """
        Get the certificate authority of a hub.
        Get information for a particular PEM-encoded certificate, specified by the Hub ID.
        :param hub_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`GetHubCAResponse <GetHubCAResponse>`

        Usage:
        ::

            result = await api.get_hub_ca(
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/ca",
        )

        self._throw_on_error(res)
        return unmarshal_GetHubCAResponse(res.json())

    async def list_devices(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDevicesRequestOrderBy] = None,
        name: Optional[str] = None,
        hub_id: Optional[str] = None,
        allow_insecure: Optional[bool] = None,
        status: Optional[DeviceStatus] = None,
    ) -> ListDevicesResponse:
        """
        List devices.
        List all devices in the specified region. By default, returned devices are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of devices to return within a page. Maximum value is 100.
        :param order_by: Ordering of requested devices.
        :param name: Name to filter for, only devices with this name will be returned.
        :param hub_id: Hub ID to filter for, only devices attached to this Hub will be returned.
        :param allow_insecure: Defines wheter to filter the allow_insecure flag.
        :param status: Device status (enabled, disabled, etc.).
        :return: :class:`ListDevicesResponse <ListDevicesResponse>`

        Usage:
        ::

            result = await api.list_devices()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/devices",
            params={
                "allow_insecure": allow_insecure,
                "hub_id": hub_id,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDevicesResponse(res.json())

    async def list_devices_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDevicesRequestOrderBy] = None,
        name: Optional[str] = None,
        hub_id: Optional[str] = None,
        allow_insecure: Optional[bool] = None,
        status: Optional[DeviceStatus] = None,
    ) -> List[Device]:
        """
        List devices.
        List all devices in the specified region. By default, returned devices are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of devices to return within a page. Maximum value is 100.
        :param order_by: Ordering of requested devices.
        :param name: Name to filter for, only devices with this name will be returned.
        :param hub_id: Hub ID to filter for, only devices attached to this Hub will be returned.
        :param allow_insecure: Defines wheter to filter the allow_insecure flag.
        :param status: Device status (enabled, disabled, etc.).
        :return: :class:`List[Device] <List[Device]>`

        Usage:
        ::

            result = await api.list_devices_all()
        """

        return await fetch_all_pages_async(
            type=ListDevicesResponse,
            key="devices",
            fetcher=self.list_devices,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
                "hub_id": hub_id,
                "allow_insecure": allow_insecure,
                "status": status,
            },
        )

    async def create_device(
        self,
        *,
        message_filters: DeviceMessageFilters,
        allow_multiple_connections: bool,
        allow_insecure: bool,
        hub_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> CreateDeviceResponse:
        """
        Add a device.
        Attach a device to a given Hub.
        :param message_filters: Filter-sets to authorize or deny the device to publish/subscribe to specific topics.
        :param allow_multiple_connections: Defines whether to allow multiple physical devices to connect with this device's credentials.
        :param allow_insecure: Defines whether to allow plain and server-authenticated SSL connections in addition to mutually-authenticated ones.
        :param hub_id: Hub ID of the device.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Device name.
        :param description: Device description.
        :return: :class:`CreateDeviceResponse <CreateDeviceResponse>`

        Usage:
        ::

            result = await api.create_device(
                message_filters=DeviceMessageFilters(),
                allow_multiple_connections=False,
                allow_insecure=False,
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/devices",
            body=marshal_CreateDeviceRequest(
                CreateDeviceRequest(
                    message_filters=message_filters,
                    allow_multiple_connections=allow_multiple_connections,
                    allow_insecure=allow_insecure,
                    hub_id=hub_id,
                    region=region,
                    name=name or random_name(prefix="device"),
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateDeviceResponse(res.json())

    async def get_device(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> Device:
        """
        Get a device.
        Retrieve information about an existing device, specified by its device ID. Its full details, including name, status and ID, are returned in the response object.
        :param device_id: Device ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Device <Device>`

        Usage:
        ::

            result = await api.get_device(
                device_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Device(res.json())

    async def update_device(
        self,
        *,
        message_filters: DeviceMessageFilters,
        device_id: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        allow_insecure: Optional[bool] = None,
        allow_multiple_connections: Optional[bool] = None,
        hub_id: Optional[str] = None,
    ) -> Device:
        """
        Update a device.
        Update the parameters of an existing device, specified by its device ID.
        :param message_filters: Filter-sets to restrict the topics the device can publish/subscribe to.
        :param device_id: Device ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Description for the device.
        :param allow_insecure: Defines whether to allow plain and server-authenticated SSL connections in addition to mutually-authenticated ones.
        :param allow_multiple_connections: Defines whether to allow multiple physical devices to connect with this device's credentials.
        :param hub_id: Change Hub for this device, additional fees may apply, see IoT Hub pricing.
        :return: :class:`Device <Device>`

        Usage:
        ::

            result = await api.update_device(
                message_filters=DeviceMessageFilters(),
                device_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "PATCH",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}",
            body=marshal_UpdateDeviceRequest(
                UpdateDeviceRequest(
                    message_filters=message_filters,
                    device_id=device_id,
                    region=region,
                    description=description,
                    allow_insecure=allow_insecure,
                    allow_multiple_connections=allow_multiple_connections,
                    hub_id=hub_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Device(res.json())

    async def enable_device(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> Device:
        """
        Enable a device.
        Enable a specific device, specified by its device ID.
        :param device_id: Device ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Device <Device>`

        Usage:
        ::

            result = await api.enable_device(
                device_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/enable",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Device(res.json())

    async def disable_device(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> Device:
        """
        Disable a device.
        Disable an existing device, specified by its device ID.
        :param device_id: Device ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Device <Device>`

        Usage:
        ::

            result = await api.disable_device(
                device_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/disable",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Device(res.json())

    async def renew_device_certificate(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> RenewDeviceCertificateResponse:
        """
        Renew a device certificate.
        Renew the certificate of an existing device, specified by its device ID.
        :param device_id: Device ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`RenewDeviceCertificateResponse <RenewDeviceCertificateResponse>`

        Usage:
        ::

            result = await api.renew_device_certificate(
                device_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/renew-certificate",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_RenewDeviceCertificateResponse(res.json())

    async def set_device_certificate(
        self,
        *,
        certificate_pem: str,
        device_id: str,
        region: Optional[Region] = None,
    ) -> SetDeviceCertificateResponse:
        """
        Set a custom certificate on a device.
        Switch the existing certificate of a given device with an EM-encoded custom certificate.
        :param certificate_pem: PEM-encoded custom certificate.
        :param device_id: Device ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SetDeviceCertificateResponse <SetDeviceCertificateResponse>`

        Usage:
        ::

            result = await api.set_device_certificate(
                certificate_pem="example",
                device_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "PUT",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/certificate",
            body=marshal_SetDeviceCertificateRequest(
                SetDeviceCertificateRequest(
                    certificate_pem=certificate_pem,
                    device_id=device_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetDeviceCertificateResponse(res.json())

    async def get_device_certificate(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> GetDeviceCertificateResponse:
        """
        Get a device's certificate.
        Get information for a particular PEM-encoded certificate, specified by the device ID. The response returns full details of the device, including its type of certificate.
        :param device_id: Device ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`GetDeviceCertificateResponse <GetDeviceCertificateResponse>`

        Usage:
        ::

            result = await api.get_device_certificate(
                device_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/certificate",
        )

        self._throw_on_error(res)
        return unmarshal_GetDeviceCertificateResponse(res.json())

    async def delete_device(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Remove a device.
        Remove a specific device from the specific Hub it is attached to.
        :param device_id: Device ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_device(
                device_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}",
        )

        self._throw_on_error(res)

    async def get_device_metrics(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
        start_date: Optional[datetime] = None,
    ) -> GetDeviceMetricsResponse:
        """
        Get a device's metrics.
        Get the metrics of an existing device, specified by its device ID.
        :param device_id: Device ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param start_date: Start date used to compute the best scale for the returned metrics.
        :return: :class:`GetDeviceMetricsResponse <GetDeviceMetricsResponse>`
        :deprecated

        Usage:
        ::

            result = await api.get_device_metrics(
                device_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/metrics",
            params={
                "start_date": start_date,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetDeviceMetricsResponse(res.json())

    async def list_routes(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        hub_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListRoutesResponse:
        """
        List routes.
        List all routes in the specified region. By default, returned routes are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of routes to return within a page. Maximum value is 100.
        :param order_by: Ordering of requested routes.
        :param hub_id: Hub ID to filter for.
        :param name: Route name to filter for.
        :return: :class:`ListRoutesResponse <ListRoutesResponse>`

        Usage:
        ::

            result = await api.list_routes()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/routes",
            params={
                "hub_id": hub_id,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRoutesResponse(res.json())

    async def list_routes_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        hub_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[RouteSummary]:
        """
        List routes.
        List all routes in the specified region. By default, returned routes are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of routes to return within a page. Maximum value is 100.
        :param order_by: Ordering of requested routes.
        :param hub_id: Hub ID to filter for.
        :param name: Route name to filter for.
        :return: :class:`List[RouteSummary] <List[RouteSummary]>`

        Usage:
        ::

            result = await api.list_routes_all()
        """

        return await fetch_all_pages_async(
            type=ListRoutesResponse,
            key="routes",
            fetcher=self.list_routes,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "hub_id": hub_id,
                "name": name,
            },
        )

    async def create_route(
        self,
        *,
        topic: str,
        hub_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        s3_config: Optional[CreateRouteRequestS3Config] = None,
        db_config: Optional[CreateRouteRequestDatabaseConfig] = None,
        rest_config: Optional[CreateRouteRequestRestConfig] = None,
    ) -> Route:
        """
        Create a route.
        Multiple kinds of routes can be created, such as:
        - Database Route
          Create a route that will record subscribed MQTT messages into your database.
          <b>You need to manage the database by yourself</b>.
        - REST Route.
          Create a route that will call a REST API on received subscribed MQTT messages.
        - S3 Routes.
          Create a route that will put subscribed MQTT messages into an S3 bucket.
          You need to create the bucket yourself and grant write access.
          Granting can be done with s3cmd (`s3cmd setacl s3://<my-bucket> --acl-grant=write:555c69c3-87d0-4bf8-80f1-99a2f757d031:555c69c3-87d0-4bf8-80f1-99a2f757d031`).
        :param topic: Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters.
        :param hub_id: Hub ID of the route.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Route name.
        :param s3_config: If creating S3 Route, S3-specific configuration fields.
        :param db_config: If creating Database Route, DB-specific configuration fields.
        :param rest_config: If creating Rest Route, Rest-specific configuration fields.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.create_route(
                topic="example",
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/routes",
            body=marshal_CreateRouteRequest(
                CreateRouteRequest(
                    topic=topic,
                    hub_id=hub_id,
                    region=region,
                    name=name or random_name(prefix="route"),
                    s3_config=s3_config,
                    db_config=db_config,
                    rest_config=rest_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def update_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        topic: Optional[str] = None,
        s3_config: Optional[UpdateRouteRequestS3Config] = None,
        db_config: Optional[UpdateRouteRequestDatabaseConfig] = None,
        rest_config: Optional[UpdateRouteRequestRestConfig] = None,
    ) -> Route:
        """
        Update a route.
        Update the parameters of an existing route, specified by its route ID.
        :param route_id: Route id.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Route name.
        :param topic: Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters.
        :param s3_config: When updating S3 Route, S3-specific configuration fields.
        :param db_config: When updating Database Route, DB-specific configuration fields.
        :param rest_config: When updating Rest Route, Rest-specific configuration fields.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.update_route(
                route_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "PATCH",
            f"/iot/v1/regions/{param_region}/routes/{param_route_id}",
            body=marshal_UpdateRouteRequest(
                UpdateRouteRequest(
                    route_id=route_id,
                    region=region,
                    name=name,
                    topic=topic,
                    s3_config=s3_config,
                    db_config=db_config,
                    rest_config=rest_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def get_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
    ) -> Route:
        """
        Get a route.
        Get information for a particular route, specified by the route ID. The response returns full details of the route, including its type, the topic it subscribes to and its configuration.
        :param route_id: Route ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.get_route(
                route_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def delete_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a route.
        Delete an existing route, specified by its route ID. Deleting a route is permanent, and cannot be undone.
        :param route_id: Route ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_route(
                route_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/routes/{param_route_id}",
        )

        self._throw_on_error(res)

    async def list_networks(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNetworksRequestOrderBy] = None,
        name: Optional[str] = None,
        hub_id: Optional[str] = None,
        topic_prefix: Optional[str] = None,
    ) -> ListNetworksResponse:
        """
        List the networks.
        List the networks.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of networks to return. The maximum value is 100.
        :param order_by: Ordering of requested routes.
        :param name: Network name to filter for.
        :param hub_id: Hub ID to filter for.
        :param topic_prefix: Topic prefix to filter for.
        :return: :class:`ListNetworksResponse <ListNetworksResponse>`

        Usage:
        ::

            result = await api.list_networks()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/networks",
            params={
                "hub_id": hub_id,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "topic_prefix": topic_prefix,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNetworksResponse(res.json())

    async def list_networks_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNetworksRequestOrderBy] = None,
        name: Optional[str] = None,
        hub_id: Optional[str] = None,
        topic_prefix: Optional[str] = None,
    ) -> List[Network]:
        """
        List the networks.
        List the networks.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of networks to return. The maximum value is 100.
        :param order_by: Ordering of requested routes.
        :param name: Network name to filter for.
        :param hub_id: Hub ID to filter for.
        :param topic_prefix: Topic prefix to filter for.
        :return: :class:`List[Network] <List[Network]>`

        Usage:
        ::

            result = await api.list_networks_all()
        """

        return await fetch_all_pages_async(
            type=ListNetworksResponse,
            key="networks",
            fetcher=self.list_networks,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
                "hub_id": hub_id,
                "topic_prefix": topic_prefix,
            },
        )

    async def create_network(
        self,
        *,
        topic_prefix: str,
        hub_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        type_: Optional[NetworkNetworkType] = None,
    ) -> CreateNetworkResponse:
        """
        Create a new network.
        Create a new network for an existing hub.  Beside the default network, you can add networks for different data providers. Possible network types are Sigfox and REST.
        :param topic_prefix: Topic prefix for the Network.
        :param hub_id: Hub ID to connect the Network to.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Network name.
        :param type_: Type of network to connect with.
        :return: :class:`CreateNetworkResponse <CreateNetworkResponse>`

        Usage:
        ::

            result = await api.create_network(
                topic_prefix="example",
                hub_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/networks",
            body=marshal_CreateNetworkRequest(
                CreateNetworkRequest(
                    topic_prefix=topic_prefix,
                    hub_id=hub_id,
                    region=region,
                    name=name or random_name(prefix="network"),
                    type_=type_,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateNetworkResponse(res.json())

    async def get_network(
        self,
        *,
        network_id: str,
        region: Optional[Region] = None,
    ) -> Network:
        """
        Retrieve a specific network.
        Retrieve an existing network, specified by its network ID.  The response returns full details of the network, including its type, the topic prefix and its endpoint.
        :param network_id: Network ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Network <Network>`

        Usage:
        ::

            result = await api.get_network(
                network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_network_id = validate_path_param("network_id", network_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/networks/{param_network_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Network(res.json())

    async def delete_network(
        self,
        *,
        network_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a Network.
        Delete an existing network, specified by its network ID. Deleting a network is permanent, and cannot be undone.
        :param network_id: Network ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_network(
                network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_network_id = validate_path_param("network_id", network_id)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/networks/{param_network_id}",
        )

        self._throw_on_error(res)

    async def get_twin_document(
        self,
        *,
        document_name: str,
        twin_id: str,
        region: Optional[Region] = None,
    ) -> TwinDocument:
        """
        BETA - Get a Cloud Twin Document.
        BETA - Get a Cloud Twin Document.
        :param document_name: Name of the document.
        :param twin_id: Twin ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`TwinDocument <TwinDocument>`

        Usage:
        ::

            result = await api.get_twin_document(
                document_name="example",
                twin_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)
        param_document_name = validate_path_param("document_name", document_name)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}/documents/{param_document_name}",
        )

        self._throw_on_error(res)
        return unmarshal_TwinDocument(res.json())

    async def put_twin_document(
        self,
        *,
        document_name: str,
        twin_id: str,
        region: Optional[Region] = None,
        version: Optional[int] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> TwinDocument:
        """
        BETA - Update a Cloud Twin Document.
        BETA - Update a Cloud Twin Document.
        :param document_name: Name of the document.
        :param twin_id: Twin ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param version: If set, ensures that the current version of the document matches before persisting the update.
        :param data: New data that will replace the contents of the document.
        :return: :class:`TwinDocument <TwinDocument>`

        Usage:
        ::

            result = await api.put_twin_document(
                document_name="example",
                twin_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)
        param_document_name = validate_path_param("document_name", document_name)

        res = self._request(
            "PUT",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}/documents/{param_document_name}",
            body=marshal_PutTwinDocumentRequest(
                PutTwinDocumentRequest(
                    document_name=document_name,
                    twin_id=twin_id,
                    region=region,
                    version=version,
                    data=data,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TwinDocument(res.json())

    async def patch_twin_document(
        self,
        *,
        document_name: str,
        twin_id: str,
        region: Optional[Region] = None,
        version: Optional[int] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> TwinDocument:
        """
        BETA - Patch a Cloud Twin Document.
        BETA - Patch a Cloud Twin Document.
        :param document_name: Name of the document.
        :param twin_id: Twin ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param version: If set, ensures that the current version of the document matches before persisting the update.
        :param data: A json data that will be applied on the document's current data.
        Patching rules:
        * The patch goes recursively through the patch objects.
        * If the patch object property is null, it is removed from the final object.
        * If the patch object property is a value (number, strings, bool, arrays), it is replaced.
        * If the patch object property is an object, the previous rules will be applied recursively on it.
        :return: :class:`TwinDocument <TwinDocument>`

        Usage:
        ::

            result = await api.patch_twin_document(
                document_name="example",
                twin_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)
        param_document_name = validate_path_param("document_name", document_name)

        res = self._request(
            "PATCH",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}/documents/{param_document_name}",
            body=marshal_PatchTwinDocumentRequest(
                PatchTwinDocumentRequest(
                    document_name=document_name,
                    twin_id=twin_id,
                    region=region,
                    version=version,
                    data=data,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TwinDocument(res.json())

    async def delete_twin_document(
        self,
        *,
        document_name: str,
        twin_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        BETA - Delete a Cloud Twin Document.
        BETA - Delete a Cloud Twin Document.
        :param document_name: Name of the document.
        :param twin_id: Twin ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_twin_document(
                document_name="example",
                twin_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)
        param_document_name = validate_path_param("document_name", document_name)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}/documents/{param_document_name}",
        )

        self._throw_on_error(res)

    async def list_twin_documents(
        self,
        *,
        twin_id: str,
        region: Optional[Region] = None,
    ) -> ListTwinDocumentsResponse:
        """
        BETA - List the documents of a Cloud Twin.
        BETA - List the documents of a Cloud Twin.
        :param twin_id: Twin ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ListTwinDocumentsResponse <ListTwinDocumentsResponse>`

        Usage:
        ::

            result = await api.list_twin_documents(
                twin_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}",
        )

        self._throw_on_error(res)
        return unmarshal_ListTwinDocumentsResponse(res.json())

    async def delete_twin_documents(
        self,
        *,
        twin_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        BETA - Delete all the documents of a Cloud Twin.
        BETA - Delete all the documents of a Cloud Twin.
        :param twin_id: Twin ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_twin_documents(
                twin_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}",
        )

        self._throw_on_error(res)
