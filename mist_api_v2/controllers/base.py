def list_resources(auth_context, resource_type, cloud=None, search='', only='',
                   sort='', start=0, limit=100, deref='auto', all_orgs=False):
    """
        List resources of any type and prepare the HTTP response
    """
    from mist.api.methods import list_resources
    if not limit:
        limit = 100
    items, total = list_resources(
        auth_context, resource_type, cloud=cloud, search=search, only=only,
        sort=sort, limit=limit, all_orgs=all_orgs
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
