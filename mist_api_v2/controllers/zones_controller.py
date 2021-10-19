import connexion

from mist.api.helpers import delete_none
from mist.api.dns.models import Zone
from mist.api.tag.methods import resolve_id_and_set_tags

from mist_api_v2.models.create_zone_request import CreateZoneRequest  # noqa: E501
from mist_api_v2.models.get_zone_response import GetZoneResponse  # noqa: E501
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
    auth_context = connexion.context['token_info']['auth_context']
    params = delete_none(create_zone_request.to_dict())
    try:
        [cloud], total = list_resources(
            auth_context, 'cloud', search=params.pop('cloud'), limit=1)
    except ValueError:
        return 'Cloud does not exist', 404
    auth_context.check_perm("cloud", "read", cloud.id)
    auth_context.check_perm("cloud", "create_resources", cloud.id)
    tags, _ = auth_context.check_perm("zone", "add", None)
    params['domain'] = params.pop('name')
    new_zone = Zone.add(owner=cloud.owner, cloud=cloud, **params)
    new_zone.assign_to(auth_context.user)
    if tags:
        resolve_id_and_set_tags(auth_context.owner, 'zone', new_zone.id,
                                tags, cloud_id=cloud.id)
    return new_zone.as_dict()


def edit_zone(zone, name=None):  # noqa: E501
    """Edit zone

    Edit target zone # noqa: E501

    :param zone:
    :type zone: str
    :param name: New zone name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


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
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(
        auth_context, 'zone', search=zone, only=only, deref=deref)
    return GetZoneResponse(data=result['data'], meta=result['meta'])


def list_zones(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
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

    :rtype: ListZonesResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = list_resources(
        auth_context, 'zone', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref)
    return ListZonesResponse(data=result['data'], meta=result['meta'])
