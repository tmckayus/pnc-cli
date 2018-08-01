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


class ProductVersionRefRest(object):
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
        'version': 'str',
        'product_name': 'str',
        'product_id': 'int',
        'current_milestone_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'product_name': 'productName',
        'product_id': 'productId',
        'current_milestone_id': 'currentMilestoneId'
    }

    def __init__(self, id=None, version=None, product_name=None, product_id=None, current_milestone_id=None):
        """
        ProductVersionRefRest - a model defined in Swagger
        """

        self._id = None
        self._version = None
        self._product_name = None
        self._product_id = None
        self._current_milestone_id = None

        if id is not None:
          self.id = id
        if version is not None:
          self.version = version
        if product_name is not None:
          self.product_name = product_name
        if product_id is not None:
          self.product_id = product_id
        if current_milestone_id is not None:
          self.current_milestone_id = current_milestone_id

    @property
    def id(self):
        """
        Gets the id of this ProductVersionRefRest.

        :return: The id of this ProductVersionRefRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductVersionRefRest.

        :param id: The id of this ProductVersionRefRest.
        :type: int
        """

        self._id = id

    @property
    def version(self):
        """
        Gets the version of this ProductVersionRefRest.

        :return: The version of this ProductVersionRefRest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ProductVersionRefRest.

        :param version: The version of this ProductVersionRefRest.
        :type: str
        """

        self._version = version

    @property
    def product_name(self):
        """
        Gets the product_name of this ProductVersionRefRest.

        :return: The product_name of this ProductVersionRefRest.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this ProductVersionRefRest.

        :param product_name: The product_name of this ProductVersionRefRest.
        :type: str
        """

        self._product_name = product_name

    @property
    def product_id(self):
        """
        Gets the product_id of this ProductVersionRefRest.

        :return: The product_id of this ProductVersionRefRest.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this ProductVersionRefRest.

        :param product_id: The product_id of this ProductVersionRefRest.
        :type: int
        """

        self._product_id = product_id

    @property
    def current_milestone_id(self):
        """
        Gets the current_milestone_id of this ProductVersionRefRest.

        :return: The current_milestone_id of this ProductVersionRefRest.
        :rtype: int
        """
        return self._current_milestone_id

    @current_milestone_id.setter
    def current_milestone_id(self, current_milestone_id):
        """
        Sets the current_milestone_id of this ProductVersionRefRest.

        :param current_milestone_id: The current_milestone_id of this ProductVersionRefRest.
        :type: int
        """

        self._current_milestone_id = current_milestone_id

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
        if not isinstance(other, ProductVersionRefRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
