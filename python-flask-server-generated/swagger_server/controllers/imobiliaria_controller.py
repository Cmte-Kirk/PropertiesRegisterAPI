import connexion
import six

from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.imobiliaria import Imobiliaria  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util


def imobiliaria_get():  # noqa: E501
    """Lista as Imabiliárias

    Listagem de Imabiliárias # noqa: E501


    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def imobiliaria_id_get(id):  # noqa: E501
    """Obtem os dados de uma Imabiliária

    Dados da Imabiliária # noqa: E501

    :param id: 
    :type id: int

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def imobiliaria_post(body):  # noqa: E501
    """Registro de Imabiliárias

    Inclui uma nova Imabiliária # noqa: E501

    :param body: Dados do imóvel
    :type body: dict | bytes

    :rtype: Imobiliaria
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def imobiliaria_put(body):  # noqa: E501
    """Atualiza os dados de uma Imabiliária

    Atualização de dados de Imabiliária # noqa: E501

    :param body: Dados do imóvel
    :type body: dict | bytes

    :rtype: Imobiliaria
    """
    if connexion.request.is_json:
        body = Imobiliaria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
