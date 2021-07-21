import connexion
import requests

from mist.api import config

from mist_api_v2.models.get_datapoints_response import GetDatapointsResponse  # noqa: E501

from mist.api.monitoring.victoriametrics.helpers import parse_relative_time

from .base import list_resources, get_resource


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
    machine_name_map = {machine["id"]: machine["name"] for machine in machines.get("data", [])
                        if machine.get("id") and machine.get("name")}

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
    filtered_result = []
    if datapoints.get("data", {}).get("result", []):
        for item in datapoints["data"]["result"]:
            if isinstance(item, dict) and item.get("metric", {}).get("machine_id") and machine_name_map.get(item.get("metric", {})["machine_id"]):
                item["metric"].update(
                    {"name": machine_name_map[item["metric"]["machine_id"]]})
                filtered_result.append(item)
        datapoints["data"]["result"] = filtered_result

    meta = {
        'total_matching': 1,
        'total_returned': 1,
        'sort': '',
        'start': ''
    }
    return GetDatapointsResponse(data=datapoints, meta=meta)
