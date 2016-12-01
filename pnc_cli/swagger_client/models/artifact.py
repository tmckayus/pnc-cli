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

from datetime import datetime
from pprint import pformat
from six import iteritems


class Artifact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Artifact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'identifier': 'str',
            'md5': 'str',
            'sha1': 'str',
            'sha256': 'str',
            'size': 'int',
            'artifact_quality': 'str',
            'repo_type': 'str',
            'filename': 'str',
            'deploy_path': 'str',
            'build_records': 'list[BuildRecord]',
            'dependant_build_records': 'list[BuildRecord]',
            'origin_url': 'str',
            'import_date': 'datetime',
            'distributed_in_product_milestones': 'list[ProductMilestone]',
            'field_handler': 'FieldHandler',
            'built': 'bool',
            'imported': 'bool',
            'trusted': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'identifier': 'identifier',
            'md5': 'md5',
            'sha1': 'sha1',
            'sha256': 'sha256',
            'size': 'size',
            'artifact_quality': 'artifactQuality',
            'repo_type': 'repoType',
            'filename': 'filename',
            'deploy_path': 'deployPath',
            'build_records': 'buildRecords',
            'dependant_build_records': 'dependantBuildRecords',
            'origin_url': 'originUrl',
            'import_date': 'importDate',
            'distributed_in_product_milestones': 'distributedInProductMilestones',
            'field_handler': 'fieldHandler',
            'built': 'built',
            'imported': 'imported',
            'trusted': 'trusted'
        }

        self._id = None
        self._identifier = None
        self._md5 = None
        self._sha1 = None
        self._sha256 = None
        self._size = None
        self._artifact_quality = None
        self._repo_type = None
        self._filename = None
        self._deploy_path = None
        self._build_records = None
        self._dependant_build_records = None
        self._origin_url = None
        self._import_date = None
        self._distributed_in_product_milestones = None
        self._field_handler = None
        self._built = None
        self._imported = None
        self._trusted = None

    @property
    def id(self):
        """
        Gets the id of this Artifact.


        :return: The id of this Artifact.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Artifact.


        :param id: The id of this Artifact.
        :type: int
        """
        self._id = id

    @property
    def identifier(self):
        """
        Gets the identifier of this Artifact.


        :return: The identifier of this Artifact.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Artifact.


        :param identifier: The identifier of this Artifact.
        :type: str
        """
        self._identifier = identifier

    @property
    def md5(self):
        """
        Gets the md5 of this Artifact.


        :return: The md5 of this Artifact.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this Artifact.


        :param md5: The md5 of this Artifact.
        :type: str
        """
        self._md5 = md5

    @property
    def sha1(self):
        """
        Gets the sha1 of this Artifact.


        :return: The sha1 of this Artifact.
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """
        Sets the sha1 of this Artifact.


        :param sha1: The sha1 of this Artifact.
        :type: str
        """
        self._sha1 = sha1

    @property
    def sha256(self):
        """
        Gets the sha256 of this Artifact.


        :return: The sha256 of this Artifact.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """
        Sets the sha256 of this Artifact.


        :param sha256: The sha256 of this Artifact.
        :type: str
        """
        self._sha256 = sha256

    @property
    def size(self):
        """
        Gets the size of this Artifact.


        :return: The size of this Artifact.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Artifact.


        :param size: The size of this Artifact.
        :type: int
        """
        self._size = size

    @property
    def artifact_quality(self):
        """
        Gets the artifact_quality of this Artifact.


        :return: The artifact_quality of this Artifact.
        :rtype: str
        """
        return self._artifact_quality

    @artifact_quality.setter
    def artifact_quality(self, artifact_quality):
        """
        Sets the artifact_quality of this Artifact.


        :param artifact_quality: The artifact_quality of this Artifact.
        :type: str
        """
        allowed_values = ["NEW", "VERIFIED", "TESTED", "DEPRECATED", "BLACKLISTED"]
        if artifact_quality not in allowed_values:
            raise ValueError(
                "Invalid value for `artifact_quality`, must be one of {0}"
                .format(allowed_values)
            )
        self._artifact_quality = artifact_quality

    @property
    def repo_type(self):
        """
        Gets the repo_type of this Artifact.


        :return: The repo_type of this Artifact.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """
        Sets the repo_type of this Artifact.


        :param repo_type: The repo_type of this Artifact.
        :type: str
        """
        allowed_values = ["MAVEN", "NPM", "COCOA_POD", "GENERIC_PROXY"]
        if repo_type not in allowed_values:
            raise ValueError(
                "Invalid value for `repo_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._repo_type = repo_type

    @property
    def filename(self):
        """
        Gets the filename of this Artifact.


        :return: The filename of this Artifact.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this Artifact.


        :param filename: The filename of this Artifact.
        :type: str
        """
        self._filename = filename

    @property
    def deploy_path(self):
        """
        Gets the deploy_path of this Artifact.


        :return: The deploy_path of this Artifact.
        :rtype: str
        """
        return self._deploy_path

    @deploy_path.setter
    def deploy_path(self, deploy_path):
        """
        Sets the deploy_path of this Artifact.


        :param deploy_path: The deploy_path of this Artifact.
        :type: str
        """
        self._deploy_path = deploy_path

    @property
    def build_records(self):
        """
        Gets the build_records of this Artifact.


        :return: The build_records of this Artifact.
        :rtype: list[BuildRecord]
        """
        return self._build_records

    @build_records.setter
    def build_records(self, build_records):
        """
        Sets the build_records of this Artifact.


        :param build_records: The build_records of this Artifact.
        :type: list[BuildRecord]
        """
        self._build_records = build_records

    @property
    def dependant_build_records(self):
        """
        Gets the dependant_build_records of this Artifact.


        :return: The dependant_build_records of this Artifact.
        :rtype: list[BuildRecord]
        """
        return self._dependant_build_records

    @dependant_build_records.setter
    def dependant_build_records(self, dependant_build_records):
        """
        Sets the dependant_build_records of this Artifact.


        :param dependant_build_records: The dependant_build_records of this Artifact.
        :type: list[BuildRecord]
        """
        self._dependant_build_records = dependant_build_records

    @property
    def origin_url(self):
        """
        Gets the origin_url of this Artifact.


        :return: The origin_url of this Artifact.
        :rtype: str
        """
        return self._origin_url

    @origin_url.setter
    def origin_url(self, origin_url):
        """
        Sets the origin_url of this Artifact.


        :param origin_url: The origin_url of this Artifact.
        :type: str
        """
        self._origin_url = origin_url

    @property
    def import_date(self):
        """
        Gets the import_date of this Artifact.


        :return: The import_date of this Artifact.
        :rtype: datetime
        """
        return self._import_date

    @import_date.setter
    def import_date(self, import_date):
        """
        Sets the import_date of this Artifact.


        :param import_date: The import_date of this Artifact.
        :type: datetime
        """
        self._import_date = import_date

    @property
    def distributed_in_product_milestones(self):
        """
        Gets the distributed_in_product_milestones of this Artifact.


        :return: The distributed_in_product_milestones of this Artifact.
        :rtype: list[ProductMilestone]
        """
        return self._distributed_in_product_milestones

    @distributed_in_product_milestones.setter
    def distributed_in_product_milestones(self, distributed_in_product_milestones):
        """
        Sets the distributed_in_product_milestones of this Artifact.


        :param distributed_in_product_milestones: The distributed_in_product_milestones of this Artifact.
        :type: list[ProductMilestone]
        """
        self._distributed_in_product_milestones = distributed_in_product_milestones

    @property
    def field_handler(self):
        """
        Gets the field_handler of this Artifact.


        :return: The field_handler of this Artifact.
        :rtype: FieldHandler
        """
        return self._field_handler

    @field_handler.setter
    def field_handler(self, field_handler):
        """
        Sets the field_handler of this Artifact.


        :param field_handler: The field_handler of this Artifact.
        :type: FieldHandler
        """
        self._field_handler = field_handler

    @property
    def built(self):
        """
        Gets the built of this Artifact.


        :return: The built of this Artifact.
        :rtype: bool
        """
        return self._built

    @built.setter
    def built(self, built):
        """
        Sets the built of this Artifact.


        :param built: The built of this Artifact.
        :type: bool
        """
        self._built = built

    @property
    def imported(self):
        """
        Gets the imported of this Artifact.


        :return: The imported of this Artifact.
        :rtype: bool
        """
        return self._imported

    @imported.setter
    def imported(self, imported):
        """
        Sets the imported of this Artifact.


        :param imported: The imported of this Artifact.
        :type: bool
        """
        self._imported = imported

    @property
    def trusted(self):
        """
        Gets the trusted of this Artifact.


        :return: The trusted of this Artifact.
        :rtype: bool
        """
        return self._trusted

    @trusted.setter
    def trusted(self, trusted):
        """
        Sets the trusted of this Artifact.


        :param trusted: The trusted of this Artifact.
        :type: bool
        """
        self._trusted = trusted

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
