import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.imovel import Imovel  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def imoveis_get():  # noqa: E501
    """Lista os Imóveis

    Listagem de imóveis # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def imoveis_id_get(id):  # noqa: E501
    """Obtem os dados de um Imóvel

    Dados do Imóvel # noqa: E501

    :param id: 
    :type id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def imoveis_post(body):  # noqa: E501
    """Registro de imóveis

    Inclui um novo imóvel # noqa: E501

    :param body: Dados do imóvel
    :type body: dict | bytes

    :rtype: Imovel
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def imoveis_put(body):  # noqa: E501
    """Atualiza os dados de um Imóvel

    Atualização de dados de imóvel # noqa: E501

    :param body: Dados do imóvel
    :type body: dict | bytes

    :rtype: Imovel
    """
    if connexion.request.is_json:
        body = Imovel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
