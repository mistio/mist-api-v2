

def list_resources(auth_context, resource_type, cloud=None, tags='',
                   search='', only='', sort='', start=0, limit=100,
                   deref='auto'):
    """
        List resources of any type and prepare the HTTP response
    """
    from mist.api.methods import list_resources
    if not limit:
        limit = 100
    try:
        start = int(start)
    except (ValueError, TypeError):
        start = 0
    items, total = list_resources(
        auth_context, resource_type, cloud=cloud, tags=tags,
        search=search, only=only, sort=sort, limit=limit,
        start=start
    )
    meta = {
        'total': total,
        'returned': len(items),
        'sort': sort,
        'start': start
    }
    return {
        'data': [i.as_dict_v2(deref or '', only or '') for i in items],
        'meta': meta
    }


def get_resource(auth_context, resource_type, cloud=None, search='', only='',
                 sort='', deref='auto'):
    """
        Get a single resource of any type and prepare the HTTP response
    """
    result = list_resources(auth_context, resource_type, cloud=cloud,
                            search=search, only=only, sort=sort, limit=1,
                            deref=deref)

    if result['data']:
        result['data'] = result['data'][0]
    else:
        result['data'] = {}

    return result

def get_org_resources_count(auth_context, org_id):
    from mist.api.users.models import Organization
    org = Organization.objects.get(id=org_id)
    # list_resources looks for resources in the auth_context.org org
    # so here we set it to the org the api call is meant for
    auth_context.org = org
    limit = 1
    start = 0
    resources_count = {}
    resource_types = {'cloud', 'cluster', 'machine', 'volume', 'bucket',
                      'network', 'zone', 'key', 'image', 'schedule'}
    from mist.api.methods import list_resources
    for resource_type in resource_types:
        _, total = list_resources(
            auth_context, resource_type, limit=limit, start=start
        )
        resources_count[f'{resource_type}s'] = total
    return resources_count
