from datetime import date
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products() -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        products: list[dict[str, object]] = [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            },
        ]
        expected_result: list[str] = ["duck"]
        assert outdated_products(products) == expected_result


def test_no_outdated_products() -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 1)
        products: list[dict[str, object]] = [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
        ]
        expected_result: list[str] = []
        assert outdated_products(products) == expected_result


def test_all_outdated_products() -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 15)
        products: list[dict[str, object]] = [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            },
        ]
        expected_result: list[str] = ["salmon", "chicken", "duck"]
        assert outdated_products(products) == expected_result
