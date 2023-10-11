# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ForwardPortAlgorithm,
    ListAclRequestOrderBy,
    ListBackendsRequestOrderBy,
    ListCertificatesRequestOrderBy,
    ListFrontendsRequestOrderBy,
    ListLbsRequestOrderBy,
    ListPrivateNetworksRequestOrderBy,
    ListRoutesRequestOrderBy,
    ListSubscriberRequestOrderBy,
    OnMarkedDownAction,
    Protocol,
    ProxyProtocol,
    SSLCompatibilityLevel,
    StickySessionsType,
    Acl,
    AclAction,
    AclMatch,
    AclSpec,
    AddBackendServersRequest,
    AttachPrivateNetworkRequest,
    Backend,
    BackendServerStats,
    Certificate,
    CreateAclRequest,
    CreateBackendRequest,
    CreateCertificateRequest,
    CreateCertificateRequestCustomCertificate,
    CreateCertificateRequestLetsencryptConfig,
    CreateFrontendRequest,
    CreateIpRequest,
    CreateLbRequest,
    CreateRouteRequest,
    CreateSubscriberRequest,
    Frontend,
    HealthCheck,
    HealthCheckHttpConfig,
    HealthCheckHttpsConfig,
    HealthCheckLdapConfig,
    HealthCheckMysqlConfig,
    HealthCheckPgsqlConfig,
    HealthCheckRedisConfig,
    HealthCheckTcpConfig,
    Ip,
    Lb,
    LbStats,
    LbType,
    ListAclResponse,
    ListBackendStatsResponse,
    ListBackendsResponse,
    ListCertificatesResponse,
    ListFrontendsResponse,
    ListIpsResponse,
    ListLbPrivateNetworksResponse,
    ListLbTypesResponse,
    ListLbsResponse,
    ListRoutesResponse,
    ListSubscriberResponse,
    MigrateLbRequest,
    PrivateNetwork,
    PrivateNetworkDHCPConfig,
    PrivateNetworkIpamConfig,
    PrivateNetworkStaticConfig,
    RemoveBackendServersRequest,
    Route,
    RouteMatch,
    SetAclsResponse,
    SetBackendServersRequest,
    SubscribeToLbRequest,
    Subscriber,
    SubscriberEmailConfig,
    SubscriberWebhookConfig,
    UpdateAclRequest,
    UpdateBackendRequest,
    UpdateCertificateRequest,
    UpdateFrontendRequest,
    UpdateHealthCheckRequest,
    UpdateIpRequest,
    UpdateLbRequest,
    UpdateRouteRequest,
    UpdateSubscriberRequest,
    ZonedApiAddBackendServersRequest,
    ZonedApiAttachPrivateNetworkRequest,
    ZonedApiCreateAclRequest,
    ZonedApiCreateBackendRequest,
    ZonedApiCreateCertificateRequest,
    ZonedApiCreateFrontendRequest,
    ZonedApiCreateIpRequest,
    ZonedApiCreateLbRequest,
    ZonedApiCreateRouteRequest,
    ZonedApiCreateSubscriberRequest,
    ZonedApiMigrateLbRequest,
    ZonedApiRemoveBackendServersRequest,
    ZonedApiSetAclsRequest,
    ZonedApiSetBackendServersRequest,
    ZonedApiSubscribeToLbRequest,
    ZonedApiUpdateAclRequest,
    ZonedApiUpdateBackendRequest,
    ZonedApiUpdateCertificateRequest,
    ZonedApiUpdateFrontendRequest,
    ZonedApiUpdateHealthCheckRequest,
    ZonedApiUpdateIpRequest,
    ZonedApiUpdateLbRequest,
    ZonedApiUpdateRouteRequest,
    ZonedApiUpdateSubscriberRequest,
)
from .content import (
    CERTIFICATE_TRANSIENT_STATUSES,
    LB_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Ip,
    unmarshal_Subscriber,
    unmarshal_HealthCheck,
    unmarshal_Lb,
    unmarshal_Backend,
    unmarshal_Certificate,
    unmarshal_Frontend,
    unmarshal_Acl,
    unmarshal_PrivateNetwork,
    unmarshal_Route,
    unmarshal_LbStats,
    unmarshal_ListAclResponse,
    unmarshal_ListBackendStatsResponse,
    unmarshal_ListBackendsResponse,
    unmarshal_ListCertificatesResponse,
    unmarshal_ListFrontendsResponse,
    unmarshal_ListIpsResponse,
    unmarshal_ListLbPrivateNetworksResponse,
    unmarshal_ListLbTypesResponse,
    unmarshal_ListLbsResponse,
    unmarshal_ListRoutesResponse,
    unmarshal_ListSubscriberResponse,
    unmarshal_SetAclsResponse,
    marshal_AddBackendServersRequest,
    marshal_AttachPrivateNetworkRequest,
    marshal_CreateAclRequest,
    marshal_CreateBackendRequest,
    marshal_CreateCertificateRequest,
    marshal_CreateFrontendRequest,
    marshal_CreateIpRequest,
    marshal_CreateLbRequest,
    marshal_CreateRouteRequest,
    marshal_CreateSubscriberRequest,
    marshal_MigrateLbRequest,
    marshal_RemoveBackendServersRequest,
    marshal_SetBackendServersRequest,
    marshal_SubscribeToLbRequest,
    marshal_UpdateAclRequest,
    marshal_UpdateBackendRequest,
    marshal_UpdateCertificateRequest,
    marshal_UpdateFrontendRequest,
    marshal_UpdateHealthCheckRequest,
    marshal_UpdateIpRequest,
    marshal_UpdateLbRequest,
    marshal_UpdateRouteRequest,
    marshal_UpdateSubscriberRequest,
    marshal_ZonedApiAddBackendServersRequest,
    marshal_ZonedApiAttachPrivateNetworkRequest,
    marshal_ZonedApiCreateAclRequest,
    marshal_ZonedApiCreateBackendRequest,
    marshal_ZonedApiCreateCertificateRequest,
    marshal_ZonedApiCreateFrontendRequest,
    marshal_ZonedApiCreateIpRequest,
    marshal_ZonedApiCreateLbRequest,
    marshal_ZonedApiCreateRouteRequest,
    marshal_ZonedApiCreateSubscriberRequest,
    marshal_ZonedApiMigrateLbRequest,
    marshal_ZonedApiRemoveBackendServersRequest,
    marshal_ZonedApiSetAclsRequest,
    marshal_ZonedApiSetBackendServersRequest,
    marshal_ZonedApiSubscribeToLbRequest,
    marshal_ZonedApiUpdateAclRequest,
    marshal_ZonedApiUpdateBackendRequest,
    marshal_ZonedApiUpdateCertificateRequest,
    marshal_ZonedApiUpdateFrontendRequest,
    marshal_ZonedApiUpdateHealthCheckRequest,
    marshal_ZonedApiUpdateIpRequest,
    marshal_ZonedApiUpdateLbRequest,
    marshal_ZonedApiUpdateRouteRequest,
    marshal_ZonedApiUpdateSubscriberRequest,
)


