from mist.api.exceptions import NotFoundError


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
    if not resource_type.endswith('s'):
        resource_type += 's'
    meta = {
        'kind': resource_type,
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
        result['meta']['kind'] = result['meta']['kind'][:-1]
    else:
        raise NotFoundError(f'Resource {search} not found')

    return result


def get_org_resources_summary(auth_context, org_id):
    from mist.api.users.models import Organization
    org = Organization.objects.get(id=org_id)
    resources_count = {}
    # get count for org resources
    org_r_types = {'key', 'script', 'template', 'tunnel', 'schedule', 'rule',
                   'team', 'secret', 'stack'}
    from mist.api.helpers import get_resource_model
    for resource_type in org_r_types:
        try:
            resource_model = get_resource_model(resource_type)
        except KeyError:
            # if tunnels are not present
            continue
        except Exception as exc:
            raise
        total_resources = 0
        if resource_type == 'schedule':
            # Schedules need to filter reminder types which is a reference
            schedules = resource_model.objects(owner=org, deleted=None)
            total_resources = len(schedules)
            # remove reminders
            for schedule in schedules:
                if schedule.schedule_type.type == 'reminder':
                    total_resources -= 1
        elif resource_type == 'team':
            total_resources = len(org.teams)
        elif resource_type == 'rule':
            total_resources = resource_model.objects(owner_id=org.id).count()
        elif resource_type == 'secret':
            total_resources = resource_model.objects(owner=org).count()
        else:
            total_resources = resource_model.objects(
                owner=org, deleted=None).count()
        resources_count[f'{resource_type}s'] = {'total': total_resources}

    # get count for cloud resources
    limit = 1
    start = 0
    cloud_r_types = {'cloud', 'cluster', 'machine', 'image', 'volume',
                     'bucket', 'network', 'zone'}
    from mist.api.methods import list_resources
    for resource_type in cloud_r_types:
        _, total = list_resources(
            auth_context, resource_type, limit=limit, start=start
        )
        resources_count[f'{resource_type}s'] = {'total': total}

    return resources_count
