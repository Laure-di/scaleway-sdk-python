from typing import Optional
from scaleway_core.bridge import Zone
from scaleway_core.utils import validate_path_param
from .api import InstanceV1API
from .custom_marshalling import marshal_GetServerUserDataRequest
from .custom_types import GetServerUserDataRequest


class InstanceUtilsV1API(InstanceV1API):
    """
    This API extends InstanceV1API by adding utility methods for managing Instance resources,
    such as getting and setting server user data, while inheriting all methods of InstanceV1API.
    """

    def get_server_user_data(self, server_id: str, key: str, zone: Optional[Zone] = None):
        """
        GetServerUserData gets the content of a user data on a server for the given key.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id:
        :param key:
        :return: A plain text response with data user information

        Usage:
        ::

            result = api.get_server_user_data(
                server_id="example",
                key="example",
            )
        """
        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/user_data/{key}",
            body=marshal_GetServerUserDataRequest(
                GetServerUserDataRequest(
                    zone=zone,
                    server_id=server_id,
                    key=key,
                ),
                self.client,
            ),
        )
        self._throw_on_error(res)
        return res

    def set_server_user_data(self, server_id: str, key: str, content: bytes, zone: Optional[Zone] = None):
        """
        Sets the content of a user data on a server for the given key.
        :param zone: Zone to target. If none is passed, it will use the default zone from the config.
        :param server_id: The ID of the server.
        :param key: The user data key.
        :param content: The content to set as user data in bytes.
        :return: A plain text response confirming the operation.
        """
        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        headers = {
            'Content-Type': 'text/plain',
        }
        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/user_data/{key}",
            body=content,
            headers=headers,
        )

        self._throw_on_error(res)
        return res
