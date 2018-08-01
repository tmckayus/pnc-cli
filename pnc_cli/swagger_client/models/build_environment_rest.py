# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from datetime import datetime
from pprint import pformat
from six import iteritems
import re


class BuildEnvironmentRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'system_image_repository_url': 'str',
        'system_image_id': 'str',
        'attributes': 'dict(str, str)',
        'system_image_type': 'str',
        'deprecated': 'bool',
        'image_repository_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'system_image_repository_url': 'systemImageRepositoryUrl',
        'system_image_id': 'systemImageId',
        'attributes': 'attributes',
        'system_image_type': 'systemImageType',
        'deprecated': 'deprecated',
        'image_repository_url': 'imageRepositoryUrl'
    }

    def __init__(self, id=None, name=None, description=None, system_image_repository_url=None, system_image_id=None, attributes=None, system_image_type=None, deprecated=False, image_repository_url=None):
        """
        BuildEnvironmentRest - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._system_image_repository_url = None
        self._system_image_id = None
        self._attributes = None
        self._system_image_type = None
        self._deprecated = None
        self._image_repository_url = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if system_image_repository_url is not None:
          self.system_image_repository_url = system_image_repository_url
        if system_image_id is not None:
          self.system_image_id = system_image_id
        if attributes is not None:
          self.attributes = attributes
        if system_image_type is not None:
          self.system_image_type = system_image_type
        if deprecated is not None:
          self.deprecated = deprecated
        if image_repository_url is not None:
          self.image_repository_url = image_repository_url

    @property
    def id(self):
        """
        Gets the id of this BuildEnvironmentRest.

        :return: The id of this BuildEnvironmentRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildEnvironmentRest.

        :param id: The id of this BuildEnvironmentRest.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BuildEnvironmentRest.

        :return: The name of this BuildEnvironmentRest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildEnvironmentRest.

        :param name: The name of this BuildEnvironmentRest.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this BuildEnvironmentRest.

        :return: The description of this BuildEnvironmentRest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BuildEnvironmentRest.

        :param description: The description of this BuildEnvironmentRest.
        :type: str
        """

        self._description = description

    @property
    def system_image_repository_url(self):
        """
        Gets the system_image_repository_url of this BuildEnvironmentRest.

        :return: The system_image_repository_url of this BuildEnvironmentRest.
        :rtype: str
        """
        return self._system_image_repository_url

    @system_image_repository_url.setter
    def system_image_repository_url(self, system_image_repository_url):
        """
        Sets the system_image_repository_url of this BuildEnvironmentRest.

        :param system_image_repository_url: The system_image_repository_url of this BuildEnvironmentRest.
        :type: str
        """

        self._system_image_repository_url = system_image_repository_url

    @property
    def system_image_id(self):
        """
        Gets the system_image_id of this BuildEnvironmentRest.

        :return: The system_image_id of this BuildEnvironmentRest.
        :rtype: str
        """
        return self._system_image_id

    @system_image_id.setter
    def system_image_id(self, system_image_id):
        """
        Sets the system_image_id of this BuildEnvironmentRest.

        :param system_image_id: The system_image_id of this BuildEnvironmentRest.
        :type: str
        """

        self._system_image_id = system_image_id

    @property
    def attributes(self):
        """
        Gets the attributes of this BuildEnvironmentRest.

        :return: The attributes of this BuildEnvironmentRest.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this BuildEnvironmentRest.

        :param attributes: The attributes of this BuildEnvironmentRest.
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def system_image_type(self):
        """
        Gets the system_image_type of this BuildEnvironmentRest.

        :return: The system_image_type of this BuildEnvironmentRest.
        :rtype: str
        """
        return self._system_image_type

    @system_image_type.setter
    def system_image_type(self, system_image_type):
        """
        Sets the system_image_type of this BuildEnvironmentRest.

        :param system_image_type: The system_image_type of this BuildEnvironmentRest.
        :type: str
        """
        allowed_values = ["DOCKER_IMAGE", "VIRTUAL_MACHINE_RAW", "VIRTUAL_MACHINE_QCOW2", "LOCAL_WORKSPACE"]
        if system_image_type not in allowed_values:
            raise ValueError(
                "Invalid value for `system_image_type` ({0}), must be one of {1}"
                .format(system_image_type, allowed_values)
            )

        self._system_image_type = system_image_type

    @property
    def deprecated(self):
        """
        Gets the deprecated of this BuildEnvironmentRest.

        :return: The deprecated of this BuildEnvironmentRest.
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """
        Sets the deprecated of this BuildEnvironmentRest.

        :param deprecated: The deprecated of this BuildEnvironmentRest.
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def image_repository_url(self):
        """
        Gets the image_repository_url of this BuildEnvironmentRest.

        :return: The image_repository_url of this BuildEnvironmentRest.
        :rtype: str
        """
        return self._image_repository_url

    @image_repository_url.setter
    def image_repository_url(self, image_repository_url):
        """
        Sets the image_repository_url of this BuildEnvironmentRest.

        :param image_repository_url: The image_repository_url of this BuildEnvironmentRest.
        :type: str
        """

        self._image_repository_url = image_repository_url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BuildEnvironmentRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
