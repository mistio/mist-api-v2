import connexion
import requests

from mist.api import config

from mist_api_v2.models.get_datapoints_response import GetDatapointsResponse  # noqa: E501

from mist.api.monitoring.victoriametrics.helpers import parse_relative_time, apply_rbac

from .base import list_resources


def get_datapoints(query, search=None, tags=None, start=None, end=None, step=None, time=None):  # noqa: E501
    """Get datapoints

    Get datapoints for a specific query # noqa: E501

    :param query:
    :type query: str
    :param tags:
    :type tags: str
    :param start:
    :type start: str
    :param end:
    :type end: str
    :param step:
    :type step: str
    :param time:
    :type time: str

    :rtype: GetDatapointsResponse
    """
    auth_context = connexion.context['token_info']['auth_context']

    def calculate_time_args(start, stop, step):
        time_args = ""
        if start is not None:
            time_args += f"&start={parse_relative_time(start)}"
        if stop is not None:
            time_args += f"&end={parse_relative_time(stop)}"
        if step is not None:
            time_args += f"&step={parse_relative_time(step)}"
        return time_args

    machines = list_resources(
        auth_context, 'machine', search=search
    )

    machine_ids = "|".join([machine["id"] for machine in machines.get(
        "data", []) if machine.get("id")])
    try:
        query = apply_rbac(query, machine_ids)
    except RuntimeError as exc:
        return str(exc), 400

    tenant = str(int(auth_context.org.id[:8], 16))
    uri = config.VICTORIAMETRICS_URI.replace("<org_id>", tenant)
    datapoints = None
    if time:
        print(time)
        datapoints = requests.get(
            f"{uri}/api/v1/query"
            f"?query={query}&time={parse_relative_time(time)}",
            timeout=20)
    else:
        time_args = calculate_time_args(start, end, step)
        datapoints = requests.get(
            f"{uri}/api/v1/query_range"
            f"?query={query}{time_args}", timeout=20)
    if not datapoints.ok:
        error_response = datapoints.json()
        return error_response.get("error", ""), datapoints.status_code

    datapoints = datapoints.json()

    meta = {
        'total_matching': 1,
        'total_returned': 1,
        'sort': '',
        'start': ''
    }
    return GetDatapointsResponse(data=datapoints, meta=meta)