class LbV1ZonedAPI(API):
    """
    This API allows you to manage your Scaleway Load Balancer services.
    """

    def list_lbs(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: Optional[ListLbsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListLbsResponse:
        """
        List Load Balancers.
        List all Load Balancers in the specified zone, for a Scaleway Organization or Scaleway Project. By default, the Load Balancers returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Load Balancer name to filter for.
        :param order_by: Sort order of Load Balancers in the response.
        :param page_size: Number of Load Balancers to return.
        :param page: Page number to return, from the paginated results.
        :param organization_id: Organization ID to filter for, only Load Balancers from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancers from this Project will be returned.
        :return: :class:`ListLbsResponse <ListLbsResponse>`

        Usage:
        ::

            result = api.list_lbs()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs",
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
        return unmarshal_ListLbsResponse(res.json())

    def list_lbs_all(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: Optional[ListLbsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Lb]:
        """
        List Load Balancers.
        List all Load Balancers in the specified zone, for a Scaleway Organization or Scaleway Project. By default, the Load Balancers returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Load Balancer name to filter for.
        :param order_by: Sort order of Load Balancers in the response.
        :param page_size: Number of Load Balancers to return.
        :param page: Page number to return, from the paginated results.
        :param organization_id: Organization ID to filter for, only Load Balancers from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancers from this Project will be returned.
        :return: :class:`List[Lb] <List[Lb]>`

        Usage:
        ::

            result = api.list_lbs_all()
        """

        return fetch_all_pages(
            type=ListLbsResponse,
            key="lbs",
            fetcher=self.list_lbs,
            args={
                "zone": zone,
                "name": name,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def create_lb(
        self,
        *,
        type_: str,
        description: str,
        zone: Optional[Zone] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        ip_id: Optional[str] = None,
        assign_flexible_ip: Optional[bool] = None,
        tags: Optional[List[str]] = None,
        ssl_compatibility_level: Optional[SSLCompatibilityLevel] = None,
    ) -> Lb:
        """
        Create a Load Balancer.
        Create a new Load Balancer. Note that the Load Balancer will be created without frontends or backends; these must be created separately via the dedicated endpoints.
        :param type_: Load Balancer commercial offer type. Use the Load Balancer types endpoint to retrieve a list of available offer types.
        :param description: Description for the Load Balancer.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization_id: Scaleway Organization to create the Load Balancer in.
        :param project_id: Scaleway Project to create the Load Balancer in.
        :param name: Name for the Load Balancer.
        :param ip_id: ID of an existing flexible IP address to attach to the Load Balancer.
        :param assign_flexible_ip: Defines whether to automatically assign a flexible public IP to lb. Default value is `false` (do not assign).
        :param tags: List of tags for the Load Balancer.
        :param ssl_compatibility_level: Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and do not need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.create_lb(
                type="example",
                description="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs",
            body=marshal_ZonedApiCreateLbRequest(
                ZonedApiCreateLbRequest(
                    type_=type_,
                    description=description,
                    zone=zone,
                    name=name or random_name(prefix="lb"),
                    ip_id=ip_id,
                    assign_flexible_ip=assign_flexible_ip,
                    tags=tags,
                    ssl_compatibility_level=ssl_compatibility_level,
                    organization_id=organization_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def get_lb(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Get a Load Balancer.
        Retrieve information about an existing Load Balancer, specified by its Load Balancer ID. Its full details, including name, status and IP address, are returned in the response object.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.get_lb(
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def wait_for_lb(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Lb, bool]] = None,
    ) -> Lb:
        """
        Get a Load Balancer.
        Retrieve information about an existing Load Balancer, specified by its Load Balancer ID. Its full details, including name, status and IP address, are returned in the response object.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.get_lb(
                lb_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in LB_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_lb,
            options=options,
            args={
                "lb_id": lb_id,
                "zone": zone,
            },
        )

    def update_lb(
        self,
        *,
        description: str,
        name: str,
        lb_id: str,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
        ssl_compatibility_level: Optional[SSLCompatibilityLevel] = None,
    ) -> Lb:
        """
        Update a Load Balancer.
        Update the parameters of an existing Load Balancer, specified by its Load Balancer ID. Note that the request type is PUT and not PATCH. You must set all parameters.
        :param description: Load Balancer description.
        :param name: Load Balancer name.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: List of tags for the Load Balancer.
        :param ssl_compatibility_level: Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and don't need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.update_lb(
                description="example",
                name="example",
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}",
            body=marshal_ZonedApiUpdateLbRequest(
                ZonedApiUpdateLbRequest(
                    description=description,
                    name=name,
                    lb_id=lb_id,
                    zone=zone,
                    tags=tags,
                    ssl_compatibility_level=ssl_compatibility_level,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def delete_lb(
        self,
        *,
        release_ip: bool,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a Load Balancer.
        Delete an existing Load Balancer, specified by its Load Balancer ID. Deleting a Load Balancer is permanent, and cannot be undone. The Load Balancer's flexible IP address can either be deleted with the Load Balancer, or kept in your account for future use.
        :param release_ip: Defines whether the Load Balancer's flexible IP should be deleted. Set to true to release the flexible IP, or false to keep it available in your account for future Load Balancers.
        :param lb_id: ID of the Load Balancer to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_lb(
                release_ip=False,
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}",
            params={
                "release_ip": release_ip,
            },
        )

        self._throw_on_error(res)

    def migrate_lb(
        self,
        *,
        type_: str,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Migrate a Load Balancer.
        Migrate an existing Load Balancer from one commercial type to another. Allows you to scale your Load Balancer up or down in terms of bandwidth or multi-cloud provision.
        :param type_: Load Balancer type to migrate to (use the List all Load Balancer offer types endpoint to get a list of available offer types).
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.migrate_lb(
                type="example",
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/migrate",
            body=marshal_ZonedApiMigrateLbRequest(
                ZonedApiMigrateLbRequest(
                    type_=type_,
                    lb_id=lb_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def list_i_ps(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        ip_address: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListIpsResponse:
        """
        List IP addresses.
        List the Load Balancer flexible IP addresses held in the account (filtered by Organization ID or Project ID). It is also possible to search for a specific IP address.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of IP addresses to return.
        :param ip_address: IP address to filter for.
        :param organization_id: Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = api.list_i_ps()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/ips",
            params={
                "ip_address": ip_address,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIpsResponse(res.json())

    def list_i_ps_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        ip_address: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Ip]:
        """
        List IP addresses.
        List the Load Balancer flexible IP addresses held in the account (filtered by Organization ID or Project ID). It is also possible to search for a specific IP address.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of IP addresses to return.
        :param ip_address: IP address to filter for.
        :param organization_id: Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
        :return: :class:`List[Ip] <List[Ip]>`

        Usage:
        ::

            result = api.list_i_ps_all()
        """

        return fetch_all_pages(
            type=ListIpsResponse,
            key="ips",
            fetcher=self.list_i_ps,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "ip_address": ip_address,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def create_ip(
        self,
        *,
        zone: Optional[Zone] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Create an IP address.
        Create a new Load Balancer flexible IP address, in the specified Scaleway Project. This can be attached to new Load Balancers created in the future.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization_id: Organization ID of the Organization where the IP address should be created.
        :param project_id: Project ID of the Project where the IP address should be created.
        :param reverse: Reverse DNS (domain name) for the IP address.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.create_ip()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/ips",
            body=marshal_ZonedApiCreateIpRequest(
                ZonedApiCreateIpRequest(
                    zone=zone,
                    reverse=reverse,
                    organization_id=organization_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    def get_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
    ) -> Ip:
        """
        Get an IP address.
        Retrieve the full details of a Load Balancer flexible IP address.
        :param ip_id: IP address ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.get_ip(
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    def release_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete an IP address.
        Delete a Load Balancer flexible IP address. This action is irreversible, and cannot be undone.
        :param ip_id: IP address ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.release_ip(
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)

    def update_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Update an IP address.
        Update the reverse DNS of a Load Balancer flexible IP address.
        :param ip_id: IP address ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param reverse: Reverse DNS (domain name) for the IP address.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.update_ip(
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/lb/v1/zones/{param_zone}/ips/{param_ip_id}",
            body=marshal_ZonedApiUpdateIpRequest(
                ZonedApiUpdateIpRequest(
                    ip_id=ip_id,
                    zone=zone,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    def list_backends(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: Optional[ListBackendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListBackendsResponse:
        """
        List the backends of a given Load Balancer.
        List all the backends of a Load Balancer, specified by its Load Balancer ID. By default, results are returned in ascending order by the creation date of each backend. The response is an array of backend objects, containing full details of each one including their configuration parameters such as protocol, port and forwarding algorithm.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the backend to filter for.
        :param order_by: Sort order of backends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of backends to return.
        :return: :class:`ListBackendsResponse <ListBackendsResponse>`

        Usage:
        ::

            result = api.list_backends(
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/backends",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendsResponse(res.json())

    def list_backends_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: Optional[ListBackendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Backend]:
        """
        List the backends of a given Load Balancer.
        List all the backends of a Load Balancer, specified by its Load Balancer ID. By default, results are returned in ascending order by the creation date of each backend. The response is an array of backend objects, containing full details of each one including their configuration parameters such as protocol, port and forwarding algorithm.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the backend to filter for.
        :param order_by: Sort order of backends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of backends to return.
        :return: :class:`List[Backend] <List[Backend]>`

        Usage:
        ::

            result = api.list_backends_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListBackendsResponse,
            key="backends",
            fetcher=self.list_backends,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_backend(
        self,
        *,
        forward_port: int,
        health_check: HealthCheck,
        lb_id: str,
        sticky_sessions_cookie_name: str,
        zone: Optional[Zone] = None,
        send_proxy_v2: Optional[bool] = None,
        on_marked_down_action: Optional[OnMarkedDownAction] = None,
        forward_port_algorithm: Optional[ForwardPortAlgorithm] = None,
        forward_protocol: Optional[Protocol] = None,
        server_ip: Optional[List[str]] = None,
        name: Optional[str] = None,
        timeout_server: Optional[str] = None,
        timeout_connect: Optional[str] = None,
        timeout_tunnel: Optional[str] = None,
        sticky_sessions: Optional[StickySessionsType] = None,
        proxy_protocol: Optional[ProxyProtocol] = None,
        failover_host: Optional[str] = None,
        ssl_bridging: Optional[bool] = None,
        ignore_ssl_server_verify: Optional[bool] = None,
        redispatch_attempt_count: Optional[int] = None,
        max_retries: Optional[int] = None,
        max_connections: Optional[int] = None,
        timeout_queue: Optional[str] = None,
    ) -> Backend:
        """
        Create a backend for a given Load Balancer.
        Create a new backend for a given Load Balancer, specifying its full configuration including protocol, port and forwarding algorithm.
        :param forward_port: Port to be used by the backend when forwarding traffic to backend servers.
        :param health_check: Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
        :param lb_id: Load Balancer ID.
        :param sticky_sessions_cookie_name: Cookie name for cookie-based sticky sessions.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field.
        :param on_marked_down_action: Action to take when a backend server is marked as down.
        :param forward_port_algorithm: Load balancing algorithm to be used when determining which backend server to forward new traffic to.
        :param forward_protocol: Protocol to be used by the backend when forwarding traffic to backend servers.
        :param server_ip: List of backend server IP addresses (IPv4 or IPv6) the backend should forward traffic to.
        :param name: Name for the backend.
        :param timeout_server: Maximum allowed time for a backend server to process a request.
        :param timeout_connect: Maximum allowed time for establishing a connection to a backend server.
        :param timeout_tunnel: Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
        :param sticky_sessions: Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie TO stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
        :param proxy_protocol: Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
        :param failover_host: Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
        :param ssl_bridging: Defines whether to enable SSL bridging between the Load Balancer and backend servers.
        :param ignore_ssl_server_verify: Defines whether the server certificate verification should be ignored.
        :param redispatch_attempt_count: Whether to use another backend server on each attempt.
        :param max_retries: Number of retries when a backend server connection failed.
        :param max_connections: Maximum number of connections allowed per backend server.
        :param timeout_queue: Maximum time for a request to be left pending in queue when `max_connections` is reached.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.create_backend(
                forward_port=1,
                health_check=HealthCheck(),
                lb_id="example",
                sticky_sessions_cookie_name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/backends",
            body=marshal_ZonedApiCreateBackendRequest(
                ZonedApiCreateBackendRequest(
                    forward_port=forward_port,
                    health_check=health_check,
                    lb_id=lb_id,
                    sticky_sessions_cookie_name=sticky_sessions_cookie_name,
                    zone=zone,
                    send_proxy_v2=send_proxy_v2,
                    on_marked_down_action=on_marked_down_action,
                    forward_port_algorithm=forward_port_algorithm,
                    forward_protocol=forward_protocol,
                    server_ip=server_ip,
                    name=name or random_name(prefix="lbb"),
                    timeout_server=timeout_server,
                    timeout_connect=timeout_connect,
                    timeout_tunnel=timeout_tunnel,
                    sticky_sessions=sticky_sessions,
                    proxy_protocol=proxy_protocol,
                    failover_host=failover_host,
                    ssl_bridging=ssl_bridging,
                    ignore_ssl_server_verify=ignore_ssl_server_verify,
                    redispatch_attempt_count=redispatch_attempt_count,
                    max_retries=max_retries,
                    max_connections=max_connections,
                    timeout_queue=timeout_queue,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def get_backend(
        self,
        *,
        backend_id: str,
        zone: Optional[Zone] = None,
    ) -> Backend:
        """
        Get a backend of a given Load Balancer.
        Get the full details of a given backend, specified by its backend ID. The response contains the backend's full configuration parameters including protocol, port and forwarding algorithm.
        :param backend_id: Backend ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.get_backend(
                backend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def update_backend(
        self,
        *,
        forward_port: int,
        name: str,
        backend_id: str,
        sticky_sessions_cookie_name: str,
        zone: Optional[Zone] = None,
        timeout_connect: Optional[str] = None,
        on_marked_down_action: Optional[OnMarkedDownAction] = None,
        forward_port_algorithm: Optional[ForwardPortAlgorithm] = None,
        send_proxy_v2: Optional[bool] = None,
        timeout_server: Optional[str] = None,
        forward_protocol: Optional[Protocol] = None,
        timeout_tunnel: Optional[str] = None,
        sticky_sessions: Optional[StickySessionsType] = None,
        proxy_protocol: Optional[ProxyProtocol] = None,
        failover_host: Optional[str] = None,
        ssl_bridging: Optional[bool] = None,
        ignore_ssl_server_verify: Optional[bool] = None,
        redispatch_attempt_count: Optional[int] = None,
        max_retries: Optional[int] = None,
        max_connections: Optional[int] = None,
        timeout_queue: Optional[str] = None,
    ) -> Backend:
        """
        Update a backend of a given Load Balancer.
        Update a backend of a given Load Balancer, specified by its backend ID. Note that the request type is PUT and not PATCH. You must set all parameters.
        :param forward_port: Port to be used by the backend when forwarding traffic to backend servers.
        :param name: Backend name.
        :param backend_id: Backend ID.
        :param sticky_sessions_cookie_name: Cookie name for cookie-based sticky sessions.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param timeout_connect: Maximum allowed time for establishing a connection to a backend server.
        :param on_marked_down_action: Action to take when a backend server is marked as down.
        :param forward_port_algorithm: Load balancing algorithm to be used when determining which backend server to forward new traffic to.
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field.
        :param timeout_server: Maximum allowed time for a backend server to process a request.
        :param forward_protocol: Protocol to be used by the backend when forwarding traffic to backend servers.
        :param timeout_tunnel: Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
        :param sticky_sessions: Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
        :param proxy_protocol: Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
        :param failover_host: Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
        :param ssl_bridging: Defines whether to enable SSL bridging between the Load Balancer and backend servers.
        :param ignore_ssl_server_verify: Defines whether the server certificate verification should be ignored.
        :param redispatch_attempt_count: Whether to use another backend server on each attempt.
        :param max_retries: Number of retries when a backend server connection failed.
        :param max_connections: Maximum number of connections allowed per backend server.
        :param timeout_queue: Maximum time for a request to be left pending in queue when `max_connections` is reached.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.update_backend(
                forward_port=1,
                name="example",
                backend_id="example",
                sticky_sessions_cookie_name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}",
            body=marshal_ZonedApiUpdateBackendRequest(
                ZonedApiUpdateBackendRequest(
                    forward_port=forward_port,
                    name=name,
                    backend_id=backend_id,
                    sticky_sessions_cookie_name=sticky_sessions_cookie_name,
                    zone=zone,
                    timeout_connect=timeout_connect,
                    on_marked_down_action=on_marked_down_action,
                    forward_port_algorithm=forward_port_algorithm,
                    send_proxy_v2=send_proxy_v2,
                    timeout_server=timeout_server,
                    forward_protocol=forward_protocol,
                    timeout_tunnel=timeout_tunnel,
                    sticky_sessions=sticky_sessions,
                    proxy_protocol=proxy_protocol,
                    failover_host=failover_host,
                    ssl_bridging=ssl_bridging,
                    ignore_ssl_server_verify=ignore_ssl_server_verify,
                    redispatch_attempt_count=redispatch_attempt_count,
                    max_retries=max_retries,
                    max_connections=max_connections,
                    timeout_queue=timeout_queue,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def delete_backend(
        self,
        *,
        backend_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a backend of a given Load Balancer.
        Delete a backend of a given Load Balancer, specified by its backend ID. This action is irreversible and cannot be undone.
        :param backend_id: ID of the backend to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_backend(
                backend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)

    def add_backend_servers(
        self,
        *,
        backend_id: str,
        zone: Optional[Zone] = None,
        server_ip: Optional[List[str]] = None,
    ) -> Backend:
        """
        Add a set of backend servers to a given backend.
        For a given backend specified by its backend ID, add a set of backend servers (identified by their IP addresses) it should forward traffic to. These will be appended to any existing set of backend servers for this backend.
        :param backend_id: Backend ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_ip: List of IP addresses to add to backend servers.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.add_backend_servers(
                backend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}/servers",
            body=marshal_ZonedApiAddBackendServersRequest(
                ZonedApiAddBackendServersRequest(
                    backend_id=backend_id,
                    zone=zone,
                    server_ip=server_ip,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def remove_backend_servers(
        self,
        *,
        backend_id: str,
        zone: Optional[Zone] = None,
        server_ip: Optional[List[str]] = None,
    ) -> Backend:
        """
        Remove a set of servers for a given backend.
        For a given backend specified by its backend ID, remove the specified backend servers (identified by their IP addresses) so that it no longer forwards traffic to them.
        :param backend_id: Backend ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_ip: List of IP addresses to remove from backend servers.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.remove_backend_servers(
                backend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}/servers",
            body=marshal_ZonedApiRemoveBackendServersRequest(
                ZonedApiRemoveBackendServersRequest(
                    backend_id=backend_id,
                    zone=zone,
                    server_ip=server_ip,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def set_backend_servers(
        self,
        *,
        backend_id: str,
        zone: Optional[Zone] = None,
        server_ip: Optional[List[str]] = None,
    ) -> Backend:
        """
        Define all backend servers for a given backend.
        For a given backend specified by its backend ID, define the set of backend servers (identified by their IP addresses) that it should forward traffic to. Any existing backend servers configured for this backend will be removed.
        :param backend_id: Backend ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_ip: List of IP addresses for backend servers. Any other existing backend servers will be removed.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.set_backend_servers(
                backend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}/servers",
            body=marshal_ZonedApiSetBackendServersRequest(
                ZonedApiSetBackendServersRequest(
                    backend_id=backend_id,
                    zone=zone,
                    server_ip=server_ip,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def update_health_check(
        self,
        *,
        check_send_proxy: bool,
        port: int,
        backend_id: str,
        check_max_retries: int,
        zone: Optional[Zone] = None,
        check_delay: Optional[str] = None,
        check_timeout: Optional[str] = None,
        tcp_config: Optional[HealthCheckTcpConfig] = None,
        mysql_config: Optional[HealthCheckMysqlConfig] = None,
        pgsql_config: Optional[HealthCheckPgsqlConfig] = None,
        ldap_config: Optional[HealthCheckLdapConfig] = None,
        redis_config: Optional[HealthCheckRedisConfig] = None,
        http_config: Optional[HealthCheckHttpConfig] = None,
        https_config: Optional[HealthCheckHttpsConfig] = None,
        transient_check_delay: Optional[str] = None,
    ) -> HealthCheck:
        """
        Update a health check for a given backend.
        Update the configuration of the health check performed by a given backend to verify the health of its backend servers, identified by its backend ID. Note that the request type is PUT and not PATCH. You must set all parameters.
        :param check_send_proxy: Defines whether proxy protocol should be activated for the health check.
        :param port: Port to use for the backend server health check.
        :param backend_id: Backend ID.
        :param check_max_retries: Number of consecutive unsuccessful health checks after which the server will be considered dead.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param check_delay: Time to wait between two consecutive health checks.
        :param check_timeout: Maximum time a backend server has to reply to the health check.
        :param tcp_config: Object to configure a basic TCP health check.
        :param mysql_config: Object to configure a MySQL health check. The check requires MySQL >=3.22, for older versions, use a TCP health check.
        :param pgsql_config: Object to configure a PostgreSQL health check.
        :param ldap_config: Object to configure an LDAP health check. The response is analyzed to find the LDAPv3 response message.
        :param redis_config: Object to configure a Redis health check. The response is analyzed to find the +PONG response message.
        :param http_config: Object to configure an HTTP health check.
        :param https_config: Object to configure an HTTPS health check.
        :param transient_check_delay: Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
        :return: :class:`HealthCheck <HealthCheck>`

        Usage:
        ::

            result = api.update_health_check(
                check_send_proxy=False,
                port=1,
                backend_id="example",
                check_max_retries=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}/healthcheck",
            body=marshal_ZonedApiUpdateHealthCheckRequest(
                ZonedApiUpdateHealthCheckRequest(
                    check_send_proxy=check_send_proxy,
                    check_max_retries=check_max_retries,
                    port=port,
                    backend_id=backend_id,
                    zone=zone,
                    check_delay=check_delay,
                    check_timeout=check_timeout,
                    transient_check_delay=transient_check_delay,
                    tcp_config=tcp_config,
                    mysql_config=mysql_config,
                    pgsql_config=pgsql_config,
                    ldap_config=ldap_config,
                    redis_config=redis_config,
                    http_config=http_config,
                    https_config=https_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_HealthCheck(res.json())

    def list_frontends(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: Optional[ListFrontendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListFrontendsResponse:
        """
        List frontends of a given Load Balancer.
        List all the frontends of a Load Balancer, specified by its Load Balancer ID. By default, results are returned in ascending order by the creation date of each frontend. The response is an array of frontend objects, containing full details of each one including the port they listen on and the backend they are attached to.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the frontend to filter for.
        :param order_by: Sort order of frontends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of frontends to return.
        :return: :class:`ListFrontendsResponse <ListFrontendsResponse>`

        Usage:
        ::

            result = api.list_frontends(
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/frontends",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListFrontendsResponse(res.json())

    def list_frontends_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: Optional[ListFrontendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Frontend]:
        """
        List frontends of a given Load Balancer.
        List all the frontends of a Load Balancer, specified by its Load Balancer ID. By default, results are returned in ascending order by the creation date of each frontend. The response is an array of frontend objects, containing full details of each one including the port they listen on and the backend they are attached to.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the frontend to filter for.
        :param order_by: Sort order of frontends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of frontends to return.
        :return: :class:`List[Frontend] <List[Frontend]>`

        Usage:
        ::

            result = api.list_frontends_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListFrontendsResponse,
            key="frontends",
            fetcher=self.list_frontends,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_frontend(
        self,
        *,
        enable_http3: bool,
        backend_id: str,
        inbound_port: int,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        timeout_client: Optional[str] = None,
        certificate_id: Optional[str] = None,
        certificate_ids: Optional[List[str]] = None,
    ) -> Frontend:
        """
        Create a frontend in a given Load Balancer.
        Create a new frontend for a given Load Balancer, specifying its configuration including the port it should listen on and the backend to attach it to.
        :param enable_http3: Defines whether to enable HTTP/3 protocol on the frontend.
        :param backend_id: Backend ID (ID of the backend the frontend should pass traffic to).
        :param inbound_port: Port the frontend should listen on.
        :param lb_id: Load Balancer ID (ID of the Load Balancer to attach the frontend to).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name for the frontend.
        :param timeout_client: Maximum allowed inactivity time on the client side.
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array.
        :param certificate_ids: List of SSL/TLS certificate IDs to bind to the frontend.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.create_frontend(
                enable_http3=False,
                backend_id="example",
                inbound_port=1,
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/frontends",
            body=marshal_ZonedApiCreateFrontendRequest(
                ZonedApiCreateFrontendRequest(
                    enable_http3=enable_http3,
                    backend_id=backend_id,
                    inbound_port=inbound_port,
                    lb_id=lb_id,
                    zone=zone,
                    name=name or random_name(prefix="lbf"),
                    timeout_client=timeout_client,
                    certificate_id=certificate_id,
                    certificate_ids=certificate_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    def get_frontend(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
    ) -> Frontend:
        """
        Get a frontend.
        Get the full details of a given frontend, specified by its frontend ID. The response contains the frontend's full configuration parameters including the backend it is attached to, the port it listens on, and any certificates it has.
        :param frontend_id: Frontend ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.get_frontend(
                frontend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    def update_frontend(
        self,
        *,
        enable_http3: bool,
        backend_id: str,
        inbound_port: int,
        name: str,
        frontend_id: str,
        zone: Optional[Zone] = None,
        timeout_client: Optional[str] = None,
        certificate_id: Optional[str] = None,
        certificate_ids: Optional[List[str]] = None,
    ) -> Frontend:
        """
        Update a frontend.
        Update a given frontend, specified by its frontend ID. You can update configuration parameters including its name and the port it listens on. Note that the request type is PUT and not PATCH. You must set all parameters.
        :param enable_http3: Defines whether to enable HTTP/3 protocol on the frontend.
        :param backend_id: Backend ID (ID of the backend the frontend should pass traffic to).
        :param inbound_port: Port the frontend should listen on.
        :param name: Frontend name.
        :param frontend_id: Frontend ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param timeout_client: Maximum allowed inactivity time on the client side.
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array.
        :param certificate_ids: List of SSL/TLS certificate IDs to bind to the frontend.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.update_frontend(
                enable_http3=False,
                backend_id="example",
                inbound_port=1,
                name="example",
                frontend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}",
            body=marshal_ZonedApiUpdateFrontendRequest(
                ZonedApiUpdateFrontendRequest(
                    enable_http3=enable_http3,
                    backend_id=backend_id,
                    inbound_port=inbound_port,
                    name=name,
                    frontend_id=frontend_id,
                    zone=zone,
                    timeout_client=timeout_client,
                    certificate_id=certificate_id,
                    certificate_ids=certificate_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    def delete_frontend(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a frontend.
        Delete a given frontend, specified by its frontend ID. This action is irreversible and cannot be undone.
        :param frontend_id: ID of the frontend to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_frontend(
                frontend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)

    def list_routes(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> ListRoutesResponse:
        """
        List all routes.
        List all routes for a given frontend. The response is an array of routes, each one  with a specified backend to direct to if a certain condition is matched (based on the value of the SNI field or HTTP Host header).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of routes in the response.
        :param page_size: The number of route objects to return.
        :param page: The page number to return, from the paginated results.
        :param frontend_id: Frontend ID to filter for, only Routes from this Frontend will be returned.
        :return: :class:`ListRoutesResponse <ListRoutesResponse>`

        Usage:
        ::

            result = api.list_routes()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/routes",
            params={
                "frontend_id": frontend_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRoutesResponse(res.json())

    def list_routes_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> List[Route]:
        """
        List all routes.
        List all routes for a given frontend. The response is an array of routes, each one  with a specified backend to direct to if a certain condition is matched (based on the value of the SNI field or HTTP Host header).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of routes in the response.
        :param page_size: The number of route objects to return.
        :param page: The page number to return, from the paginated results.
        :param frontend_id: Frontend ID to filter for, only Routes from this Frontend will be returned.
        :return: :class:`List[Route] <List[Route]>`

        Usage:
        ::

            result = api.list_routes_all()
        """

        return fetch_all_pages(
            type=ListRoutesResponse,
            key="routes",
            fetcher=self.list_routes,
            args={
                "zone": zone,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "frontend_id": frontend_id,
            },
        )

    def create_route(
        self,
        *,
        backend_id: str,
        frontend_id: str,
        zone: Optional[Zone] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Create a route.
        Create a new route on a given frontend. To configure a route, specify the backend to direct to if a certain condition is matched (based on the value of the SNI field or HTTP Host header).
        :param backend_id: ID of the target backend for the route.
        :param frontend_id: ID of the source frontend to create the route on.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param match: Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.create_route(
                backend_id="example",
                frontend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/routes",
            body=marshal_ZonedApiCreateRouteRequest(
                ZonedApiCreateRouteRequest(
                    backend_id=backend_id,
                    frontend_id=frontend_id,
                    zone=zone,
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    def get_route(
        self,
        *,
        route_id: str,
        zone: Optional[Zone] = None,
    ) -> Route:
        """
        Get a route.
        Retrieve information about an existing route, specified by its route ID. Its full details, origin frontend, target backend and match condition, are returned in the response object.
        :param route_id: Route ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.get_route(
                route_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    def update_route(
        self,
        *,
        backend_id: str,
        route_id: str,
        zone: Optional[Zone] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Update a route.
        Update the configuration of an existing route, specified by its route ID.
        :param backend_id: ID of the target backend for the route.
        :param route_id: Route ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param match: Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.update_route(
                backend_id="example",
                route_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/routes/{param_route_id}",
            body=marshal_ZonedApiUpdateRouteRequest(
                ZonedApiUpdateRouteRequest(
                    backend_id=backend_id,
                    route_id=route_id,
                    zone=zone,
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    def delete_route(
        self,
        *,
        route_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a route.
        Delete an existing route, specified by its route ID. Deleting a route is permanent, and cannot be undone.
        :param route_id: Route ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_route(
                route_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/routes/{param_route_id}",
        )

        self._throw_on_error(res)

    def get_lb_stats(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        backend_id: Optional[str] = None,
    ) -> LbStats:
        """
        Get usage statistics of a given Load Balancer.
        Get usage statistics of a given Load Balancer.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param backend_id: ID of the backend.
        :return: :class:`LbStats <LbStats>`
        :deprecated

        Usage:
        ::

            result = api.get_lb_stats(
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/stats",
            params={
                "backend_id": backend_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_LbStats(res.json())

    def list_backend_stats(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        backend_id: Optional[str] = None,
    ) -> ListBackendStatsResponse:
        """
        List backend server statistics.
        List information about your backend servers, including their state and the result of their last health check.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of items to return.
        :param backend_id: ID of the backend.
        :return: :class:`ListBackendStatsResponse <ListBackendStatsResponse>`

        Usage:
        ::

            result = api.list_backend_stats(
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/backend-stats",
            params={
                "backend_id": backend_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendStatsResponse(res.json())

    def list_backend_stats_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        backend_id: Optional[str] = None,
    ) -> List[BackendServerStats]:
        """
        List backend server statistics.
        List information about your backend servers, including their state and the result of their last health check.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of items to return.
        :param backend_id: ID of the backend.
        :return: :class:`List[BackendServerStats] <List[BackendServerStats]>`

        Usage:
        ::

            result = api.list_backend_stats_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListBackendStatsResponse,
            key="backend_servers_stats",
            fetcher=self.list_backend_stats,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "backend_id": backend_id,
            },
        )

    def list_acls(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListAclRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> ListAclResponse:
        """
        List ACLs for a given frontend.
        List the ACLs for a given frontend, specified by its frontend ID. The response is an array of ACL objects, each one representing an ACL that denies or allows traffic based on certain conditions.
        :param frontend_id: Frontend ID (ACLs attached to this frontend will be returned in the response).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of ACLs in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of ACLs to return.
        :param name: ACL name to filter for.
        :return: :class:`ListAclResponse <ListAclResponse>`

        Usage:
        ::

            result = api.list_acls(
                frontend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}/acls",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAclResponse(res.json())

    def list_acls_all(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListAclRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> List[Acl]:
        """
        List ACLs for a given frontend.
        List the ACLs for a given frontend, specified by its frontend ID. The response is an array of ACL objects, each one representing an ACL that denies or allows traffic based on certain conditions.
        :param frontend_id: Frontend ID (ACLs attached to this frontend will be returned in the response).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of ACLs in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of ACLs to return.
        :param name: ACL name to filter for.
        :return: :class:`List[Acl] <List[Acl]>`

        Usage:
        ::

            result = api.list_acls_all(
                frontend_id="example",
            )
        """

        return fetch_all_pages(
            type=ListAclResponse,
            key="acls",
            fetcher=self.list_acls,
            args={
                "frontend_id": frontend_id,
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
            },
        )

    def create_acl(
        self,
        *,
        description: str,
        index: int,
        match: AclMatch,
        action: AclAction,
        frontend_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
    ) -> Acl:
        """
        Create an ACL for a given frontend.
        Create a new ACL for a given frontend. Each ACL must have a name, an action to perform (allow or deny), and a match rule (the action is carried out when the incoming traffic matches the rule).
        :param description: ACL description.
        :param index: Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
        :param match: ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
        :param action: Action to take when incoming traffic matches an ACL filter.
        :param frontend_id: Frontend ID to attach the ACL to.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: ACL name.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.create_acl(
                description="example",
                index=1,
                match=AclMatch(),
                action=AclAction(),
                frontend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}/acls",
            body=marshal_ZonedApiCreateAclRequest(
                ZonedApiCreateAclRequest(
                    description=description,
                    index=index,
                    match=match,
                    action=action,
                    frontend_id=frontend_id,
                    zone=zone,
                    name=name or random_name(prefix="acl"),
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def get_acl(
        self,
        *,
        acl_id: str,
        zone: Optional[Zone] = None,
    ) -> Acl:
        """
        Get an ACL.
        Get information for a particular ACL, specified by its ACL ID. The response returns full details of the ACL, including its name, action, match rule and frontend.
        :param acl_id: ACL ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.get_acl(
                acl_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def update_acl(
        self,
        *,
        index: int,
        match: AclMatch,
        action: AclAction,
        name: str,
        acl_id: str,
        zone: Optional[Zone] = None,
        description: Optional[str] = None,
    ) -> Acl:
        """
        Update an ACL.
        Update a particular ACL, specified by its ACL ID. You can update details including its name, action and match rule.
        :param index: Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
        :param match: ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
        :param action: Action to take when incoming traffic matches an ACL filter.
        :param name: ACL name.
        :param acl_id: ACL ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param description: ACL description.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.update_acl(
                index=1,
                match=AclMatch(),
                action=AclAction(),
                name="example",
                acl_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/acls/{param_acl_id}",
            body=marshal_ZonedApiUpdateAclRequest(
                ZonedApiUpdateAclRequest(
                    index=index,
                    match=match,
                    action=action,
                    name=name,
                    acl_id=acl_id,
                    zone=zone,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def delete_acl(
        self,
        *,
        acl_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete an ACL.
        Delete an ACL, specified by its ACL ID. Deleting an ACL is irreversible and cannot be undone.
        :param acl_id: ACL ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_acl(
                acl_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)

    def set_acls(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
        acls: Optional[List[AclSpec]] = None,
    ) -> SetAclsResponse:
        """
        Define all ACLs for a given frontend.
        For a given frontend specified by its frontend ID, define and add the complete set of ACLS for that frontend. Any existing ACLs on this frontend will be removed.
        :param frontend_id: Frontend ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param acls: List of ACLs for this frontend. Any other existing ACLs on this frontend will be removed.
        :return: :class:`SetAclsResponse <SetAclsResponse>`

        Usage:
        ::

            result = api.set_acls(
                frontend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}/acls",
            body=marshal_ZonedApiSetAclsRequest(
                ZonedApiSetAclsRequest(
                    frontend_id=frontend_id,
                    zone=zone,
                    acls=acls,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetAclsResponse(res.json())

    def create_certificate(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig] = None,
        custom_certificate: Optional[CreateCertificateRequestCustomCertificate] = None,
    ) -> Certificate:
        """
        Create an SSL/TLS certificate.
        Generate a new SSL/TLS certificate for a given Load Balancer. You can choose to create a Let's Encrypt certificate, or import a custom certificate.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name for the certificate.
        :param letsencrypt: Object to define a new Let's Encrypt certificate to be generated.
        :param custom_certificate: Object to define an existing custom certificate to be imported.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.create_certificate(
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/certificates",
            body=marshal_ZonedApiCreateCertificateRequest(
                ZonedApiCreateCertificateRequest(
                    lb_id=lb_id,
                    zone=zone,
                    name=name or random_name(prefix="certificate"),
                    letsencrypt=letsencrypt,
                    custom_certificate=custom_certificate,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    def list_certificates(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListCertificatesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> ListCertificatesResponse:
        """
        List all SSL/TLS certificates on a given Load Balancer.
        List all the SSL/TLS certificates on a given Load Balancer. The response is an array of certificate objects, which are by default listed in ascending order of creation date.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of certificates in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of certificates to return.
        :param name: Certificate name to filter for, only certificates of this name will be returned.
        :return: :class:`ListCertificatesResponse <ListCertificatesResponse>`

        Usage:
        ::

            result = api.list_certificates(
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/certificates",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCertificatesResponse(res.json())

    def list_certificates_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListCertificatesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> List[Certificate]:
        """
        List all SSL/TLS certificates on a given Load Balancer.
        List all the SSL/TLS certificates on a given Load Balancer. The response is an array of certificate objects, which are by default listed in ascending order of creation date.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of certificates in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of certificates to return.
        :param name: Certificate name to filter for, only certificates of this name will be returned.
        :return: :class:`List[Certificate] <List[Certificate]>`

        Usage:
        ::

            result = api.list_certificates_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListCertificatesResponse,
            key="certificates",
            fetcher=self.list_certificates,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
            },
        )

    def get_certificate(
        self,
        *,
        certificate_id: str,
        zone: Optional[Zone] = None,
    ) -> Certificate:
        """
        Get an SSL/TLS certificate.
        Get information for a particular SSL/TLS certificate, specified by its certificate ID. The response returns full details of the certificate, including its type, main domain name, and alternative domain names.
        :param certificate_id: Certificate ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.get_certificate(
                certificate_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    def wait_for_certificate(
        self,
        *,
        certificate_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Certificate, bool]] = None,
    ) -> Certificate:
        """
        Get an SSL/TLS certificate.
        Get information for a particular SSL/TLS certificate, specified by its certificate ID. The response returns full details of the certificate, including its type, main domain name, and alternative domain names.
        :param certificate_id: Certificate ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.get_certificate(
                certificate_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in CERTIFICATE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_certificate,
            options=options,
            args={
                "certificate_id": certificate_id,
                "zone": zone,
            },
        )

    def update_certificate(
        self,
        *,
        name: str,
        certificate_id: str,
        zone: Optional[Zone] = None,
    ) -> Certificate:
        """
        Update an SSL/TLS certificate.
        Update the name of a particular SSL/TLS certificate, specified by its certificate ID.
        :param name: Certificate name.
        :param certificate_id: Certificate ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.update_certificate(
                name="example",
                certificate_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/certificates/{param_certificate_id}",
            body=marshal_ZonedApiUpdateCertificateRequest(
                ZonedApiUpdateCertificateRequest(
                    name=name,
                    certificate_id=certificate_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    def delete_certificate(
        self,
        *,
        certificate_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete an SSL/TLS certificate.
        Delete an SSL/TLS certificate, specified by its certificate ID. Deleting a certificate is irreversible and cannot be undone.
        :param certificate_id: Certificate ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_certificate(
                certificate_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)

    def list_lb_types(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListLbTypesResponse:
        """
        List all Load Balancer offer types.
        List all the different commercial Load Balancer types. The response includes an array of offer types, each with a name, description, and information about its stock availability.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`ListLbTypesResponse <ListLbTypesResponse>`

        Usage:
        ::

            result = api.list_lb_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lb-types",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLbTypesResponse(res.json())

    def list_lb_types_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[LbType]:
        """
        List all Load Balancer offer types.
        List all the different commercial Load Balancer types. The response includes an array of offer types, each with a name, description, and information about its stock availability.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`List[LbType] <List[LbType]>`

        Usage:
        ::

            result = api.list_lb_types_all()
        """

        return fetch_all_pages(
            type=ListLbTypesResponse,
            key="lb_types",
            fetcher=self.list_lb_types,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_subscriber(
        self,
        *,
        name: str,
        zone: Optional[Zone] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Subscriber:
        """
        Create a subscriber.
        Create a new subscriber, either with an email configuration or a webhook configuration, for a specified Scaleway Project.
        :param name: Subscriber name.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param email_config: Email address configuration.
        :param webhook_config: WebHook URI configuration.
        :param organization_id: Organization ID to create the subscriber in.
        :param project_id: Project ID to create the subscriber in.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.create_subscriber(
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/subscribers",
            body=marshal_ZonedApiCreateSubscriberRequest(
                ZonedApiCreateSubscriberRequest(
                    name=name,
                    zone=zone,
                    organization_id=organization_id,
                    project_id=project_id,
                    email_config=email_config,
                    webhook_config=webhook_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    def get_subscriber(
        self,
        *,
        subscriber_id: str,
        zone: Optional[Zone] = None,
    ) -> Subscriber:
        """
        Get a subscriber.
        Retrieve information about an existing subscriber, specified by its subscriber ID. Its full details, including name and email/webhook configuration, are returned in the response object.
        :param subscriber_id: Subscriber ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.get_subscriber(
                subscriber_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/subscribers/{param_subscriber_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    def list_subscriber(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListSubscriberRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListSubscriberResponse:
        """
        List all subscribers.
        List all subscribers to Load Balancer alerts. By default, returns all subscribers to Load Balancer alerts for the Organization associated with the authentication token used for the request.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of subscribers in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :param name: Subscriber name to search for.
        :param organization_id: Filter subscribers by Organization ID.
        :param project_id: Filter subscribers by Project ID.
        :return: :class:`ListSubscriberResponse <ListSubscriberResponse>`

        Usage:
        ::

            result = api.list_subscriber()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/subscribers",
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
        return unmarshal_ListSubscriberResponse(res.json())

    def list_subscriber_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListSubscriberRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Subscriber]:
        """
        List all subscribers.
        List all subscribers to Load Balancer alerts. By default, returns all subscribers to Load Balancer alerts for the Organization associated with the authentication token used for the request.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of subscribers in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :param name: Subscriber name to search for.
        :param organization_id: Filter subscribers by Organization ID.
        :param project_id: Filter subscribers by Project ID.
        :return: :class:`List[Subscriber] <List[Subscriber]>`

        Usage:
        ::

            result = api.list_subscriber_all()
        """

        return fetch_all_pages(
            type=ListSubscriberResponse,
            key="subscribers",
            fetcher=self.list_subscriber,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def update_subscriber(
        self,
        *,
        name: str,
        subscriber_id: str,
        zone: Optional[Zone] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
    ) -> Subscriber:
        """
        Update a subscriber.
        Update the parameters of a given subscriber (e.g. name, webhook configuration, email configuration), specified by its subscriber ID.
        :param name: Subscriber name.
        :param subscriber_id: Subscriber ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param email_config: Email address configuration.
        :param webhook_config: Webhook URI configuration.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.update_subscriber(
                name="example",
                subscriber_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/subscribers/{param_subscriber_id}",
            body=marshal_ZonedApiUpdateSubscriberRequest(
                ZonedApiUpdateSubscriberRequest(
                    name=name,
                    subscriber_id=subscriber_id,
                    zone=zone,
                    email_config=email_config,
                    webhook_config=webhook_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    def delete_subscriber(
        self,
        *,
        subscriber_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Delete a subscriber.
        Delete an existing subscriber, specified by its subscriber ID. Deleting a subscriber is permanent, and cannot be undone.
        :param subscriber_id: Subscriber ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.delete_subscriber(
                subscriber_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/lb/subscription/{param_subscriber_id}",
        )

        self._throw_on_error(res)

    def subscribe_to_lb(
        self,
        *,
        subscriber_id: str,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Subscribe a subscriber to alerts for a given Load Balancer.
        Subscribe an existing subscriber to alerts for a given Load Balancer.
        :param subscriber_id: Subscriber ID.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.subscribe_to_lb(
                subscriber_id="example",
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lb/{param_lb_id}/subscribe",
            body=marshal_ZonedApiSubscribeToLbRequest(
                ZonedApiSubscribeToLbRequest(
                    subscriber_id=subscriber_id,
                    lb_id=lb_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def unsubscribe_from_lb(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Unsubscribe a subscriber from alerts for a given Load Balancer.
        Unsubscribe a subscriber from alerts for a given Load Balancer. The subscriber is not deleted, and can be resubscribed in the future if necessary.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.unsubscribe_from_lb(
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/lb/{param_lb_id}/unsubscribe",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def list_lb_private_networks(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListLbPrivateNetworksResponse:
        """
        List Private Networks attached to a Load Balancer.
        List the Private Networks attached to a given Load Balancer, specified by its Load Balancer ID. The response is an array of Private Network objects, giving information including the status, configuration, name and creation date of each Private Network.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Private Network objects in the response.
        :param page_size: Number of objects to return.
        :param page: The page number to return, from the paginated results.
        :return: :class:`ListLbPrivateNetworksResponse <ListLbPrivateNetworksResponse>`

        Usage:
        ::

            result = api.list_lb_private_networks(
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/private-networks",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLbPrivateNetworksResponse(res.json())

    def list_lb_private_networks_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[PrivateNetwork]:
        """
        List Private Networks attached to a Load Balancer.
        List the Private Networks attached to a given Load Balancer, specified by its Load Balancer ID. The response is an array of Private Network objects, giving information including the status, configuration, name and creation date of each Private Network.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of Private Network objects in the response.
        :param page_size: Number of objects to return.
        :param page: The page number to return, from the paginated results.
        :return: :class:`List[PrivateNetwork] <List[PrivateNetwork]>`

        Usage:
        ::

            result = api.list_lb_private_networks_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListLbPrivateNetworksResponse,
            key="private_network",
            fetcher=self.list_lb_private_networks,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
            },
        )

    def attach_private_network(
        self,
        *,
        private_network_id: str,
        lb_id: str,
        zone: Optional[Zone] = None,
        static_config: Optional[PrivateNetworkStaticConfig] = None,
        dhcp_config: Optional[PrivateNetworkDHCPConfig] = None,
        ipam_config: Optional[PrivateNetworkIpamConfig] = None,
    ) -> PrivateNetwork:
        """
        Attach a Load Balancer to a Private Network.
        Attach a specified Load Balancer to a specified Private Network, defining a static or DHCP configuration for the Load Balancer on the network.
        :param private_network_id: Private Network ID.
        :param lb_id: Load Balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param static_config: Object containing an array of a local IP address for the Load Balancer on this Private Network.
        :param dhcp_config: Defines whether to let DHCP assign IP addresses.
        :param ipam_config: For internal use only.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = api.attach_private_network(
                private_network_id="example",
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/private-networks/{param_private_network_id}/attach",
            body=marshal_ZonedApiAttachPrivateNetworkRequest(
                ZonedApiAttachPrivateNetworkRequest(
                    private_network_id=private_network_id,
                    lb_id=lb_id,
                    zone=zone,
                    static_config=static_config,
                    dhcp_config=dhcp_config,
                    ipam_config=ipam_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    def detach_private_network(
        self,
        *,
        private_network_id: str,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> None:
        """
        Detach Load Balancer from Private Network.
        Detach a specified Load Balancer from a specified Private Network.
        :param private_network_id: Set your instance private network id.
        :param lb_id: Load balancer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.

        Usage:
        ::

            result = api.detach_private_network(
                private_network_id="example",
                lb_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/private-networks/{param_private_network_id}/detach",
            body={},
        )

        self._throw_on_error(res)


class LbV1API(API):
    """
    This API allows you to manage your load balancer service.
    """

    def list_lbs(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListLbsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListLbsResponse:
        """
        List load balancers.
        List load balancers.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Load Balancer name to filter for.
        :param order_by: Sort order of Load Balancers in the response.
        :param page_size: Number of Load Balancers to return.
        :param page: Page number to return, from the paginated results.
        :param organization_id: Organization ID to filter for, only Load Balancers from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancers from this Project will be returned.
        :return: :class:`ListLbsResponse <ListLbsResponse>`

        Usage:
        ::

            result = api.list_lbs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs",
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
        return unmarshal_ListLbsResponse(res.json())

    def list_lbs_all(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListLbsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Lb]:
        """
        List load balancers.
        List load balancers.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Load Balancer name to filter for.
        :param order_by: Sort order of Load Balancers in the response.
        :param page_size: Number of Load Balancers to return.
        :param page: Page number to return, from the paginated results.
        :param organization_id: Organization ID to filter for, only Load Balancers from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancers from this Project will be returned.
        :return: :class:`List[Lb] <List[Lb]>`

        Usage:
        ::

            result = api.list_lbs_all()
        """

        return fetch_all_pages(
            type=ListLbsResponse,
            key="lbs",
            fetcher=self.list_lbs,
            args={
                "region": region,
                "name": name,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def create_lb(
        self,
        *,
        type_: str,
        description: str,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        ip_id: Optional[str] = None,
        assign_flexible_ip: Optional[bool] = None,
        tags: Optional[List[str]] = None,
        ssl_compatibility_level: Optional[SSLCompatibilityLevel] = None,
    ) -> Lb:
        """
        Create a load balancer.
        Create a load balancer.
        :param type_: Load Balancer commercial offer type. Use the Load Balancer types endpoint to retrieve a list of available offer types.
        :param description: Description for the Load Balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Scaleway Organization to create the Load Balancer in.
        :param project_id: Scaleway Project to create the Load Balancer in.
        :param name: Name for the Load Balancer.
        :param ip_id: ID of an existing flexible IP address to attach to the Load Balancer.
        :param assign_flexible_ip: Defines whether to automatically assign a flexible public IP to lb. Default value is `false` (do not assign).
        :param tags: List of tags for the Load Balancer.
        :param ssl_compatibility_level: Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and do not need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.create_lb(
                type="example",
                description="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs",
            body=marshal_CreateLbRequest(
                CreateLbRequest(
                    type_=type_,
                    description=description,
                    region=region,
                    name=name or random_name(prefix="lb"),
                    ip_id=ip_id,
                    assign_flexible_ip=assign_flexible_ip,
                    tags=tags,
                    ssl_compatibility_level=ssl_compatibility_level,
                    organization_id=organization_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def get_lb(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Get a load balancer.
        Get a load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.get_lb(
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def wait_for_lb(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Lb, bool]] = None,
    ) -> Lb:
        """
        Get a load balancer.
        Get a load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.get_lb(
                lb_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in LB_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_lb,
            options=options,
            args={
                "lb_id": lb_id,
                "region": region,
            },
        )

    def update_lb(
        self,
        *,
        description: str,
        name: str,
        lb_id: str,
        region: Optional[Region] = None,
        tags: Optional[List[str]] = None,
        ssl_compatibility_level: Optional[SSLCompatibilityLevel] = None,
    ) -> Lb:
        """
        Update a load balancer.
        Update a load balancer.
        :param description: Load Balancer description.
        :param name: Load Balancer name.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: List of tags for the Load Balancer.
        :param ssl_compatibility_level: Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and don't need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.update_lb(
                description="example",
                name="example",
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}",
            body=marshal_UpdateLbRequest(
                UpdateLbRequest(
                    description=description,
                    name=name,
                    lb_id=lb_id,
                    region=region,
                    tags=tags,
                    ssl_compatibility_level=ssl_compatibility_level,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def delete_lb(
        self,
        *,
        release_ip: bool,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a load balancer.
        Delete a load balancer.
        :param release_ip: Defines whether the Load Balancer's flexible IP should be deleted. Set to true to release the flexible IP, or false to keep it available in your account for future Load Balancers.
        :param lb_id: ID of the Load Balancer to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_lb(
                release_ip=False,
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}",
            params={
                "release_ip": release_ip,
            },
        )

        self._throw_on_error(res)

    def migrate_lb(
        self,
        *,
        type_: str,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Migrate a load balancer.
        Migrate a load balancer.
        :param type_: Load Balancer type to migrate to (use the List all Load Balancer offer types endpoint to get a list of available offer types).
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.migrate_lb(
                type="example",
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/migrate",
            body=marshal_MigrateLbRequest(
                MigrateLbRequest(
                    type_=type_,
                    lb_id=lb_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def list_i_ps(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        ip_address: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListIpsResponse:
        """
        List IPs.
        List IPs.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of IP addresses to return.
        :param ip_address: IP address to filter for.
        :param organization_id: Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = api.list_i_ps()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/ips",
            params={
                "ip_address": ip_address,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIpsResponse(res.json())

    def list_i_ps_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        ip_address: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Ip]:
        """
        List IPs.
        List IPs.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of IP addresses to return.
        :param ip_address: IP address to filter for.
        :param organization_id: Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
        :return: :class:`List[Ip] <List[Ip]>`

        Usage:
        ::

            result = api.list_i_ps_all()
        """

        return fetch_all_pages(
            type=ListIpsResponse,
            key="ips",
            fetcher=self.list_i_ps,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "ip_address": ip_address,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def create_ip(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Create an IP.
        Create an IP.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Organization ID of the Organization where the IP address should be created.
        :param project_id: Project ID of the Project where the IP address should be created.
        :param reverse: Reverse DNS (domain name) for the IP address.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.create_ip()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/ips",
            body=marshal_CreateIpRequest(
                CreateIpRequest(
                    region=region,
                    reverse=reverse,
                    organization_id=organization_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    def get_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
    ) -> Ip:
        """
        Get an IP.
        Get an IP.
        :param ip_id: IP address ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.get_ip(
                ip_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    def release_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete an IP.
        Delete an IP.
        :param ip_id: IP address ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.release_ip(
                ip_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)

    def update_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Update an IP.
        Update an IP.
        :param ip_id: IP address ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param reverse: Reverse DNS (domain name) for the IP address.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.update_ip(
                ip_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/lb/v1/regions/{param_region}/ips/{param_ip_id}",
            body=marshal_UpdateIpRequest(
                UpdateIpRequest(
                    ip_id=ip_id,
                    region=region,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    def list_backends(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListBackendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListBackendsResponse:
        """
        List backends in a given load balancer.
        List backends in a given load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the backend to filter for.
        :param order_by: Sort order of backends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of backends to return.
        :return: :class:`ListBackendsResponse <ListBackendsResponse>`

        Usage:
        ::

            result = api.list_backends(
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/backends",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendsResponse(res.json())

    def list_backends_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListBackendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Backend]:
        """
        List backends in a given load balancer.
        List backends in a given load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the backend to filter for.
        :param order_by: Sort order of backends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of backends to return.
        :return: :class:`List[Backend] <List[Backend]>`

        Usage:
        ::

            result = api.list_backends_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListBackendsResponse,
            key="backends",
            fetcher=self.list_backends,
            args={
                "lb_id": lb_id,
                "region": region,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_backend(
        self,
        *,
        forward_port: int,
        health_check: HealthCheck,
        lb_id: str,
        sticky_sessions_cookie_name: str,
        region: Optional[Region] = None,
        send_proxy_v2: Optional[bool] = None,
        on_marked_down_action: Optional[OnMarkedDownAction] = None,
        forward_port_algorithm: Optional[ForwardPortAlgorithm] = None,
        forward_protocol: Optional[Protocol] = None,
        server_ip: Optional[List[str]] = None,
        name: Optional[str] = None,
        timeout_server: Optional[str] = None,
        timeout_connect: Optional[str] = None,
        timeout_tunnel: Optional[str] = None,
        sticky_sessions: Optional[StickySessionsType] = None,
        proxy_protocol: Optional[ProxyProtocol] = None,
        failover_host: Optional[str] = None,
        ssl_bridging: Optional[bool] = None,
        ignore_ssl_server_verify: Optional[bool] = None,
        redispatch_attempt_count: Optional[int] = None,
        max_retries: Optional[int] = None,
        max_connections: Optional[int] = None,
        timeout_queue: Optional[str] = None,
    ) -> Backend:
        """
        Create a backend in a given load balancer.
        Create a backend in a given load balancer.
        :param forward_port: Port to be used by the backend when forwarding traffic to backend servers.
        :param health_check: Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
        :param lb_id: Load Balancer ID.
        :param sticky_sessions_cookie_name: Cookie name for cookie-based sticky sessions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field.
        :param on_marked_down_action: Action to take when a backend server is marked as down.
        :param forward_port_algorithm: Load balancing algorithm to be used when determining which backend server to forward new traffic to.
        :param forward_protocol: Protocol to be used by the backend when forwarding traffic to backend servers.
        :param server_ip: List of backend server IP addresses (IPv4 or IPv6) the backend should forward traffic to.
        :param name: Name for the backend.
        :param timeout_server: Maximum allowed time for a backend server to process a request.
        :param timeout_connect: Maximum allowed time for establishing a connection to a backend server.
        :param timeout_tunnel: Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
        :param sticky_sessions: Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie TO stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
        :param proxy_protocol: Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
        :param failover_host: Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
        :param ssl_bridging: Defines whether to enable SSL bridging between the Load Balancer and backend servers.
        :param ignore_ssl_server_verify: Defines whether the server certificate verification should be ignored.
        :param redispatch_attempt_count: Whether to use another backend server on each attempt.
        :param max_retries: Number of retries when a backend server connection failed.
        :param max_connections: Maximum number of connections allowed per backend server.
        :param timeout_queue: Maximum time for a request to be left pending in queue when `max_connections` is reached.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.create_backend(
                forward_port=1,
                health_check=HealthCheck(),
                lb_id="example",
                sticky_sessions_cookie_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/backends",
            body=marshal_CreateBackendRequest(
                CreateBackendRequest(
                    forward_port=forward_port,
                    health_check=health_check,
                    lb_id=lb_id,
                    sticky_sessions_cookie_name=sticky_sessions_cookie_name,
                    region=region,
                    send_proxy_v2=send_proxy_v2,
                    on_marked_down_action=on_marked_down_action,
                    forward_port_algorithm=forward_port_algorithm,
                    forward_protocol=forward_protocol,
                    server_ip=server_ip,
                    name=name or random_name(prefix="lbb"),
                    timeout_server=timeout_server,
                    timeout_connect=timeout_connect,
                    timeout_tunnel=timeout_tunnel,
                    sticky_sessions=sticky_sessions,
                    proxy_protocol=proxy_protocol,
                    failover_host=failover_host,
                    ssl_bridging=ssl_bridging,
                    ignore_ssl_server_verify=ignore_ssl_server_verify,
                    redispatch_attempt_count=redispatch_attempt_count,
                    max_retries=max_retries,
                    max_connections=max_connections,
                    timeout_queue=timeout_queue,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def get_backend(
        self,
        *,
        backend_id: str,
        region: Optional[Region] = None,
    ) -> Backend:
        """
        Get a backend in a given load balancer.
        Get a backend in a given load balancer.
        :param backend_id: Backend ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.get_backend(
                backend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def update_backend(
        self,
        *,
        forward_port: int,
        name: str,
        backend_id: str,
        sticky_sessions_cookie_name: str,
        region: Optional[Region] = None,
        timeout_connect: Optional[str] = None,
        on_marked_down_action: Optional[OnMarkedDownAction] = None,
        forward_port_algorithm: Optional[ForwardPortAlgorithm] = None,
        send_proxy_v2: Optional[bool] = None,
        timeout_server: Optional[str] = None,
        forward_protocol: Optional[Protocol] = None,
        timeout_tunnel: Optional[str] = None,
        sticky_sessions: Optional[StickySessionsType] = None,
        proxy_protocol: Optional[ProxyProtocol] = None,
        failover_host: Optional[str] = None,
        ssl_bridging: Optional[bool] = None,
        ignore_ssl_server_verify: Optional[bool] = None,
        redispatch_attempt_count: Optional[int] = None,
        max_retries: Optional[int] = None,
        max_connections: Optional[int] = None,
        timeout_queue: Optional[str] = None,
    ) -> Backend:
        """
        Update a backend in a given load balancer.
        Update a backend in a given load balancer.
        :param forward_port: Port to be used by the backend when forwarding traffic to backend servers.
        :param name: Backend name.
        :param backend_id: Backend ID.
        :param sticky_sessions_cookie_name: Cookie name for cookie-based sticky sessions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param timeout_connect: Maximum allowed time for establishing a connection to a backend server.
        :param on_marked_down_action: Action to take when a backend server is marked as down.
        :param forward_port_algorithm: Load balancing algorithm to be used when determining which backend server to forward new traffic to.
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field.
        :param timeout_server: Maximum allowed time for a backend server to process a request.
        :param forward_protocol: Protocol to be used by the backend when forwarding traffic to backend servers.
        :param timeout_tunnel: Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
        :param sticky_sessions: Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
        :param proxy_protocol: Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
        :param failover_host: Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
        :param ssl_bridging: Defines whether to enable SSL bridging between the Load Balancer and backend servers.
        :param ignore_ssl_server_verify: Defines whether the server certificate verification should be ignored.
        :param redispatch_attempt_count: Whether to use another backend server on each attempt.
        :param max_retries: Number of retries when a backend server connection failed.
        :param max_connections: Maximum number of connections allowed per backend server.
        :param timeout_queue: Maximum time for a request to be left pending in queue when `max_connections` is reached.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.update_backend(
                forward_port=1,
                name="example",
                backend_id="example",
                sticky_sessions_cookie_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}",
            body=marshal_UpdateBackendRequest(
                UpdateBackendRequest(
                    forward_port=forward_port,
                    name=name,
                    backend_id=backend_id,
                    sticky_sessions_cookie_name=sticky_sessions_cookie_name,
                    region=region,
                    timeout_connect=timeout_connect,
                    on_marked_down_action=on_marked_down_action,
                    forward_port_algorithm=forward_port_algorithm,
                    send_proxy_v2=send_proxy_v2,
                    timeout_server=timeout_server,
                    forward_protocol=forward_protocol,
                    timeout_tunnel=timeout_tunnel,
                    sticky_sessions=sticky_sessions,
                    proxy_protocol=proxy_protocol,
                    failover_host=failover_host,
                    ssl_bridging=ssl_bridging,
                    ignore_ssl_server_verify=ignore_ssl_server_verify,
                    redispatch_attempt_count=redispatch_attempt_count,
                    max_retries=max_retries,
                    max_connections=max_connections,
                    timeout_queue=timeout_queue,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def delete_backend(
        self,
        *,
        backend_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a backend in a given load balancer.
        Delete a backend in a given load balancer.
        :param backend_id: ID of the backend to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_backend(
                backend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)

    def add_backend_servers(
        self,
        *,
        backend_id: str,
        region: Optional[Region] = None,
        server_ip: Optional[List[str]] = None,
    ) -> Backend:
        """
        Add a set of servers in a given backend.
        Add a set of servers in a given backend.
        :param backend_id: Backend ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param server_ip: List of IP addresses to add to backend servers.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.add_backend_servers(
                backend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}/servers",
            body=marshal_AddBackendServersRequest(
                AddBackendServersRequest(
                    backend_id=backend_id,
                    region=region,
                    server_ip=server_ip,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def remove_backend_servers(
        self,
        *,
        backend_id: str,
        region: Optional[Region] = None,
        server_ip: Optional[List[str]] = None,
    ) -> Backend:
        """
        Remove a set of servers for a given backend.
        Remove a set of servers for a given backend.
        :param backend_id: Backend ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param server_ip: List of IP addresses to remove from backend servers.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.remove_backend_servers(
                backend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}/servers",
            body=marshal_RemoveBackendServersRequest(
                RemoveBackendServersRequest(
                    backend_id=backend_id,
                    region=region,
                    server_ip=server_ip,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def set_backend_servers(
        self,
        *,
        backend_id: str,
        region: Optional[Region] = None,
        server_ip: Optional[List[str]] = None,
    ) -> Backend:
        """
        Define all servers in a given backend.
        Define all servers in a given backend.
        :param backend_id: Backend ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param server_ip: List of IP addresses for backend servers. Any other existing backend servers will be removed.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.set_backend_servers(
                backend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}/servers",
            body=marshal_SetBackendServersRequest(
                SetBackendServersRequest(
                    backend_id=backend_id,
                    region=region,
                    server_ip=server_ip,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def update_health_check(
        self,
        *,
        check_send_proxy: bool,
        port: int,
        backend_id: str,
        check_max_retries: int,
        region: Optional[Region] = None,
        check_delay: Optional[str] = None,
        check_timeout: Optional[str] = None,
        tcp_config: Optional[HealthCheckTcpConfig] = None,
        mysql_config: Optional[HealthCheckMysqlConfig] = None,
        pgsql_config: Optional[HealthCheckPgsqlConfig] = None,
        ldap_config: Optional[HealthCheckLdapConfig] = None,
        redis_config: Optional[HealthCheckRedisConfig] = None,
        http_config: Optional[HealthCheckHttpConfig] = None,
        https_config: Optional[HealthCheckHttpsConfig] = None,
        transient_check_delay: Optional[str] = None,
    ) -> HealthCheck:
        """
        Update an health check for a given backend.
        Update an health check for a given backend.
        :param check_send_proxy: Defines whether proxy protocol should be activated for the health check.
        :param port: Port to use for the backend server health check.
        :param backend_id: Backend ID.
        :param check_max_retries: Number of consecutive unsuccessful health checks after which the server will be considered dead.
        :param region: Region to target. If none is passed will use default region from the config.
        :param check_delay: Time to wait between two consecutive health checks.
        :param check_timeout: Maximum time a backend server has to reply to the health check.
        :param tcp_config: Object to configure a basic TCP health check.
        :param mysql_config: Object to configure a MySQL health check. The check requires MySQL >=3.22, for older versions, use a TCP health check.
        :param pgsql_config: Object to configure a PostgreSQL health check.
        :param ldap_config: Object to configure an LDAP health check. The response is analyzed to find the LDAPv3 response message.
        :param redis_config: Object to configure a Redis health check. The response is analyzed to find the +PONG response message.
        :param http_config: Object to configure an HTTP health check.
        :param https_config: Object to configure an HTTPS health check.
        :param transient_check_delay: Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
        :return: :class:`HealthCheck <HealthCheck>`

        Usage:
        ::

            result = api.update_health_check(
                check_send_proxy=False,
                port=1,
                backend_id="example",
                check_max_retries=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}/healthcheck",
            body=marshal_UpdateHealthCheckRequest(
                UpdateHealthCheckRequest(
                    check_send_proxy=check_send_proxy,
                    check_max_retries=check_max_retries,
                    port=port,
                    backend_id=backend_id,
                    region=region,
                    check_delay=check_delay,
                    check_timeout=check_timeout,
                    transient_check_delay=transient_check_delay,
                    tcp_config=tcp_config,
                    mysql_config=mysql_config,
                    pgsql_config=pgsql_config,
                    ldap_config=ldap_config,
                    redis_config=redis_config,
                    http_config=http_config,
                    https_config=https_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_HealthCheck(res.json())

    def list_frontends(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListFrontendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListFrontendsResponse:
        """
        List frontends in a given load balancer.
        List frontends in a given load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the frontend to filter for.
        :param order_by: Sort order of frontends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of frontends to return.
        :return: :class:`ListFrontendsResponse <ListFrontendsResponse>`

        Usage:
        ::

            result = api.list_frontends(
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/frontends",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListFrontendsResponse(res.json())

    def list_frontends_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListFrontendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Frontend]:
        """
        List frontends in a given load balancer.
        List frontends in a given load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the frontend to filter for.
        :param order_by: Sort order of frontends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of frontends to return.
        :return: :class:`List[Frontend] <List[Frontend]>`

        Usage:
        ::

            result = api.list_frontends_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListFrontendsResponse,
            key="frontends",
            fetcher=self.list_frontends,
            args={
                "lb_id": lb_id,
                "region": region,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_frontend(
        self,
        *,
        enable_http3: bool,
        backend_id: str,
        inbound_port: int,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        timeout_client: Optional[str] = None,
        certificate_id: Optional[str] = None,
        certificate_ids: Optional[List[str]] = None,
    ) -> Frontend:
        """
        Create a frontend in a given load balancer.
        Create a frontend in a given load balancer.
        :param enable_http3: Defines whether to enable HTTP/3 protocol on the frontend.
        :param backend_id: Backend ID (ID of the backend the frontend should pass traffic to).
        :param inbound_port: Port the frontend should listen on.
        :param lb_id: Load Balancer ID (ID of the Load Balancer to attach the frontend to).
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the frontend.
        :param timeout_client: Maximum allowed inactivity time on the client side.
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array.
        :param certificate_ids: List of SSL/TLS certificate IDs to bind to the frontend.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.create_frontend(
                enable_http3=False,
                backend_id="example",
                inbound_port=1,
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/frontends",
            body=marshal_CreateFrontendRequest(
                CreateFrontendRequest(
                    enable_http3=enable_http3,
                    backend_id=backend_id,
                    inbound_port=inbound_port,
                    lb_id=lb_id,
                    region=region,
                    name=name or random_name(prefix="lbf"),
                    timeout_client=timeout_client,
                    certificate_id=certificate_id,
                    certificate_ids=certificate_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    def get_frontend(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
    ) -> Frontend:
        """
        Get a frontend.
        Get a frontend.
        :param frontend_id: Frontend ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.get_frontend(
                frontend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    def update_frontend(
        self,
        *,
        enable_http3: bool,
        backend_id: str,
        inbound_port: int,
        name: str,
        frontend_id: str,
        region: Optional[Region] = None,
        timeout_client: Optional[str] = None,
        certificate_id: Optional[str] = None,
        certificate_ids: Optional[List[str]] = None,
    ) -> Frontend:
        """
        Update a frontend.
        Update a frontend.
        :param enable_http3: Defines whether to enable HTTP/3 protocol on the frontend.
        :param backend_id: Backend ID (ID of the backend the frontend should pass traffic to).
        :param inbound_port: Port the frontend should listen on.
        :param name: Frontend name.
        :param frontend_id: Frontend ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param timeout_client: Maximum allowed inactivity time on the client side.
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array.
        :param certificate_ids: List of SSL/TLS certificate IDs to bind to the frontend.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.update_frontend(
                enable_http3=False,
                backend_id="example",
                inbound_port=1,
                name="example",
                frontend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}",
            body=marshal_UpdateFrontendRequest(
                UpdateFrontendRequest(
                    enable_http3=enable_http3,
                    backend_id=backend_id,
                    inbound_port=inbound_port,
                    name=name,
                    frontend_id=frontend_id,
                    region=region,
                    timeout_client=timeout_client,
                    certificate_id=certificate_id,
                    certificate_ids=certificate_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    def delete_frontend(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a frontend.
        Delete a frontend.
        :param frontend_id: ID of the frontend to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_frontend(
                frontend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)

    def list_routes(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> ListRoutesResponse:
        """
        List all backend redirections.
        List all backend redirections.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of routes in the response.
        :param page_size: The number of route objects to return.
        :param page: The page number to return, from the paginated results.
        :param frontend_id: Frontend ID to filter for, only Routes from this Frontend will be returned.
        :return: :class:`ListRoutesResponse <ListRoutesResponse>`

        Usage:
        ::

            result = api.list_routes()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/routes",
            params={
                "frontend_id": frontend_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRoutesResponse(res.json())

    def list_routes_all(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> List[Route]:
        """
        List all backend redirections.
        List all backend redirections.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of routes in the response.
        :param page_size: The number of route objects to return.
        :param page: The page number to return, from the paginated results.
        :param frontend_id: Frontend ID to filter for, only Routes from this Frontend will be returned.
        :return: :class:`List[Route] <List[Route]>`

        Usage:
        ::

            result = api.list_routes_all()
        """

        return fetch_all_pages(
            type=ListRoutesResponse,
            key="routes",
            fetcher=self.list_routes,
            args={
                "region": region,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "frontend_id": frontend_id,
            },
        )

    def create_route(
        self,
        *,
        backend_id: str,
        frontend_id: str,
        region: Optional[Region] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Create a backend redirection.
        Create a backend redirection.
        :param backend_id: ID of the target backend for the route.
        :param frontend_id: ID of the source frontend to create the route on.
        :param region: Region to target. If none is passed will use default region from the config.
        :param match: Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.create_route(
                backend_id="example",
                frontend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/routes",
            body=marshal_CreateRouteRequest(
                CreateRouteRequest(
                    backend_id=backend_id,
                    frontend_id=frontend_id,
                    region=region,
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    def get_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
    ) -> Route:
        """
        Get single backend redirection.
        Get single backend redirection.
        :param route_id: Route ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.get_route(
                route_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    def update_route(
        self,
        *,
        backend_id: str,
        route_id: str,
        region: Optional[Region] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Edit a backend redirection.
        Edit a backend redirection.
        :param backend_id: ID of the target backend for the route.
        :param route_id: Route ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param match: Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.update_route(
                backend_id="example",
                route_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/routes/{param_route_id}",
            body=marshal_UpdateRouteRequest(
                UpdateRouteRequest(
                    backend_id=backend_id,
                    route_id=route_id,
                    region=region,
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    def delete_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a backend redirection.
        Delete a backend redirection.
        :param route_id: Route ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_route(
                route_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/routes/{param_route_id}",
        )

        self._throw_on_error(res)

    def get_lb_stats(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        backend_id: Optional[str] = None,
    ) -> LbStats:
        """
        Get usage statistics of a given load balancer.
        Get usage statistics of a given load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param backend_id: ID of the backend.
        :return: :class:`LbStats <LbStats>`
        :deprecated

        Usage:
        ::

            result = api.get_lb_stats(
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/stats",
            params={
                "backend_id": backend_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_LbStats(res.json())

    def list_backend_stats(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        backend_id: Optional[str] = None,
    ) -> ListBackendStatsResponse:
        """
        List backend server statistics.
        List backend server statistics.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of items to return.
        :param backend_id: ID of the backend.
        :return: :class:`ListBackendStatsResponse <ListBackendStatsResponse>`

        Usage:
        ::

            result = api.list_backend_stats(
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/backend-stats",
            params={
                "backend_id": backend_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendStatsResponse(res.json())

    def list_backend_stats_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        backend_id: Optional[str] = None,
    ) -> List[BackendServerStats]:
        """
        List backend server statistics.
        List backend server statistics.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of items to return.
        :param backend_id: ID of the backend.
        :return: :class:`List[BackendServerStats] <List[BackendServerStats]>`

        Usage:
        ::

            result = api.list_backend_stats_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListBackendStatsResponse,
            key="backend_servers_stats",
            fetcher=self.list_backend_stats,
            args={
                "lb_id": lb_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "backend_id": backend_id,
            },
        )

    def list_acls(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListAclRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> ListAclResponse:
        """
        List ACL for a given frontend.
        List ACL for a given frontend.
        :param frontend_id: Frontend ID (ACLs attached to this frontend will be returned in the response).
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of ACLs in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of ACLs to return.
        :param name: ACL name to filter for.
        :return: :class:`ListAclResponse <ListAclResponse>`

        Usage:
        ::

            result = api.list_acls(
                frontend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}/acls",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAclResponse(res.json())

    def list_acls_all(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListAclRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> List[Acl]:
        """
        List ACL for a given frontend.
        List ACL for a given frontend.
        :param frontend_id: Frontend ID (ACLs attached to this frontend will be returned in the response).
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of ACLs in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of ACLs to return.
        :param name: ACL name to filter for.
        :return: :class:`List[Acl] <List[Acl]>`

        Usage:
        ::

            result = api.list_acls_all(
                frontend_id="example",
            )
        """

        return fetch_all_pages(
            type=ListAclResponse,
            key="acls",
            fetcher=self.list_acls,
            args={
                "frontend_id": frontend_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
            },
        )

    def create_acl(
        self,
        *,
        description: str,
        index: int,
        match: AclMatch,
        action: AclAction,
        frontend_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
    ) -> Acl:
        """
        Create an ACL for a given frontend.
        Create an ACL for a given frontend.
        :param description: ACL description.
        :param index: Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
        :param match: ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
        :param action: Action to take when incoming traffic matches an ACL filter.
        :param frontend_id: Frontend ID to attach the ACL to.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: ACL name.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.create_acl(
                description="example",
                index=1,
                match=AclMatch(),
                action=AclAction(),
                frontend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}/acls",
            body=marshal_CreateAclRequest(
                CreateAclRequest(
                    description=description,
                    index=index,
                    match=match,
                    action=action,
                    frontend_id=frontend_id,
                    region=region,
                    name=name or random_name(prefix="acl"),
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def get_acl(
        self,
        *,
        acl_id: str,
        region: Optional[Region] = None,
    ) -> Acl:
        """
        Get an ACL.
        Get an ACL.
        :param acl_id: ACL ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.get_acl(
                acl_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def update_acl(
        self,
        *,
        index: int,
        match: AclMatch,
        action: AclAction,
        name: str,
        acl_id: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
    ) -> Acl:
        """
        Update an ACL.
        Update an ACL.
        :param index: Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
        :param match: ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
        :param action: Action to take when incoming traffic matches an ACL filter.
        :param name: ACL name.
        :param acl_id: ACL ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: ACL description.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.update_acl(
                index=1,
                match=AclMatch(),
                action=AclAction(),
                name="example",
                acl_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/acls/{param_acl_id}",
            body=marshal_UpdateAclRequest(
                UpdateAclRequest(
                    index=index,
                    match=match,
                    action=action,
                    name=name,
                    acl_id=acl_id,
                    region=region,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def delete_acl(
        self,
        *,
        acl_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete an ACL.
        Delete an ACL.
        :param acl_id: ACL ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_acl(
                acl_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)

    def create_certificate(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig] = None,
        custom_certificate: Optional[CreateCertificateRequestCustomCertificate] = None,
    ) -> Certificate:
        """
        Create a TLS certificate.
        Generate a new TLS certificate using Let's Encrypt or import your certificate.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name for the certificate.
        :param letsencrypt: Object to define a new Let's Encrypt certificate to be generated.
        :param custom_certificate: Object to define an existing custom certificate to be imported.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.create_certificate(
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/certificates",
            body=marshal_CreateCertificateRequest(
                CreateCertificateRequest(
                    lb_id=lb_id,
                    region=region,
                    name=name or random_name(prefix="certificate"),
                    letsencrypt=letsencrypt,
                    custom_certificate=custom_certificate,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    def list_certificates(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListCertificatesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> ListCertificatesResponse:
        """
        List all TLS certificates on a given load balancer.
        List all TLS certificates on a given load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of certificates in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of certificates to return.
        :param name: Certificate name to filter for, only certificates of this name will be returned.
        :return: :class:`ListCertificatesResponse <ListCertificatesResponse>`

        Usage:
        ::

            result = api.list_certificates(
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/certificates",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCertificatesResponse(res.json())

    def list_certificates_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListCertificatesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> List[Certificate]:
        """
        List all TLS certificates on a given load balancer.
        List all TLS certificates on a given load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of certificates in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of certificates to return.
        :param name: Certificate name to filter for, only certificates of this name will be returned.
        :return: :class:`List[Certificate] <List[Certificate]>`

        Usage:
        ::

            result = api.list_certificates_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListCertificatesResponse,
            key="certificates",
            fetcher=self.list_certificates,
            args={
                "lb_id": lb_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
            },
        )

    def get_certificate(
        self,
        *,
        certificate_id: str,
        region: Optional[Region] = None,
    ) -> Certificate:
        """
        Get a TLS certificate.
        Get a TLS certificate.
        :param certificate_id: Certificate ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.get_certificate(
                certificate_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    def wait_for_certificate(
        self,
        *,
        certificate_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Certificate, bool]] = None,
    ) -> Certificate:
        """
        Get a TLS certificate.
        Get a TLS certificate.
        :param certificate_id: Certificate ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.get_certificate(
                certificate_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in CERTIFICATE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_certificate,
            options=options,
            args={
                "certificate_id": certificate_id,
                "region": region,
            },
        )

    def update_certificate(
        self,
        *,
        name: str,
        certificate_id: str,
        region: Optional[Region] = None,
    ) -> Certificate:
        """
        Update a TLS certificate.
        Update a TLS certificate.
        :param name: Certificate name.
        :param certificate_id: Certificate ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.update_certificate(
                name="example",
                certificate_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/certificates/{param_certificate_id}",
            body=marshal_UpdateCertificateRequest(
                UpdateCertificateRequest(
                    name=name,
                    certificate_id=certificate_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    def delete_certificate(
        self,
        *,
        certificate_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a TLS certificate.
        Delete a TLS certificate.
        :param certificate_id: Certificate ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_certificate(
                certificate_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)

    def list_lb_types(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListLbTypesResponse:
        """
        List all load balancer offer type.
        List all load balancer offer type.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`ListLbTypesResponse <ListLbTypesResponse>`

        Usage:
        ::

            result = api.list_lb_types()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lb-types",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLbTypesResponse(res.json())

    def list_lb_types_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[LbType]:
        """
        List all load balancer offer type.
        List all load balancer offer type.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`List[LbType] <List[LbType]>`

        Usage:
        ::

            result = api.list_lb_types_all()
        """

        return fetch_all_pages(
            type=ListLbTypesResponse,
            key="lb_types",
            fetcher=self.list_lb_types,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_subscriber(
        self,
        *,
        name: str,
        region: Optional[Region] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Subscriber:
        """
        Create a subscriber, webhook or email.
        Create a subscriber, webhook or email.
        :param name: Subscriber name.
        :param region: Region to target. If none is passed will use default region from the config.
        :param email_config: Email address configuration.
        :param webhook_config: WebHook URI configuration.
        :param organization_id: Organization ID to create the subscriber in.
        :param project_id: Project ID to create the subscriber in.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.create_subscriber(
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/subscribers",
            body=marshal_CreateSubscriberRequest(
                CreateSubscriberRequest(
                    name=name,
                    region=region,
                    organization_id=organization_id,
                    project_id=project_id,
                    email_config=email_config,
                    webhook_config=webhook_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    def get_subscriber(
        self,
        *,
        subscriber_id: str,
        region: Optional[Region] = None,
    ) -> Subscriber:
        """
        Get a subscriber.
        Get a subscriber.
        :param subscriber_id: Subscriber ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.get_subscriber(
                subscriber_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/subscribers/{param_subscriber_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    def list_subscriber(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListSubscriberRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListSubscriberResponse:
        """
        List all subscriber.
        List all subscriber.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of subscribers in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :param name: Subscriber name to search for.
        :param organization_id: Filter subscribers by Organization ID.
        :param project_id: Filter subscribers by Project ID.
        :return: :class:`ListSubscriberResponse <ListSubscriberResponse>`

        Usage:
        ::

            result = api.list_subscriber()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/subscribers",
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
        return unmarshal_ListSubscriberResponse(res.json())

    def list_subscriber_all(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListSubscriberRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Subscriber]:
        """
        List all subscriber.
        List all subscriber.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of subscribers in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :param name: Subscriber name to search for.
        :param organization_id: Filter subscribers by Organization ID.
        :param project_id: Filter subscribers by Project ID.
        :return: :class:`List[Subscriber] <List[Subscriber]>`

        Usage:
        ::

            result = api.list_subscriber_all()
        """

        return fetch_all_pages(
            type=ListSubscriberResponse,
            key="subscribers",
            fetcher=self.list_subscriber,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def update_subscriber(
        self,
        *,
        name: str,
        subscriber_id: str,
        region: Optional[Region] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
    ) -> Subscriber:
        """
        Update a subscriber.
        Update a subscriber.
        :param name: Subscriber name.
        :param subscriber_id: Subscriber ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param email_config: Email address configuration.
        :param webhook_config: Webhook URI configuration.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.update_subscriber(
                name="example",
                subscriber_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/subscribers/{param_subscriber_id}",
            body=marshal_UpdateSubscriberRequest(
                UpdateSubscriberRequest(
                    name=name,
                    subscriber_id=subscriber_id,
                    region=region,
                    email_config=email_config,
                    webhook_config=webhook_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    def delete_subscriber(
        self,
        *,
        subscriber_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a subscriber.
        Delete a subscriber.
        :param subscriber_id: Subscriber ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_subscriber(
                subscriber_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/lb/subscriber/{param_subscriber_id}",
        )

        self._throw_on_error(res)

    def subscribe_to_lb(
        self,
        *,
        subscriber_id: str,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Subscribe a subscriber to a given load balancer.
        Subscribe a subscriber to a given load balancer.
        :param subscriber_id: Subscriber ID.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.subscribe_to_lb(
                subscriber_id="example",
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lb/{param_lb_id}/subscribe",
            body=marshal_SubscribeToLbRequest(
                SubscribeToLbRequest(
                    subscriber_id=subscriber_id,
                    lb_id=lb_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def unsubscribe_from_lb(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Unsubscribe a subscriber from a given load balancer.
        Unsubscribe a subscriber from a given load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.unsubscribe_from_lb(
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/lb/{param_lb_id}/unsubscribe",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def list_lb_private_networks(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListLbPrivateNetworksResponse:
        """
        List attached private network of load balancer.
        List attached private network of load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of Private Network objects in the response.
        :param page_size: Number of objects to return.
        :param page: The page number to return, from the paginated results.
        :return: :class:`ListLbPrivateNetworksResponse <ListLbPrivateNetworksResponse>`

        Usage:
        ::

            result = api.list_lb_private_networks(
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/private-networks",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLbPrivateNetworksResponse(res.json())

    def list_lb_private_networks_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[PrivateNetwork]:
        """
        List attached private network of load balancer.
        List attached private network of load balancer.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of Private Network objects in the response.
        :param page_size: Number of objects to return.
        :param page: The page number to return, from the paginated results.
        :return: :class:`List[PrivateNetwork] <List[PrivateNetwork]>`

        Usage:
        ::

            result = api.list_lb_private_networks_all(
                lb_id="example",
            )
        """

        return fetch_all_pages(
            type=ListLbPrivateNetworksResponse,
            key="private_network",
            fetcher=self.list_lb_private_networks,
            args={
                "lb_id": lb_id,
                "region": region,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
            },
        )

    def attach_private_network(
        self,
        *,
        private_network_id: str,
        lb_id: str,
        region: Optional[Region] = None,
        static_config: Optional[PrivateNetworkStaticConfig] = None,
        dhcp_config: Optional[PrivateNetworkDHCPConfig] = None,
        ipam_config: Optional[PrivateNetworkIpamConfig] = None,
    ) -> PrivateNetwork:
        """
        Add load balancer on instance private network.
        Add load balancer on instance private network.
        :param private_network_id: Private Network ID.
        :param lb_id: Load Balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param static_config: Object containing an array of a local IP address for the Load Balancer on this Private Network.
        :param dhcp_config: Defines whether to let DHCP assign IP addresses.
        :param ipam_config: For internal use only.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = api.attach_private_network(
                private_network_id="example",
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/private-networks/{param_private_network_id}/attach",
            body=marshal_AttachPrivateNetworkRequest(
                AttachPrivateNetworkRequest(
                    private_network_id=private_network_id,
                    lb_id=lb_id,
                    region=region,
                    static_config=static_config,
                    dhcp_config=dhcp_config,
                    ipam_config=ipam_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    def detach_private_network(
        self,
        *,
        private_network_id: str,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Remove load balancer of private network.
        Remove load balancer of private network.
        :param private_network_id: Set your instance private network id.
        :param lb_id: Load balancer ID.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.detach_private_network(
                private_network_id="example",
                lb_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/private-networks/{param_private_network_id}/detach",
            body={},
        )

        self._throw_on_error(res)
