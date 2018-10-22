# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.imovel import Imovel  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestImoveisController(BaseTestCase):
    """ImoveisController integration test stubs"""

    def test_imoveis_get(self):
        """Test case for imoveis_get

        Lista os Imóveis
        """
        response = self.client.open(
            '/api/v1.0/imoveis',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_imoveis_id_get(self):
        """Test case for imoveis_id_get

        Obtem os dados de um Imóvel
        """
        response = self.client.open(
            '/api/v1.0/imoveis/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_imoveis_post(self):
        """Test case for imoveis_post

        Registro de imóveis
        """
        body = Body()
        response = self.client.open(
            '/api/v1.0/imoveis',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_imoveis_put(self):
        """Test case for imoveis_put

        Atualiza os dados de um Imóvel
        """
        body = Imovel()
        response = self.client.open(
            '/api/v1.0/imoveis',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
