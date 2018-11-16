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


class BuildConfigSetRecordRest(object):
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
        'build_configuration_set_id': 'int',
        'build_configuration_set_name': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'status': 'str',
        'user_id': 'int',
        'username': 'str',
        'product_version_id': 'int',
        'build_record_ids': 'list[int]',
        'temporary_build': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'build_configuration_set_id': 'buildConfigurationSetId',
        'build_configuration_set_name': 'buildConfigurationSetName',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'status': 'status',
        'user_id': 'userId',
        'username': 'username',
        'product_version_id': 'productVersionId',
        'build_record_ids': 'buildRecordIds',
        'temporary_build': 'temporaryBuild'
    }

    def __init__(self, id=None, build_configuration_set_id=None, build_configuration_set_name=None, start_time=None, end_time=None, status=None, user_id=None, username=None, product_version_id=None, build_record_ids=None, temporary_build=False):
        """
        BuildConfigSetRecordRest - a model defined in Swagger
        """

        self._id = None
        self._build_configuration_set_id = None
        self._build_configuration_set_name = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._user_id = None
        self._username = None
        self._product_version_id = None
        self._build_record_ids = None
        self._temporary_build = None

        if id is not None:
          self.id = id
        if build_configuration_set_id is not None:
          self.build_configuration_set_id = build_configuration_set_id
        if build_configuration_set_name is not None:
          self.build_configuration_set_name = build_configuration_set_name
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if status is not None:
          self.status = status
        if user_id is not None:
          self.user_id = user_id
        if username is not None:
          self.username = username
        if product_version_id is not None:
          self.product_version_id = product_version_id
        if build_record_ids is not None:
          self.build_record_ids = build_record_ids
        if temporary_build is not None:
          self.temporary_build = temporary_build

    @property
    def id(self):
        """
        Gets the id of this BuildConfigSetRecordRest.

        :return: The id of this BuildConfigSetRecordRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildConfigSetRecordRest.

        :param id: The id of this BuildConfigSetRecordRest.
        :type: int
        """

        self._id = id

    @property
    def build_configuration_set_id(self):
        """
        Gets the build_configuration_set_id of this BuildConfigSetRecordRest.

        :return: The build_configuration_set_id of this BuildConfigSetRecordRest.
        :rtype: int
        """
        return self._build_configuration_set_id

    @build_configuration_set_id.setter
    def build_configuration_set_id(self, build_configuration_set_id):
        """
        Sets the build_configuration_set_id of this BuildConfigSetRecordRest.

        :param build_configuration_set_id: The build_configuration_set_id of this BuildConfigSetRecordRest.
        :type: int
        """

        self._build_configuration_set_id = build_configuration_set_id

    @property
    def build_configuration_set_name(self):
        """
        Gets the build_configuration_set_name of this BuildConfigSetRecordRest.

        :return: The build_configuration_set_name of this BuildConfigSetRecordRest.
        :rtype: str
        """
        return self._build_configuration_set_name

    @build_configuration_set_name.setter
    def build_configuration_set_name(self, build_configuration_set_name):
        """
        Sets the build_configuration_set_name of this BuildConfigSetRecordRest.

        :param build_configuration_set_name: The build_configuration_set_name of this BuildConfigSetRecordRest.
        :type: str
        """

        self._build_configuration_set_name = build_configuration_set_name

    @property
    def start_time(self):
        """
        Gets the start_time of this BuildConfigSetRecordRest.

        :return: The start_time of this BuildConfigSetRecordRest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this BuildConfigSetRecordRest.

        :param start_time: The start_time of this BuildConfigSetRecordRest.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this BuildConfigSetRecordRest.

        :return: The end_time of this BuildConfigSetRecordRest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this BuildConfigSetRecordRest.

        :param end_time: The end_time of this BuildConfigSetRecordRest.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def status(self):
        """
        Gets the status of this BuildConfigSetRecordRest.

        :return: The status of this BuildConfigSetRecordRest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BuildConfigSetRecordRest.

        :param status: The status of this BuildConfigSetRecordRest.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED", "NO_REBUILD_REQUIRED", "UNSTABLE", "BUILDING", "REJECTED", "CANCELLED", "SYSTEM_ERROR", "UNKNOWN", "NONE"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def user_id(self):
        """
        Gets the user_id of this BuildConfigSetRecordRest.

        :return: The user_id of this BuildConfigSetRecordRest.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this BuildConfigSetRecordRest.

        :param user_id: The user_id of this BuildConfigSetRecordRest.
        :type: int
        """

        self._user_id = user_id

    @property
    def username(self):
        """
        Gets the username of this BuildConfigSetRecordRest.

        :return: The username of this BuildConfigSetRecordRest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this BuildConfigSetRecordRest.

        :param username: The username of this BuildConfigSetRecordRest.
        :type: str
        """

        self._username = username

    @property
    def product_version_id(self):
        """
        Gets the product_version_id of this BuildConfigSetRecordRest.

        :return: The product_version_id of this BuildConfigSetRecordRest.
        :rtype: int
        """
        return self._product_version_id

    @product_version_id.setter
    def product_version_id(self, product_version_id):
        """
        Sets the product_version_id of this BuildConfigSetRecordRest.

        :param product_version_id: The product_version_id of this BuildConfigSetRecordRest.
        :type: int
        """

        self._product_version_id = product_version_id

    @property
    def build_record_ids(self):
        """
        Gets the build_record_ids of this BuildConfigSetRecordRest.

        :return: The build_record_ids of this BuildConfigSetRecordRest.
        :rtype: list[int]
        """
        return self._build_record_ids

    @build_record_ids.setter
    def build_record_ids(self, build_record_ids):
        """
        Sets the build_record_ids of this BuildConfigSetRecordRest.

        :param build_record_ids: The build_record_ids of this BuildConfigSetRecordRest.
        :type: list[int]
        """

        self._build_record_ids = build_record_ids

    @property
    def temporary_build(self):
        """
        Gets the temporary_build of this BuildConfigSetRecordRest.

        :return: The temporary_build of this BuildConfigSetRecordRest.
        :rtype: bool
        """
        return self._temporary_build

    @temporary_build.setter
    def temporary_build(self, temporary_build):
        """
        Sets the temporary_build of this BuildConfigSetRecordRest.

        :param temporary_build: The temporary_build of this BuildConfigSetRecordRest.
        :type: bool
        """

        self._temporary_build = temporary_build

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
        if not isinstance(other, BuildConfigSetRecordRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
