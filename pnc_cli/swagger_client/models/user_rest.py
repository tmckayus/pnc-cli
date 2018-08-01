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


class UserRest(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'username': 'str'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'username': 'username'
    }

    def __init__(self, id=None, email=None, first_name=None, last_name=None, username=None):
        """
        UserRest - a model defined in Swagger
        """

        self._id = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._username = None

        if id is not None:
          self.id = id
        if email is not None:
          self.email = email
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if username is not None:
          self.username = username

    @property
    def id(self):
        """
        Gets the id of this UserRest.

        :return: The id of this UserRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserRest.

        :param id: The id of this UserRest.
        :type: int
        """

        self._id = id

    @property
    def email(self):
        """
        Gets the email of this UserRest.

        :return: The email of this UserRest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserRest.

        :param email: The email of this UserRest.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this UserRest.

        :return: The first_name of this UserRest.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserRest.

        :param first_name: The first_name of this UserRest.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this UserRest.

        :return: The last_name of this UserRest.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserRest.

        :param last_name: The last_name of this UserRest.
        :type: str
        """

        self._last_name = last_name

    @property
    def username(self):
        """
        Gets the username of this UserRest.

        :return: The username of this UserRest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserRest.

        :param username: The username of this UserRest.
        :type: str
        """

        self._username = username

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
        if not isinstance(other, UserRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
