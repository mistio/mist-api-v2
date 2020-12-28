import connexion
import six

from mist_api_v2.models.get_image_response import GetImageResponse  # noqa: E501
from mist_api_v2.models.list_images_response import ListImagesResponse  # noqa: E501
from mist_api_v2 import util


def get_image(image):  # noqa: E501
    """Get image

    Get details about target image # noqa: E501

    :param image: 
    :type image: str

    :rtype: GetImageResponse
    """
    return 'do some magic!'


def list_images(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List images

    List images owned by the active org. READ permission required on image &amp; cloud. # noqa: E501

    :param cloud: 
    :type cloud: str
    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str
    :param start: Start results from index or id
    :type start: str
    :param limit: Limit number of results, 1000 max
    :type limit: int
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: ListImagesResponse
    """
    return 'do some magic!'
