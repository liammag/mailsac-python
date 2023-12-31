# coding: utf-8

"""
    mailsac API Specification

    ## About the API  The Mailsac API allows for interacting with Mailsac services, including checking email, email validations, setting up forwarding addresses, receiving web socket email messages, and sending outbound mail.  [**Get a free API key**](https://mailsac.com/api-keys)  Test the Mailsac API online:  * [**Swagger UI Explorer** &rarr;](https://mailsac.com/docs/swagger)  **Base API Endpoint**:  * `https://mailsac.com/api/` * _All API documentation is relative to this endpoint._  **OpenAPI Spec**:  * [Download JSON](https://mailsac.com/openapi.json) * [Download YAML](https://mailsac.com/openapi.yml)   ### Support and Resources  * [npm Node.js and Browser library - @mailsac/api](https://www.npmjs.com/package/@mailsac/api) * [Full Documentation and Guides](https://docs.mailsac.com) * [Community Support and Discussion Forums](https://forum.mailsac.com/forums/) * [Web socket example in Node.js - ruffrey](https://github.com/ruffrey/mailsac-node-websocket-example)  Paid Email Support, Pre-Sales    > support@team.mailsac.com  [Terms of Service](https://docs.mailsac.com/en/latest/about/terms_of_service.html)  [Privacy Policy](https://docs.mailsac.com/en/latest/about/privacy_policy.html)   # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import client
from client.api.domains_api import DomainsApi  # noqa: E501
from client.rest import ApiException


class TestDomainsApi(unittest.TestCase):
    """DomainsApi unit test stubs"""

    def setUp(self):
        self.api = DomainsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_domains(self):
        """Test case for list_domains

        List domains  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
