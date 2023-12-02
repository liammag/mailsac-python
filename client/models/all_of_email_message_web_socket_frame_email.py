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
from client.models.email_message_body_props import EmailMessageBodyProps  # noqa: F401,E501

class AllOfEmailMessageWebSocketFrameEmail(EmailMessageBodyProps):
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
        'id': 'MessageId',
        '_from': 'list[EmailRecipient]',
        'to': 'list[EmailRecipient]',
        'cc': 'list[EmailRecipient]',
        'bcc': 'list[EmailRecipient]',
        'subject': 'EmailSubject',
        'saved_by': 'str',
        'original_inbox': 'str',
        'inbox': 'str',
        'domain': 'str',
        'received': 'ModelDate',
        'size': 'float',
        'attachments': 'list[Md5sum]',
        'ip': 'str',
        'via': 'str',
        'folder': 'str',
        'labels': 'list[str]',
        'read': 'bool',
        'rtls': 'bool',
        'links': 'list[str]',
        'spam': 'float'
    }
    if hasattr(EmailMessageBodyProps, "swagger_types"):
        swagger_types.update(EmailMessageBodyProps.swagger_types)

    attribute_map = {
        'id': '_id',
        '_from': 'from',
        'to': 'to',
        'cc': 'cc',
        'bcc': 'bcc',
        'subject': 'subject',
        'saved_by': 'savedBy',
        'original_inbox': 'originalInbox',
        'inbox': 'inbox',
        'domain': 'domain',
        'received': 'received',
        'size': 'size',
        'attachments': 'attachments',
        'ip': 'ip',
        'via': 'via',
        'folder': 'folder',
        'labels': 'labels',
        'read': 'read',
        'rtls': 'rtls',
        'links': 'links',
        'spam': 'spam'
    }
    if hasattr(EmailMessageBodyProps, "attribute_map"):
        attribute_map.update(EmailMessageBodyProps.attribute_map)

    def __init__(self, id=None, _from=None, to=None, cc=None, bcc=None, subject=None, saved_by=None, original_inbox=None, inbox=None, domain=None, received=None, size=None, attachments=None, ip=None, via=None, folder='inbox', labels=None, read=None, rtls=None, links=None, spam=None, *args, **kwargs):  # noqa: E501
        """AllOfEmailMessageWebSocketFrameEmail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self.__from = None
        self._to = None
        self._cc = None
        self._bcc = None
        self._subject = None
        self._saved_by = None
        self._original_inbox = None
        self._inbox = None
        self._domain = None
        self._received = None
        self._size = None
        self._attachments = None
        self._ip = None
        self._via = None
        self._folder = None
        self._labels = None
        self._read = None
        self._rtls = None
        self._links = None
        self._spam = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if cc is not None:
            self.cc = cc
        if bcc is not None:
            self.bcc = bcc
        if subject is not None:
            self.subject = subject
        if saved_by is not None:
            self.saved_by = saved_by
        if original_inbox is not None:
            self.original_inbox = original_inbox
        if inbox is not None:
            self.inbox = inbox
        if domain is not None:
            self.domain = domain
        if received is not None:
            self.received = received
        if size is not None:
            self.size = size
        if attachments is not None:
            self.attachments = attachments
        if ip is not None:
            self.ip = ip
        if via is not None:
            self.via = via
        if folder is not None:
            self.folder = folder
        if labels is not None:
            self.labels = labels
        if read is not None:
            self.read = read
        if rtls is not None:
            self.rtls = rtls
        if links is not None:
            self.links = links
        if spam is not None:
            self.spam = spam
        EmailMessageBodyProps.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501


        :return: The id of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: MessageId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllOfEmailMessageWebSocketFrameEmail.


        :param id: The id of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: MessageId
        """

        self._id = id

    @property
    def _from(self):
        """Gets the _from of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        The FROM sender, this will always have 1 item in the array unless the email was malformed.  # noqa: E501

        :return: The _from of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: list[EmailRecipient]
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this AllOfEmailMessageWebSocketFrameEmail.

        The FROM sender, this will always have 1 item in the array unless the email was malformed.  # noqa: E501

        :param _from: The _from of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: list[EmailRecipient]
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        The RCPT-TO recipients of the email.  # noqa: E501

        :return: The to of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: list[EmailRecipient]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this AllOfEmailMessageWebSocketFrameEmail.

        The RCPT-TO recipients of the email.  # noqa: E501

        :param to: The to of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: list[EmailRecipient]
        """

        self._to = to

    @property
    def cc(self):
        """Gets the cc of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        CarbonCopy recipients of the email.  # noqa: E501

        :return: The cc of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: list[EmailRecipient]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this AllOfEmailMessageWebSocketFrameEmail.

        CarbonCopy recipients of the email.  # noqa: E501

        :param cc: The cc of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: list[EmailRecipient]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        BlindCarbonCopy recipients of the email.  # noqa: E501

        :return: The bcc of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: list[EmailRecipient]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this AllOfEmailMessageWebSocketFrameEmail.

        BlindCarbonCopy recipients of the email.  # noqa: E501

        :param bcc: The bcc of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: list[EmailRecipient]
        """

        self._bcc = bcc

    @property
    def subject(self):
        """Gets the subject of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501


        :return: The subject of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: EmailSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this AllOfEmailMessageWebSocketFrameEmail.


        :param subject: The subject of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: EmailSubject
        """

        self._subject = subject

    @property
    def saved_by(self):
        """Gets the saved_by of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        Indicates a starred message by your account Account._id. Otherwise `null`.  # noqa: E501

        :return: The saved_by of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: str
        """
        return self._saved_by

    @saved_by.setter
    def saved_by(self, saved_by):
        """Sets the saved_by of this AllOfEmailMessageWebSocketFrameEmail.

        Indicates a starred message by your account Account._id. Otherwise `null`.  # noqa: E501

        :param saved_by: The saved_by of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: str
        """

        self._saved_by = saved_by

    @property
    def original_inbox(self):
        """Gets the original_inbox of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        Same as inbox unless sent to the encryptedInbox, in which case it would be the encryptedInbox.  # noqa: E501

        :return: The original_inbox of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: str
        """
        return self._original_inbox

    @original_inbox.setter
    def original_inbox(self, original_inbox):
        """Sets the original_inbox of this AllOfEmailMessageWebSocketFrameEmail.

        Same as inbox unless sent to the encryptedInbox, in which case it would be the encryptedInbox.  # noqa: E501

        :param original_inbox: The original_inbox of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: str
        """

        self._original_inbox = original_inbox

    @property
    def inbox(self):
        """Gets the inbox of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        Email address to which this message belongs.  # noqa: E501

        :return: The inbox of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: str
        """
        return self._inbox

    @inbox.setter
    def inbox(self, inbox):
        """Sets the inbox of this AllOfEmailMessageWebSocketFrameEmail.

        Email address to which this message belongs.  # noqa: E501

        :param inbox: The inbox of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: str
        """

        self._inbox = inbox

    @property
    def domain(self):
        """Gets the domain of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        hostname domain for the inbox  # noqa: E501

        :return: The domain of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AllOfEmailMessageWebSocketFrameEmail.

        hostname domain for the inbox  # noqa: E501

        :param domain: The domain of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def received(self):
        """Gets the received of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501


        :return: The received of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: ModelDate
        """
        return self._received

    @received.setter
    def received(self, received):
        """Sets the received of this AllOfEmailMessageWebSocketFrameEmail.


        :param received: The received of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: ModelDate
        """

        self._received = received

    @property
    def size(self):
        """Gets the size of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        Content length in bytes of the original raw email message  # noqa: E501

        :return: The size of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this AllOfEmailMessageWebSocketFrameEmail.

        Content length in bytes of the original raw email message  # noqa: E501

        :param size: The size of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def attachments(self):
        """Gets the attachments of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        `null` or array of MD5 hashes of attachments. Use the Attachments API to get metadata and download attachments.  # noqa: E501

        :return: The attachments of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: list[Md5sum]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this AllOfEmailMessageWebSocketFrameEmail.

        `null` or array of MD5 hashes of attachments. Use the Attachments API to get metadata and download attachments.  # noqa: E501

        :param attachments: The attachments of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: list[Md5sum]
        """

        self._attachments = attachments

    @property
    def ip(self):
        """Gets the ip of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        The remote SMTP server that send the mail to the server at `via`  # noqa: E501

        :return: The ip of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this AllOfEmailMessageWebSocketFrameEmail.

        The remote SMTP server that send the mail to the server at `via`  # noqa: E501

        :param ip: The ip of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def via(self):
        """Gets the via of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        IP address of SMTP server that received the message from `ip`  # noqa: E501

        :return: The via of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: str
        """
        return self._via

    @via.setter
    def via(self, via):
        """Sets the via of this AllOfEmailMessageWebSocketFrameEmail.

        IP address of SMTP server that received the message from `ip`  # noqa: E501

        :param via: The via of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: str
        """

        self._via = via

    @property
    def folder(self):
        """Gets the folder of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        Inbox folder that this message has been put into  # noqa: E501

        :return: The folder of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this AllOfEmailMessageWebSocketFrameEmail.

        Inbox folder that this message has been put into  # noqa: E501

        :param folder: The folder of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: str
        """
        allowed_values = ["inbox", "all", "sent", "spam", "trash"]  # noqa: E501
        if folder not in allowed_values:
            raise ValueError(
                "Invalid value for `folder` ({0}), must be one of {1}"  # noqa: E501
                .format(folder, allowed_values)
            )

        self._folder = folder

    @property
    def labels(self):
        """Gets the labels of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        Custom inbox labels created by the end user  # noqa: E501

        :return: The labels of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AllOfEmailMessageWebSocketFrameEmail.

        Custom inbox labels created by the end user  # noqa: E501

        :param labels: The labels of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def read(self):
        """Gets the read of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        Read/uread status. true=read, false=unread. Only set from the Inbox UI app.  # noqa: E501

        :return: The read of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this AllOfEmailMessageWebSocketFrameEmail.

        Read/uread status. true=read, false=unread. Only set from the Inbox UI app.  # noqa: E501

        :param read: The read of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: bool
        """

        self._read = read

    @property
    def rtls(self):
        """Gets the rtls of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        When true, indicates the SMTP message was received over TLS (encrypted).  # noqa: E501

        :return: The rtls of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: bool
        """
        return self._rtls

    @rtls.setter
    def rtls(self, rtls):
        """Sets the rtls of this AllOfEmailMessageWebSocketFrameEmail.

        When true, indicates the SMTP message was received over TLS (encrypted).  # noqa: E501

        :param rtls: The rtls of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: bool
        """

        self._rtls = rtls

    @property
    def links(self):
        """Gets the links of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        List of any URLs that were found in the text and HTML body of the message.  # noqa: E501

        :return: The links of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AllOfEmailMessageWebSocketFrameEmail.

        List of any URLs that were found in the text and HTML body of the message.  # noqa: E501

        :param links: The links of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: list[str]
        """

        self._links = links

    @property
    def spam(self):
        """Gets the spam of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501

        Experimental - result of spam filter scan, between 0.0 and 1.0, where 1.0 indicates a high likelihood of being spam  # noqa: E501

        :return: The spam of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :rtype: float
        """
        return self._spam

    @spam.setter
    def spam(self, spam):
        """Sets the spam of this AllOfEmailMessageWebSocketFrameEmail.

        Experimental - result of spam filter scan, between 0.0 and 1.0, where 1.0 indicates a high likelihood of being spam  # noqa: E501

        :param spam: The spam of this AllOfEmailMessageWebSocketFrameEmail.  # noqa: E501
        :type: float
        """

        self._spam = spam

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
        if issubclass(AllOfEmailMessageWebSocketFrameEmail, dict):
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
        if not isinstance(other, AllOfEmailMessageWebSocketFrameEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other