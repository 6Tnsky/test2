import pytest
import requests
from unittest.mock import patch
from main import get_random_cat_image


def test_successful_request():
    """
    Проверяет успешный запрос к API и возврат корректного URL.
    """
    mock_response = [
        {"id": "abc123", "url": "https://cdn2.thecatapi.com/images/abc123.jpg"}
    ]

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_random_cat_image()
        assert result == "https://cdn2.thecatapi.com/images/abc123.jpg"


def test_unsuccessful_request():
    """
    Проверяет неуспешный запрос (например, статус код 404) и возврат None.
    """
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404

        result = get_random_cat_image()
        assert result is None


def test_request_exception():
    """
    Проверяет обработку исключений (например, проблемы с сетью) и возврат None.
    """
    with patch("requests.get", side_effect=requests.RequestException):
        result = get_random_cat_image()
        assert result is None