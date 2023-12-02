# coding: utf-8

"""
    mailsac API Specification

    ## About the API  The Mailsac API allows for interacting with Mailsac services, including checking email, email validations, setting up forwarding addresses, receiving web socket email messages, and sending outbound mail.  [**Get a free API key**](https://mailsac.com/api-keys)  Test the Mailsac API online:  * [**Swagger UI Explorer** &rarr;](https://mailsac.com/docs/swagger)  **Base API Endpoint**:  * `https://mailsac.com/api/` * _All API documentation is relative to this endpoint._  **OpenAPI Spec**:  * [Download JSON](https://mailsac.com/openapi.json) * [Download YAML](https://mailsac.com/openapi.yml)   ### Support and Resources  * [npm Node.js and Browser library - @mailsac/api](https://www.npmjs.com/package/@mailsac/api) * [Full Documentation and Guides](https://docs.mailsac.com) * [Community Support and Discussion Forums](https://forum.mailsac.com/forums/) * [Web socket example in Node.js - ruffrey](https://github.com/ruffrey/mailsac-node-websocket-example)  Paid Email Support, Pre-Sales    > support@team.mailsac.com  [Terms of Service](https://docs.mailsac.com/en/latest/about/terms_of_service.html)  [Privacy Policy](https://docs.mailsac.com/en/latest/about/privacy_policy.html)   # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2009(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'EmailString',
        'n': 'int'
    }

    attribute_map = {
        'id': '_id',
        'n': 'n'
    }

    def __init__(self, id=None, n=None):  # noqa: E501
        """InlineResponse2009 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._n = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if n is not None:
            self.n = n

    @property
    def id(self):
        """Gets the id of this InlineResponse2009.  # noqa: E501


        :return: The id of this InlineResponse2009.  # noqa: E501
        :rtype: EmailString
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2009.


        :param id: The id of this InlineResponse2009.  # noqa: E501
        :type: EmailString
        """

        self._id = id

    @property
    def n(self):
        """Gets the n of this InlineResponse2009.  # noqa: E501

        count of messages  # noqa: E501

        :return: The n of this InlineResponse2009.  # noqa: E501
        :rtype: int
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this InlineResponse2009.

        count of messages  # noqa: E501

        :param n: The n of this InlineResponse2009.  # noqa: E501
        :type: int
        """

        self._n = n

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
            else:
                result[attr] = value
        if issubclass(InlineResponse2009, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2009):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
