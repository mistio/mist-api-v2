import connexion
import six
import requests

from mist.api import config

from mist_api_v2.models.get_datapoints_response import GetDatapointsResponse  # noqa: E501
from mist_api_v2 import util

from mist.api.monitoring.victoriametrics.helpers import calculate_time_args, parse_relative_time


def get_datapoints(query, tags=None, start=None, end=None, step=None, time=None):  # noqa: E501
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
    """from mist.api.methods import list_resources
    resources, _ = list_resources(auth_context, "machine")
    from mist.api.monitoring.methods import filter_resources_by_tags
    resources = filter_resources_by_tags(resources, tags)"""

    def calculate_time_args(start, stop, step):
        time_args = ""
        if start != None:
            time_args += f"&start={parse_relative_time(start)}"
        if stop != None:
            time_args += f"&end={parse_relative_time(stop)}"
        if step != None:
            time_args += f"&step={parse_relative_time(step)}"
        return time_args

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
    if datapoints.ok:
        meta = {
            'total_matching': 1,
            'total_returned': 1,
            'sort': '',
            'start': ''
        }
        return GetDatapointsResponse(data=datapoints.json(), meta=meta)
    error_response = datapoints.json()
    return error_response.get("error", ""), datapoints.status_code
