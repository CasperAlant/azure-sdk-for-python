# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .arm_base_model_py3 import ARMBaseModel


class Share(ARMBaseModel):
    """Represents a share on the  Data Box Edge/Gateway device.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The path ID that uniquely identifies the object.
    :vartype id: str
    :ivar name: The object name.
    :vartype name: str
    :ivar type: The hierarchical type of the object.
    :vartype type: str
    :param description: Description for the share.
    :type description: str
    :param share_status: Required. Current status of the share. Possible
     values include: 'Online', 'Offline'
    :type share_status: str or ~azure.mgmt.edgegateway.models.ShareStatus
    :param monitoring_status: Required. Current monitoring status of the
     share. Possible values include: 'Enabled', 'Disabled'
    :type monitoring_status: str or
     ~azure.mgmt.edgegateway.models.MonitoringStatus
    :param azure_container_info: Azure container mapping for the share.
    :type azure_container_info:
     ~azure.mgmt.edgegateway.models.AzureContainerInfo
    :param access_protocol: Required. Access protocol to be used by the share.
     Possible values include: 'SMB', 'NFS'
    :type access_protocol: str or
     ~azure.mgmt.edgegateway.models.ShareAccessProtocol
    :param user_access_rights: Mapping of users and corresponding access
     rights on the share (required for SMB protocol).
    :type user_access_rights:
     list[~azure.mgmt.edgegateway.models.UserAccessRight]
    :param client_access_rights: List of IP addresses and corresponding access
     rights on the share(required for NFS protocol).
    :type client_access_rights:
     list[~azure.mgmt.edgegateway.models.ClientAccessRight]
    :param refresh_details: Details of the refresh job on this share.
    :type refresh_details: ~azure.mgmt.edgegateway.models.RefreshDetails
    :ivar share_mappings: Share mount point to the role.
    :vartype share_mappings:
     list[~azure.mgmt.edgegateway.models.MountPointMap]
    :param data_policy: Data policy of the share. Possible values include:
     'Cloud', 'Local'
    :type data_policy: str or ~azure.mgmt.edgegateway.models.DataPolicy
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'share_status': {'required': True},
        'monitoring_status': {'required': True},
        'access_protocol': {'required': True},
        'share_mappings': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'share_status': {'key': 'properties.shareStatus', 'type': 'str'},
        'monitoring_status': {'key': 'properties.monitoringStatus', 'type': 'str'},
        'azure_container_info': {'key': 'properties.azureContainerInfo', 'type': 'AzureContainerInfo'},
        'access_protocol': {'key': 'properties.accessProtocol', 'type': 'str'},
        'user_access_rights': {'key': 'properties.userAccessRights', 'type': '[UserAccessRight]'},
        'client_access_rights': {'key': 'properties.clientAccessRights', 'type': '[ClientAccessRight]'},
        'refresh_details': {'key': 'properties.refreshDetails', 'type': 'RefreshDetails'},
        'share_mappings': {'key': 'properties.shareMappings', 'type': '[MountPointMap]'},
        'data_policy': {'key': 'properties.dataPolicy', 'type': 'str'},
    }

    def __init__(self, *, share_status, monitoring_status, access_protocol, description: str=None, azure_container_info=None, user_access_rights=None, client_access_rights=None, refresh_details=None, data_policy=None, **kwargs) -> None:
        super(Share, self).__init__(**kwargs)
        self.description = description
        self.share_status = share_status
        self.monitoring_status = monitoring_status
        self.azure_container_info = azure_container_info
        self.access_protocol = access_protocol
        self.user_access_rights = user_access_rights
        self.client_access_rights = client_access_rights
        self.refresh_details = refresh_details
        self.share_mappings = None
        self.data_policy = data_policy