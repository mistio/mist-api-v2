import connexion

from mist.api.helpers import delete_none
from mist.api.dns.models import Zone
from mist.api.tag.methods import add_tags_to_resource
from mist.api.exceptions import NotFoundError, PolicyUnauthorizedError

from mist.api.exceptions import BadRequestError
from mist.api.exceptions import CloudUnauthorizedError
from mist.api.exceptions import ZoneCreationError
from mist.api.exceptions import ZoneListingError
from mist.api.exceptions import CloudUnavailableError
from mist.api.exceptions import ZoneNotFoundError

from mist_api_v2 import util
from mist_api_v2.models.create_zone_request import CreateZoneRequest  # noqa: E501
from mist_api_v2.models.get_zone_response import GetZoneResponse  # noqa: E501
from mist_api_v2.models.get_record_response import GetRecordResponse  # noqa: E501
from mist_api_v2.models.list_records_response import ListRecordsResponse  # noqa: E501
from mist_api_v2.models.list_zones_response import ListZonesResponse  # noqa: E501

from .base import list_resources, get_resource


def create_zone(create_zone_request=None):  # noqa: E501
    """Create zone

    Creates one or more zones on the specified cloud. If async is true, a jobId will be returned. READ permission required on cloud. CREATE_RESOURCES permission required on cloud. CREATE permission required on zone. # noqa: E501

    :param create_zone_request:
    :type create_zone_request: dict | bytes

    :rtype: CreateZoneResponse
    """
    from mist.api.methods import list_resources
    if connexion.request.is_json:
        create_zone_request = CreateZoneRequest.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    params = delete_none(create_zone_request.to_dict())
    try:
        [cloud], total = list_resources(
            auth_context, 'cloud', search=params.pop('cloud'), limit=1)
    except ValueError:
        return 'Cloud does not exist', 404
    try:
        auth_context.check_perm("cloud", "read", cloud.id)
        auth_context.check_perm("cloud", "create_resources", cloud.id)
        tags, _ = auth_context.check_perm("zone", "add", None)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    params['domain'] = params.pop('name')
    try:
        new_zone = Zone.add(owner=cloud.owner, cloud=cloud, **params)
    except BadRequestError as e:
        return str(e), 400
    except CloudUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    except ZoneCreationError as e:
        return str(e), 503
    except ZoneListingError as e:
        return str(e), 503
    except CloudUnavailableError as e:
        return str(e), 503
    new_zone.assign_to(auth_context.user)
    if tags:
        add_tags_to_resource(auth_context.owner,
                             [{'resource_type': 'zone',
                               'resource_id': new_zone.id}],
                             tags)

    return new_zone.as_dict()


def delete_zone(zone):  # noqa: E501
    """Delete zone

    Delete target zone # noqa: E501

    :param zone:
    :type zone: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [zone], _ = list_resources(auth_context, 'zone',
                                   search=zone, limit=1)
    except ValueError:
        return 'Zone does not exist', 404
    try:
        # SEC
        auth_context.check_perm('cloud', 'read', zone.cloud.id)
        auth_context.check_perm('zone', 'read', zone.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        zone.ctl.delete_zone()
    except ZoneNotFoundError:
        return 'Zone not found', 404
    except CloudUnavailableError as e:
        return str(e), 503
    return 'Deleted zone `%s`' % zone.domain, 200


def edit_zone(zone):  # noqa: E501
    """Edit zone

    Edit target zone # noqa: E501

    :param zone:
    :type zone: str
    :param name: New zone name
    :type name: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [zone], total = list_resources(
            auth_context, 'zone', search=zone, limit=1)
    except ValueError:
        return 'Zone does not exist', 404
    try:
        auth_context.check_perm("zone", "edit", zone.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    return 'Zone successfully updated'


def get_zone(zone, only=None, deref=None):  # noqa: E501
    """Get zone

    Get details about target zone # noqa: E501

    :param zone:
    :type zone: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetZoneResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(
            auth_context, 'zone', search=zone, only=only, deref=deref)
    except NotFoundError:
        return 'Zone does not exist', 404
    return GetZoneResponse(data=result['data'], meta=result['meta'])


def list_zones(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None, at=None):  # noqa: E501
    """List zones

    List zones owned by the active org. READ permission required on zone &amp; cloud. # noqa: E501

    :param cloud:
    :type cloud: str
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
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListZonesResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    result = list_resources(
        auth_context, 'zone', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref, at=at)
    return ListZonesResponse(data=result['data'], meta=result['meta'])


def get_record(zone, record, cloud, only=None, deref=None):  # noqa: E501
    """Get record

    Get details about target record # noqa: E501

    :param zone:
    :type zone: str
    :param record:
    :type record: str
    :param cloud:
    :type cloud: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetRecordResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(
            auth_context, 'record', search=record, only=only, deref=deref)
    except NotFoundError:
        return 'Record does not exist', 404
    return GetRecordResponse(data=result['data'], meta=result['meta'])


def list_records(zone, cloud, only=None, deref=None):  # noqa: E501
    """List records

    Lists all DNS records for a particular zone. READ permission required on zone and record. # noqa: E501

    :param zone:
    :type zone: str
    :param cloud:
    :type cloud: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: ListRecordsResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    result = list_resources(
        auth_context, 'record', zone=zone, cloud=cloud,
        only=only, deref=deref)
    return ListRecordsResponse(data=result['data'], meta=result['meta'])
