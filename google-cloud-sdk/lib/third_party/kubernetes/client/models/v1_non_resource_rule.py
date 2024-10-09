# coding: utf-8
"""
    Kubernetes

    No description provided (generated by Swagger Codegen
    https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.4

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class V1NonResourceRule(object):
  """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
  """
    Attributes:
      swagger_types (dict): The key is attribute name and the value is attribute
        type.
      attribute_map (dict): The key is attribute name and the value is json key
        in definition.
  """
  swagger_types = {'non_resource_ur_ls': 'list[str]', 'verbs': 'list[str]'}

  attribute_map = {'non_resource_ur_ls': 'nonResourceURLs', 'verbs': 'verbs'}

  def __init__(self, non_resource_ur_ls=None, verbs=None):
    """
        V1NonResourceRule - a model defined in Swagger
        """

    self._non_resource_ur_ls = None
    self._verbs = None
    self.discriminator = None

    if non_resource_ur_ls is not None:
      self.non_resource_ur_ls = non_resource_ur_ls
    self.verbs = verbs

  @property
  def non_resource_ur_ls(self):
    """
        Gets the non_resource_ur_ls of this V1NonResourceRule.
        NonResourceURLs is a set of partial urls that a user should have access
        to.  *s are allowed, but only as the full, final step in the path.
        \"*\" means all.

        :return: The non_resource_ur_ls of this V1NonResourceRule.
        :rtype: list[str]
        """
    return self._non_resource_ur_ls

  @non_resource_ur_ls.setter
  def non_resource_ur_ls(self, non_resource_ur_ls):
    """
        Sets the non_resource_ur_ls of this V1NonResourceRule.
        NonResourceURLs is a set of partial urls that a user should have access
        to.  *s are allowed, but only as the full, final step in the path.
        \"*\" means all.

        :param non_resource_ur_ls: The non_resource_ur_ls of this
        V1NonResourceRule.
        :type: list[str]
        """

    self._non_resource_ur_ls = non_resource_ur_ls

  @property
  def verbs(self):
    """
        Gets the verbs of this V1NonResourceRule.
        Verb is a list of kubernetes non-resource API verbs, like: get, post,
        put, delete, patch, head, options.  \"*\" means all.

        :return: The verbs of this V1NonResourceRule.
        :rtype: list[str]
        """
    return self._verbs

  @verbs.setter
  def verbs(self, verbs):
    """
        Sets the verbs of this V1NonResourceRule.
        Verb is a list of kubernetes non-resource API verbs, like: get, post,
        put, delete, patch, head, options.  \"*\" means all.

        :param verbs: The verbs of this V1NonResourceRule.
        :type: list[str]
        """
    if verbs is None:
      raise ValueError('Invalid value for `verbs`, must not be `None`')

    self._verbs = verbs

  def to_dict(self):
    """
        Returns the model properties as a dict
        """
    result = {}

    for attr, _ in iteritems(self.swagger_types):
      value = getattr(self, attr)
      if isinstance(value, list):
        result[attr] = list(
            map(lambda x: x.to_dict() if hasattr(x, 'to_dict') else x, value))
      elif hasattr(value, 'to_dict'):
        result[attr] = value.to_dict()
      elif isinstance(value, dict):
        result[attr] = dict(
            map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], 'to_dict') else item, value.items()))
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
    if not isinstance(other, V1NonResourceRule):
      return False

    return self.__dict__ == other.__dict__

  def __ne__(self, other):
    """
        Returns true if both objects are not equal
        """
    return not self == other
