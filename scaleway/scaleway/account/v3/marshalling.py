# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    ListProjectsResponse,
    Project,
    ProjectApiCreateProjectRequest,
    ProjectApiUpdateProjectRequest,
)


def unmarshal_Project(data: Any) -> Project:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Project' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Project(**args)


def unmarshal_ListProjectsResponse(data: Any) -> ListProjectsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListProjectsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("projects", None)
    args["projects"] = (
        [unmarshal_Project(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListProjectsResponse(**args)


def marshal_ProjectApiCreateProjectRequest(
    request: ProjectApiCreateProjectRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "name": request.name,
        "organization_id": request.organization_id or defaults.default_organization_id,
    }


def marshal_ProjectApiUpdateProjectRequest(
    request: ProjectApiUpdateProjectRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "name": request.name,
    }