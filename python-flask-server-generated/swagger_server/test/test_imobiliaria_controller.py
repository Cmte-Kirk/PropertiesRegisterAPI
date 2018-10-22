# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.imobiliaria import Imobiliaria  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestImobiliariaController(BaseTestCase):
    """ImobiliariaController integration test stubs"""

    def test_imobiliaria_get(self):
        """Test case for imobiliaria_get

        Lista as Imabiliárias
        """
        response = self.client.open(
            '/api/v1.0/imobiliaria',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_imobiliaria_id_get(self):
        """Test case for imobiliaria_id_get

        Obtem os dados de uma Imabiliária
        """
        response = self.client.open(
            '/api/v1.0/imobiliaria/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_imobiliaria_post(self):
        """Test case for imobiliaria_post

        Registro de Imabiliárias
        """
        body = Body1()
        response = self.client.open(
            '/api/v1.0/imobiliaria',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_imobiliaria_put(self):
        """Test case for imobiliaria_put

        Atualiza os dados de uma Imabiliária
        """
        body = Imobiliaria()
        response = self.client.open(
            '/api/v1.0/imobiliaria',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
