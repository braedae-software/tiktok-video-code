from bs4 import BeautifulSoup  # To parse the weather site for info
from twilio.rest import Client  # To send out SMS
import requests  # Request weather site


def create_twilio_client(account_sid: str, auth_token: str) -> Client:
    """
    Creates and returns Twilio client used for SMS.

    Params:
        account_sid: unique id of Twilio account used for SMS
        auth_token: Twilio given token to validate app to Twilio for SMS

    Returns:
        Twilio client for accessing Twilio API
    """
    return Client(account_sid, auth_token)


def send_message(mes: str, twilio_num: str, to_num: str, client: Client):
    """
    Sends SMS to given number.

    Params:
        mes: message for body of SMS
        twilio_num: Twilio given phone number to send SMS from
        to_num: phone number to receive SMS
        client: Twilio client to access API to send SMS
    """
    client.messages.create(from_=twilio_num, to=to_num, body=mes)


def get_api_url(lat: float, lon: float) -> str:
    """
    Creates weather.gov url based on given lat/lon.

    Params:
        lat: latitude of location to get weather for
        lon: longitude of location to get weather for

    Returns:
        URL for weather.gov of given location
    """
    return f"https://forecast.weather.gov/MapClick.php?lat={lat}&lon={lon}"


def request_weather(lat: float, lon: float) -> str:
    """
    Scrapes weather information from weather.gov and formats to be
    SMS friendly.

    Params:
        lat: latitude of location to get weather for
        lon: longitude of location to get weather for
    Returns:
        Single day weather forecast formatted for SMS purposes.
    """
    # Get weather.gov html and parse
    url: str = get_api_url(lat, lon)
    response: requests.Response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Grab only information for today and format
    text_body: str = ""
    i: int = 0
    for f in soup.select("li.forecast-tombstone"):
        if i < 2:
            text_body += f.select_one(".period-name").get_text(
                strip=True, separator=" "
            )
            text_body += "\n"

            text_body += f.select_one(".short-desc").get_text(strip=True, separator=" ")
            text_body += "\n"

            text_body += f.select_one(".temp").text
            if i == 0:
                text_body += "\n\n\n"
            i += 1
        else:
            break
    return text_body


if __name__ == "__main__":
    # Location to get weather for
    lat: float = 0.0  # YOUR LATITUDE HERE
    lon: float = 0.0  # YOUR LONGITUDE HERE

    # Twilio information for SMS
    twilio_num: str = ""
    account_sid: str = ""
    auth_token: str = ""

    # Get number to send forecast to
    to_num: str = ""

    # Get the forecast for today and format for SMS
    weather_forecast: str = "Weather Forecast :) \n\n" + request_weather(
        lat=lat, lon=lon
    )

    # Create client object for sending SMS
    c: Client = create_twilio_client(account_sid=account_sid, auth_token=auth_token)

    # Send message
    send_message(mes=weather_forecast, twilio_num=twilio_num, to_num=to_num, client=c)
