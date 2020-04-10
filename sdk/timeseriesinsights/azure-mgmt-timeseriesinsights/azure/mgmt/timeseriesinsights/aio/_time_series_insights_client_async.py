# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import TimeSeriesInsightsClientConfiguration
from .operations_async import Operations
from .operations_async import EnvironmentsOperations
from .operations_async import EventSourcesOperations
from .operations_async import ReferenceDataSetsOperations
from .operations_async import AccessPoliciesOperations
from .. import models


class TimeSeriesInsightsClient(object):
    """Time Series Insights client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.timeseriesinsights.aio.operations_async.Operations
    :ivar environments: EnvironmentsOperations operations
    :vartype environments: azure.mgmt.timeseriesinsights.aio.operations_async.EnvironmentsOperations
    :ivar event_sources: EventSourcesOperations operations
    :vartype event_sources: azure.mgmt.timeseriesinsights.aio.operations_async.EventSourcesOperations
    :ivar reference_data_sets: ReferenceDataSetsOperations operations
    :vartype reference_data_sets: azure.mgmt.timeseriesinsights.aio.operations_async.ReferenceDataSetsOperations
    :ivar access_policies: AccessPoliciesOperations operations
    :vartype access_policies: azure.mgmt.timeseriesinsights.aio.operations_async.AccessPoliciesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = TimeSeriesInsightsClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environments = EnvironmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.event_sources = EventSourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.reference_data_sets = ReferenceDataSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_policies = AccessPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "TimeSeriesInsightsClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)