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


class IdRev(object):
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
        'rev': 'int'
    }

    attribute_map = {
        'id': 'id',
        'rev': 'rev'
    }

    def __init__(self, id=None, rev=None):
        """
        IdRev - a model defined in Swagger
        """

        self._id = None
        self._rev = None

        if id is not None:
          self.id = id
        if rev is not None:
          self.rev = rev

    @property
    def id(self):
        """
        Gets the id of this IdRev.

        :return: The id of this IdRev.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IdRev.

        :param id: The id of this IdRev.
        :type: int
        """

        self._id = id

    @property
    def rev(self):
        """
        Gets the rev of this IdRev.

        :return: The rev of this IdRev.
        :rtype: int
        """
        return self._rev

    @rev.setter
    def rev(self, rev):
        """
        Sets the rev of this IdRev.

        :param rev: The rev of this IdRev.
        :type: int
        """

        self._rev = rev

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
        if not isinstance(other, IdRev):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
