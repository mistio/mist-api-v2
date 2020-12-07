def list_resources(auth_context, resource_type, cloud=None, search='', only='',
        sort='', start=0, limit=100, deref='auto'):
    """
        List resources of any type and prepare the HTTP response
    """
    from mist.api.methods import list_resources
    items, total = list_resources(
        auth_context, resource_type, cloud=cloud, search=search, only=only,
        sort=sort, limit=limit
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
