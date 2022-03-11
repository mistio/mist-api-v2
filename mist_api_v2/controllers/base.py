

def list_resources(auth_context, resource_type, cloud=None, tags='',
                   search='', only='', sort='', start=0, limit=100,
                   deref='auto', at=None):
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
        start=start, at=at
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
                 sort='', deref='auto', at=None):
    """
        Get a single resource of any type and prepare the HTTP response
    """
    result = list_resources(auth_context, resource_type, cloud=cloud,
                            search=search, only=only, sort=sort, limit=1,
                            deref=deref, at=at)

    if result['data']:
        result['data'] = result['data'][0]
    else:
        result['data'] = {}

    return result
