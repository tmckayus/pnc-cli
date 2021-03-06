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


class RepositoryConfigurationRest(object):
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
        'internal_url': 'str',
        'external_url': 'str',
        'pre_build_sync_enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'internal_url': 'internalUrl',
        'external_url': 'externalUrl',
        'pre_build_sync_enabled': 'preBuildSyncEnabled'
    }

    def __init__(self, id=None, internal_url=None, external_url=None, pre_build_sync_enabled=False):
        """
        RepositoryConfigurationRest - a model defined in Swagger
        """

        self._id = None
        self._internal_url = None
        self._external_url = None
        self._pre_build_sync_enabled = None

        if id is not None:
          self.id = id
        if internal_url is not None:
          self.internal_url = internal_url
        if external_url is not None:
          self.external_url = external_url
        if pre_build_sync_enabled is not None:
          self.pre_build_sync_enabled = pre_build_sync_enabled

    @property
    def id(self):
        """
        Gets the id of this RepositoryConfigurationRest.

        :return: The id of this RepositoryConfigurationRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RepositoryConfigurationRest.

        :param id: The id of this RepositoryConfigurationRest.
        :type: int
        """

        self._id = id

    @property
    def internal_url(self):
        """
        Gets the internal_url of this RepositoryConfigurationRest.

        :return: The internal_url of this RepositoryConfigurationRest.
        :rtype: str
        """
        return self._internal_url

    @internal_url.setter
    def internal_url(self, internal_url):
        """
        Sets the internal_url of this RepositoryConfigurationRest.

        :param internal_url: The internal_url of this RepositoryConfigurationRest.
        :type: str
        """

        self._internal_url = internal_url

    @property
    def external_url(self):
        """
        Gets the external_url of this RepositoryConfigurationRest.

        :return: The external_url of this RepositoryConfigurationRest.
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """
        Sets the external_url of this RepositoryConfigurationRest.

        :param external_url: The external_url of this RepositoryConfigurationRest.
        :type: str
        """

        self._external_url = external_url

    @property
    def pre_build_sync_enabled(self):
        """
        Gets the pre_build_sync_enabled of this RepositoryConfigurationRest.

        :return: The pre_build_sync_enabled of this RepositoryConfigurationRest.
        :rtype: bool
        """
        return self._pre_build_sync_enabled

    @pre_build_sync_enabled.setter
    def pre_build_sync_enabled(self, pre_build_sync_enabled):
        """
        Sets the pre_build_sync_enabled of this RepositoryConfigurationRest.

        :param pre_build_sync_enabled: The pre_build_sync_enabled of this RepositoryConfigurationRest.
        :type: bool
        """

        self._pre_build_sync_enabled = pre_build_sync_enabled

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
        if not isinstance(other, RepositoryConfigurationRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
