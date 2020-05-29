from slack import WebClient
from slack.errors import SlackApiError


def notify(api_key, channel, message):
    client = WebClient(token=api_key)
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message)
        return True
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(f"Got an error: {e.response['error']}")
        return e.response["ok"] is False
