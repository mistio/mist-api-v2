import connexion
# import six

from mist.api.exceptions import PolicyUnauthorizedError

# from mist_api_v2.models.add_schedule_request import AddScheduleRequest  # noqa: E501
from mist_api_v2.models.edit_schedule_request import EditScheduleRequest  # noqa: E501
from mist_api_v2.models.get_schedule_response import GetScheduleResponse  # noqa: E501
# from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_schedules_response import ListSchedulesResponse  # noqa: E501
# from mist_api_v2 import util

from .base import list_resources, get_resource


def add_schedule(add_schedule_request=None):  # noqa: E501
    """Add schedule

    Add schedule to user schedules # noqa: E501

    :param add_schedule_request:
    :type add_schedule_request: dict | bytes

    :rtype: InlineResponse200
    """
    # if connexion.request.is_json:
    # add_schedule_request = AddScheduleRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_schedule(schedule):  # noqa: E501
    """Delete schedule

    Delete target schedule # noqa: E501

    :param schedule:
    :type schedule: str

    :rtype: None
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    result = get_resource(auth_context, 'schedule', search=schedule)
    result_data = result.get('data')
    if not result_data:
        return 'Schedule does not exist', 404
    from mist.api.schedules.models import Schedule
    schedule_id = result_data.get('id')
    try:
        auth_context.check_perm('schedule', 'remove', schedule_id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    schedule = Schedule.objects.get(owner=auth_context.owner, id=schedule_id,
                                    deleted=None)
    schedule.ctl.delete()
    return 'Deleted schedule `%s`' % schedule.name, 200


def edit_schedule(schedule, edit_schedule_request=None):  # noqa: E501
    """Edit schedule

    Edit target schedule # noqa: E501

    :param schedule:
    :type schedule: str
    :param edit_schedule_request:
    :type edit_schedule_request: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        edit_schedule_request = EditScheduleRequest.from_dict(connexion.request.get_json())  # noqa: E501
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [schedule], total = list_resources(auth_context, 'schedule',
                                           search=schedule, limit=1)
    except ValueError:
        return 'Script does not exist', 404
    try:
        auth_context.check_perm('schedule', 'edit', schedule.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    schedule.ctl.edit(edit_schedule_request.name,
                      edit_schedule_request.description)
    return 'Updated script `%s`' % schedule.name, 200


def get_schedule(schedule, only=None, deref=None):  # noqa: E501
    """Get schedule

    Get details about target schedule # noqa: E501

    :param schedule:
    :type schedule: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetScheduleResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    result = get_resource(auth_context, 'schedule',
                          search=schedule, only=only, deref=deref)
    return GetScheduleResponse(data=result['data'], meta=result['meta'])


def list_schedules(search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List schedules

    List schedules owned by the active org. READ permission required on schedules. # noqa: E501

    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str
    :param start: Start results from index or id
    :type start: str
    :param limit: Limit number of results, 1000 max
    :type limit: int
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: ListSchedulesResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    result = list_resources(auth_context, 'schedule', search=search,
                            only=only, sort=sort, limit=limit,
                            deref=deref)
    return ListSchedulesResponse(data=result['data'], meta=result['meta'])