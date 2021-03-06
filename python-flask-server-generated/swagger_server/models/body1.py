# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, nome: str=None, endereo: str=None):  # noqa: E501
        """Body1 - a model defined in Swagger

        :param nome: The nome of this Body1.  # noqa: E501
        :type nome: str
        :param endereo: The endereo of this Body1.  # noqa: E501
        :type endereo: str
        """
        self.swagger_types = {
            'nome': str,
            'endereo': str
        }

        self.attribute_map = {
            'nome': 'nome',
            'endereo': 'endereço'
        }

        self._nome = nome
        self._endereo = endereo

    @classmethod
    def from_dict(cls, dikt) -> 'Body1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_1 of this Body1.  # noqa: E501
        :rtype: Body1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nome(self) -> str:
        """Gets the nome of this Body1.


        :return: The nome of this Body1.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        """Sets the nome of this Body1.


        :param nome: The nome of this Body1.
        :type nome: str
        """
        if nome is None:
            raise ValueError("Invalid value for `nome`, must not be `None`")  # noqa: E501
        if nome is not None and len(nome) > 100:
            raise ValueError("Invalid value for `nome`, length must be less than or equal to `100`")  # noqa: E501

        self._nome = nome

    @property
    def endereo(self) -> str:
        """Gets the endereo of this Body1.


        :return: The endereo of this Body1.
        :rtype: str
        """
        return self._endereo

    @endereo.setter
    def endereo(self, endereo: str):
        """Sets the endereo of this Body1.


        :param endereo: The endereo of this Body1.
        :type endereo: str
        """
        if endereo is not None and len(endereo) > 250:
            raise ValueError("Invalid value for `endereo`, length must be less than or equal to `250`")  # noqa: E501

        self._endereo = endereo
