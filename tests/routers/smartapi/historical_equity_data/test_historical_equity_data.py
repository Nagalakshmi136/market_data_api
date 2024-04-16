# pylint: disable=missing-function-docstring
from fastapi import HTTPException
from fastapi.testclient import TestClient
from icecream import ic
from app.routers.smartapi.historical_equity_data.historical_equity_data import router
from app.schemas.stock_model import HistoricalStockPriceInfo

client = TestClient(router)


def validate_exception(endpoint_url, expected_error):
    """
    Test function to validate exception.

    This function checks if the expected exception is valid or not
    for the request with given endpoint_url.

    Parameters:
    -----------
    endpoint_url: `str`
        URL to request data from historical_stock_data endpoint.
    expected_error: `dict[str, Any]`
        Expected exception for the request with given endpoint_url.
    """
    try:
        # Make a GET request to the endpoint URL
        client.get(endpoint_url)
    except HTTPException as http_exc:
        # Check if the status code of the exception matches the expected error status code
        assert http_exc.status_code == expected_error["status_code"]
        # Check if the detail message of the exception matches the expected error detail
        assert http_exc.detail == expected_error["error"]


def test_historical_stock_data(stock_symbol_io):
    """
    Test function to validate historical_stock_data endpoint.

    This function verifies the operational behaviour of the
    historical_stock_data endpoint across various input scenarios.

    Parameters:
    -----------
    stock_symbol_io: `list[dict[str, Any]]`
        List of inputs and respective outputs.
    """
    for stock_symbol_data in stock_symbol_io:
        endpoint_url = f"/smart-api/equity/history/{stock_symbol_data['input_stock_symbol']}?interval={stock_symbol_data['input_interval']}&start_date={stock_symbol_data['input_from_date']}&end_date={stock_symbol_data['input_to_date']}"

        if stock_symbol_data["status_code"] == 200:
            # Send a GET request to the endpoint URL
            response = client.get(endpoint_url)

            # Assert that the response status code matches the expected status code
            assert response.status_code == stock_symbol_data["status_code"]
            data = response.json()
            # Assert that the response contains JSON data
            assert response.json() is not None

            # Assert that the response is list of stock data
            assert isinstance(data, list)

            # Parse the response JSON into a HistoricalStockPriceInfo object
            smart_api_stock_price_info = HistoricalStockPriceInfo.parse_obj(data[0])

            # # Assert that the stock_price_info object is an instance of StockPriceInfo
            assert isinstance(smart_api_stock_price_info, HistoricalStockPriceInfo)

        else:
            validate_exception(endpoint_url, stock_symbol_data)
