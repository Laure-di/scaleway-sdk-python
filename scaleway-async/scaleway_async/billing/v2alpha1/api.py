# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    ScwFile,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    DownloadInvoiceRequestFileType,
    InvoiceType,
    ListInvoicesRequestOrderBy,
    GetConsumptionResponse,
    Invoice,
    ListInvoicesResponse,
)
from .marshalling import (
    unmarshal_GetConsumptionResponse,
    unmarshal_ListInvoicesResponse,
)


class BillingV2Alpha1API(API):
    """
    This API allows you to query your consumption.
    """

    async def get_consumption(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> GetConsumptionResponse:
        """
        Get current month's consumption.
        The consumption reflects the amount of money you have spent for the products you have used.
        The consumption value is monetary and is not computed in real time.
        :param organization_id: Filter by organization ID.
        :return: :class:`GetConsumptionResponse <GetConsumptionResponse>`

        Usage:
        ::

            result = await api.get_consumption()
        """

        res = self._request(
            "GET",
            "/billing/v2alpha1/consumption",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetConsumptionResponse(res.json())

    async def list_invoices(
        self,
        *,
        organization_id: Optional[str] = None,
        started_after: Optional[datetime] = None,
        started_before: Optional[datetime] = None,
        invoice_type: Optional[InvoiceType] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListInvoicesRequestOrderBy] = None,
    ) -> ListInvoicesResponse:
        """
        List invoices.
        List all your invoices, filtering by `start_date` and `invoice_type`. Each invoice has its own ID.
        :param organization_id: Organization ID to filter for, only invoices from this Organization will be returned.
        :param started_after: Invoice's `start_date` is greater or equal to `started_after`.
        :param started_before: Invoice's `start_date` precedes `started_before`.
        :param invoice_type: Invoice type. It can either be `periodic` or `purchase`.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param order_by: How invoices are ordered in the response.
        :return: :class:`ListInvoicesResponse <ListInvoicesResponse>`

        Usage:
        ::

            result = await api.list_invoices()
        """

        res = self._request(
            "GET",
            "/billing/v2alpha1/invoices",
            params={
                "invoice_type": invoice_type,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "started_after": started_after,
                "started_before": started_before,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInvoicesResponse(res.json())

    async def list_invoices_all(
        self,
        *,
        organization_id: Optional[str] = None,
        started_after: Optional[datetime] = None,
        started_before: Optional[datetime] = None,
        invoice_type: Optional[InvoiceType] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListInvoicesRequestOrderBy] = None,
    ) -> List[Invoice]:
        """
        List invoices.
        List all your invoices, filtering by `start_date` and `invoice_type`. Each invoice has its own ID.
        :param organization_id: Organization ID to filter for, only invoices from this Organization will be returned.
        :param started_after: Invoice's `start_date` is greater or equal to `started_after`.
        :param started_before: Invoice's `start_date` precedes `started_before`.
        :param invoice_type: Invoice type. It can either be `periodic` or `purchase`.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param order_by: How invoices are ordered in the response.
        :return: :class:`List[Invoice] <List[Invoice]>`

        Usage:
        ::

            result = await api.list_invoices_all()
        """

        return await fetch_all_pages_async(
            type=ListInvoicesResponse,
            key="invoices",
            fetcher=self.list_invoices,
            args={
                "organization_id": organization_id,
                "started_after": started_after,
                "started_before": started_before,
                "invoice_type": invoice_type,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def download_invoice(
        self,
        *,
        invoice_id: str,
        file_type: Optional[DownloadInvoiceRequestFileType] = None,
    ) -> ScwFile:
        """
        Download an invoice.
        Download a specific invoice, specified by its ID.
        :param invoice_id: Invoice ID.
        :param file_type: Wanted file type.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.download_invoice(
                invoice_id="example",
            )
        """

        param_invoice_id = validate_path_param("invoice_id", invoice_id)

        res = self._request(
            "GET",
            f"/billing/v2alpha1/invoices/{param_invoice_id}/download",
            params={
                "file_type": file_type,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())
