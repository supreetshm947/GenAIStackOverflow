"""Generated client library for batch version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.batch.v1alpha import batch_v1alpha_messages as messages


class BatchV1alpha(base_api.BaseApiClient):
  """Generated client library for service batch version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://batch.googleapis.com/'
  MTLS_BASE_URL = 'https://batch.mtls.googleapis.com/'

  _PACKAGE = 'batch'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'BatchV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new batch handle."""
    url = url or self.BASE_URL
    super(BatchV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_jobs_taskGroups_tasks = self.ProjectsLocationsJobsTaskGroupsTasksService(self)
    self.projects_locations_jobs_taskGroups = self.ProjectsLocationsJobsTaskGroupsService(self)
    self.projects_locations_jobs = self.ProjectsLocationsJobsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_resourceAllowances = self.ProjectsLocationsResourceAllowancesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsJobsTaskGroupsTasksService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs_taskGroups_tasks resource."""

    _NAME = 'projects_locations_jobs_taskGroups_tasks'

    def __init__(self, client):
      super(BatchV1alpha.ProjectsLocationsJobsTaskGroupsTasksService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Return a single Task.

      Args:
        request: (BatchProjectsLocationsJobsTaskGroupsTasksGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}/taskGroups/{taskGroupsId}/tasks/{tasksId}',
        http_method='GET',
        method_id='batch.projects.locations.jobs.taskGroups.tasks.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='BatchProjectsLocationsJobsTaskGroupsTasksGetRequest',
        response_type_name='Task',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List Tasks associated with a job.

      Args:
        request: (BatchProjectsLocationsJobsTaskGroupsTasksListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTasksResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}/taskGroups/{taskGroupsId}/tasks',
        http_method='GET',
        method_id='batch.projects.locations.jobs.taskGroups.tasks.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/tasks',
        request_field='',
        request_type_name='BatchProjectsLocationsJobsTaskGroupsTasksListRequest',
        response_type_name='ListTasksResponse',
        supports_download=False,
    )

  class ProjectsLocationsJobsTaskGroupsService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs_taskGroups resource."""

    _NAME = 'projects_locations_jobs_taskGroups'

    def __init__(self, client):
      super(BatchV1alpha.ProjectsLocationsJobsTaskGroupsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsJobsService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs resource."""

    _NAME = 'projects_locations_jobs'

    def __init__(self, client):
      super(BatchV1alpha.ProjectsLocationsJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Cancel a Job.

      Args:
        request: (BatchProjectsLocationsJobsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}:cancel',
        http_method='POST',
        method_id='batch.projects.locations.jobs.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:cancel',
        request_field='cancelJobRequest',
        request_type_name='BatchProjectsLocationsJobsCancelRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Create a Job.

      Args:
        request: (BatchProjectsLocationsJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/jobs',
        http_method='POST',
        method_id='batch.projects.locations.jobs.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['jobId', 'requestId'],
        relative_path='v1alpha/{+parent}/jobs',
        request_field='job',
        request_type_name='BatchProjectsLocationsJobsCreateRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a Job.

      Args:
        request: (BatchProjectsLocationsJobsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method='DELETE',
        method_id='batch.projects.locations.jobs.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['reason', 'requestId'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='BatchProjectsLocationsJobsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get a Job specified by its resource name.

      Args:
        request: (BatchProjectsLocationsJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method='GET',
        method_id='batch.projects.locations.jobs.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='BatchProjectsLocationsJobsGetRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List all Jobs for a project within a region.

      Args:
        request: (BatchProjectsLocationsJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/jobs',
        http_method='GET',
        method_id='batch.projects.locations.jobs.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/jobs',
        request_field='',
        request_type_name='BatchProjectsLocationsJobsListRequest',
        response_type_name='ListJobsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update a Job.

      Args:
        request: (BatchProjectsLocationsJobsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method='PATCH',
        method_id='batch.projects.locations.jobs.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='job',
        request_type_name='BatchProjectsLocationsJobsPatchRequest',
        response_type_name='Job',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(BatchV1alpha.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (BatchProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='batch.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='BatchProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (BatchProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='batch.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='BatchProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (BatchProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='batch.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='BatchProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (BatchProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='batch.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/operations',
        request_field='',
        request_type_name='BatchProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsResourceAllowancesService(base_api.BaseApiService):
    """Service class for the projects_locations_resourceAllowances resource."""

    _NAME = 'projects_locations_resourceAllowances'

    def __init__(self, client):
      super(BatchV1alpha.ProjectsLocationsResourceAllowancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a Resource Allowance.

      Args:
        request: (BatchProjectsLocationsResourceAllowancesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourceAllowance) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/resourceAllowances',
        http_method='POST',
        method_id='batch.projects.locations.resourceAllowances.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['requestId', 'resourceAllowanceId'],
        relative_path='v1alpha/{+parent}/resourceAllowances',
        request_field='resourceAllowance',
        request_type_name='BatchProjectsLocationsResourceAllowancesCreateRequest',
        response_type_name='ResourceAllowance',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a ResourceAllowance.

      Args:
        request: (BatchProjectsLocationsResourceAllowancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/resourceAllowances/{resourceAllowancesId}',
        http_method='DELETE',
        method_id='batch.projects.locations.resourceAllowances.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['reason', 'requestId'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='BatchProjectsLocationsResourceAllowancesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get a ResourceAllowance specified by its resource name.

      Args:
        request: (BatchProjectsLocationsResourceAllowancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourceAllowance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/resourceAllowances/{resourceAllowancesId}',
        http_method='GET',
        method_id='batch.projects.locations.resourceAllowances.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='BatchProjectsLocationsResourceAllowancesGetRequest',
        response_type_name='ResourceAllowance',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List all ResourceAllowances for a project within a region.

      Args:
        request: (BatchProjectsLocationsResourceAllowancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListResourceAllowancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/resourceAllowances',
        http_method='GET',
        method_id='batch.projects.locations.resourceAllowances.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/resourceAllowances',
        request_field='',
        request_type_name='BatchProjectsLocationsResourceAllowancesListRequest',
        response_type_name='ListResourceAllowancesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update a Resource Allowance.

      Args:
        request: (BatchProjectsLocationsResourceAllowancesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourceAllowance) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/resourceAllowances/{resourceAllowancesId}',
        http_method='PATCH',
        method_id='batch.projects.locations.resourceAllowances.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='resourceAllowance',
        request_type_name='BatchProjectsLocationsResourceAllowancesPatchRequest',
        response_type_name='ResourceAllowance',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(BatchV1alpha.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (BatchProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='batch.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='BatchProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (BatchProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations',
        http_method='GET',
        method_id='batch.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/locations',
        request_field='',
        request_type_name='BatchProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(BatchV1alpha.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
