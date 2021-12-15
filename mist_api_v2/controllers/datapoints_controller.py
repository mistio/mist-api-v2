import connexion
import requests

from mist_api_v2.models.get_datapoints_response import GetDatapointsResponse  # noqa: E501

from mist.api.monitoring.victoriametrics.helpers import parse_relative_time

from mist.api.helpers import apply_promql_query_rbac, get_victoriametrics_uri


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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401

    def dictify_time_args(start, stop, step):
        time_args = {}
        if start is not None:
            time_args["start"] = parse_relative_time(start)
        if stop is not None:
            time_args["end"] = parse_relative_time(stop)
        if step is not None:
            time_args["step"] = parse_relative_time(step)
        return time_args

    try:
        query = apply_promql_query_rbac(auth_context, tags, search, query)
    except RuntimeError as exc:
        return str(exc), 400

    uri = get_victoriametrics_uri(auth_context.org)
    datapoints = None
    if time:
        datapoints = requests.post(
            f"{uri}/api/v1/query",
            data={"query": query, "time": parse_relative_time(time)},
            timeout=20)
    else:
        time_args = dictify_time_args(start, end, step)
        req = {"query": query}
        req.update(time_args)
        datapoints = requests.post(
            f"{uri}/api/v1/query_range", data=req, timeout=20)
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
