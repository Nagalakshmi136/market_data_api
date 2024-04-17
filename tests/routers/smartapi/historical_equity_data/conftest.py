# pylint: disable=line-too-long
import pytest


@pytest.fixture
def stock_symbol_io():
    """
    Provide list of inputs and respective outputs to check various possible cases.

    Return:
    -------
    `List[dict]`
          List of inputs and respective outputs
    """
    return [
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-10-11 09:15",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 200,
            # "symbol_token": "11536",
            # "symbol": "TCS-EQ",
        },
        {
            "input_stock_symbol": "SCT",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-10-11 09:15",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 404,
            "error": "Symbol SCT not found. Please provide a valid symbol. Refer to the NSE symbols list for valid symbols.",
        },
        {
            "input_stock_symbol": "infy",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-10-9 9:15",
            "input_to_date": "2023-10-9 10:5",
            "status_code": 200,
            # "symbol_token": "1594",
            # "symbol": "INFY-EQ",
        },
        {
            "input_stock_symbol": "",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-10-11 09:15",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 404,
            "error": "Symbol not found. Please provide a valid symbol. Refer to the NSE symbols list for valid symbols.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "",
            "input_from_date": "2023-10-11 09:15",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 404,
            "error": "Candlestick interval  not found. Please provide a valid interval.",
        },
        {
            "input_stock_symbol": "INFY",
            "input_interval": "TWO_MINUTE",
            "input_from_date": "2023-10-11 9:15",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 404,
            "error": "Candlestick interval TWO_MINUTE not found. Please provide a valid interval.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "3 minutes",
            "input_from_date": "2023-10-11 9:15",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 404,
            "error": "Candlestick interval 3 minutes not found. Please provide a valid interval.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "one minute",
            "input_from_date": "2023-10-5 14:0",
            "input_to_date": "2023-10-05 15:20",
            "status_code": 200,
            # "symbol_token": "11536",
            # "symbol": "TCS-EQ",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "three-minute",
            "input_from_date": "2023-oct-11 8:15",
            "input_to_date": "2023-10-11 9:40",
            "status_code": 200,
            # "symbol_token": "11536",
            # "symbol": "TCS-EQ",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 400,
            "error": "Given datetime format  is invalid. Please provide a valid datetime that should be in the form '%Y-%m-%d %H:%M'.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-10-11 9:15",
            "input_to_date": "2023-10-23 3-43",
            "status_code": 400,
            "error": "Given datetime format 2023-10-23 3-43 is invalid. Please provide a valid datetime that should be in the form '%Y-%m-%d %H:%M'.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "january",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 400,
            "error": "Given datetime format january is invalid. Please provide a valid datetime that should be in the form '%Y-%m-%d %H:%M'.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "20-3-2023 10:34",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 400,
            "error": "Given datetime format 20-3-2023 10:34 is invalid. Please provide a valid datetime that should be in the form '%Y-%m-%d %H:%M'.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-10-11 40:80",
            "input_to_date": "2023-10-11 15:29",
            "status_code": 400,
            "error": "Given datetime format 2023-10-11 40:80 is invalid. Please provide a valid datetime that should be in the form '%Y-%m-%d %H:%M'.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023/10/11 15:15",
            "input_to_date": "2023-10-11 16:29",
            "status_code": 200,
            # "symbol_token": "11536",
            # "symbol": "TCS-EQ",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-January-11 09:15",
            "input_to_date": "2023-jan-11 15:29",
            "status_code": 200,
            # "symbol_token": "11536",
            # "symbol": "TCS-EQ",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-10-14 9:20",
            "input_to_date": "2023-10-15 13:25",
            "status_code": 400,
            "error": "All days from 2023-10-14 to 2023-10-15 are market holidays.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2015-10-14 9:20",
            "input_to_date": "2015-10-15 13:25",
            "status_code": 404,
            "error": "Data for the provided dates is unavailable; please use a date range starting from the 2016-10-03 date onwards.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-10-11 16:00",
            "input_to_date": "2023-10-11 19:00",
            "status_code": 400,
            "error": "Attempted to access trading system outside of trading hours.",
        },
        {
            "input_stock_symbol": "TCS",
            "input_interval": "ONE_MINUTE",
            "input_from_date": "2023-10-11 10:34",
            "input_to_date": "2023-11-20 15:29",
            "status_code": 416,
            "error": "The specified date range from 2023-10-11 10:34 to 2023-11-20 15:29 is invalid. Please ensure that the end date is greater than or equal to start date and difference between them does not exceed 30 for given interval ONE_MINUTE.",
        },
    ]
