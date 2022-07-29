import connexion

from mist_api_v2.models.get_job_response import GetJobResponse  # noqa: E501
from mist_api_v2.models.response_metadata import ResponseMetadata  # noqa: E501
from mist_api_v2.models.job import Job  # noqa: F401
from mist_api_v2 import util  # noqa: F401
from mist.api.logs.methods import get_stream_uri


def get_job(job_id):  # noqa: E501
    """Get job

    null # noqa: E501

    :param job_id:
    :type job_id: str

    :rtype: GetJobResponse
    """
    from mist.api.logs.methods import get_story
    from mist.api.exceptions import NotFoundError
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        story = get_story(auth_context.owner.id, job_id)
    except NotFoundError:
        return 'Job not found', 404
    for key in ("type", "story_id", "key_id"):
        story.pop(key, None)
    if story.get("owner_id"):
        story["org"] = story.pop("owner_id", None)
    if story.get("job"):
        story["action"] = story.pop("job", None)
    for log in story.get("logs"):
        if log.get("owner_id"):
            log["org"] = log.pop("owner_id", None)
    if not story.get('finished_at'):
        script_actions = [log['action'] for log in story['logs']
                          if log['action'].startswith('run_script')]
        if len(script_actions):
            stream_uri = get_stream_uri(job_id)
            story["stream_uri"] = stream_uri
    return GetJobResponse(
        data=story, meta=ResponseMetadata(total=1, returned=1))
