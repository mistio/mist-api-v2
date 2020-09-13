import connexion
import six

from mist_api_v2.models.add_cloud_request import AddCloudRequest  # noqa: E501
from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_clouds_response import ListCloudsResponse  # noqa: E501
from mist_api_v2 import util


def add_cloud(add_cloud_request=None):  # noqa: E501
    """Add cloud

    Adds a new cloud and returns the cloud&#39;s id. ADD permission required on cloud. # noqa: E501

    :param add_cloud_request: 
    :type add_cloud_request: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        add_cloud_request = AddCloudRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_cloud(cloud):  # noqa: E501
    """Delete cloud

    Delete target cloud # noqa: E501

    :param cloud: 
    :type cloud: str

    :rtype: None
    """
    return 'do some magic!'


def get_cloud(cloud):  # noqa: E501
    """Get cloud

    Get details about target cloud # noqa: E501

    :param cloud: 
    :type cloud: str

    :rtype: None
    """
    return 'do some magic!'


def list_clouds(filter=None, sort=None):  # noqa: E501
    """List clouds

    List clouds owned by the active org. READ permission required on cloud. # noqa: E501

    :param filter: Only return results matching filter
    :type filter: str
    :param sort: Order results by
    :type sort: str

    :rtype: ListCloudsResponse
    """
    return 'do some magic!'
