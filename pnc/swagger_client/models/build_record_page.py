# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class BuildRecordPage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildRecordPage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'list[BuildRecord]',
            'page_index': 'int',
            'page_size': 'int',
            'total_pages': 'int'
        }

        self.attribute_map = {
            'content': 'content',
            'page_index': 'pageIndex',
            'page_size': 'pageSize',
            'total_pages': 'totalPages'
        }

        self._content = None
        self._page_index = None
        self._page_size = None
        self._total_pages = None

    @property
    def content(self):
        """
        Gets the content of this BuildRecordPage.


        :return: The content of this BuildRecordPage.
        :rtype: list[BuildRecord]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this BuildRecordPage.


        :param content: The content of this BuildRecordPage.
        :type: list[BuildRecord]
        """
        self._content = content

    @property
    def page_index(self):
        """
        Gets the page_index of this BuildRecordPage.
        Page index

        :return: The page_index of this BuildRecordPage.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this BuildRecordPage.
        Page index

        :param page_index: The page_index of this BuildRecordPage.
        :type: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        """
        Gets the page_size of this BuildRecordPage.
        Number of records per page

        :return: The page_size of this BuildRecordPage.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this BuildRecordPage.
        Number of records per page

        :param page_size: The page_size of this BuildRecordPage.
        :type: int
        """
        self._page_size = page_size

    @property
    def total_pages(self):
        """
        Gets the total_pages of this BuildRecordPage.
        Total pages provided by this query or -1 if unknown

        :return: The total_pages of this BuildRecordPage.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """
        Sets the total_pages of this BuildRecordPage.
        Total pages provided by this query or -1 if unknown

        :param total_pages: The total_pages of this BuildRecordPage.
        :type: int
        """
        self._total_pages = total_pages

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
