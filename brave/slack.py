from slack import WebClient
from slack.errors import SlackApiError


def notify_internal(api_key, channel, message):
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


def notify_user(api_key, username, message):
    # For testing...
    # notify_internal(api_key, '@bbondy', '[For %s] %s' % (username, message))
    notify_internal(api_key, '#release-boss-audit-log', '[For %s] %s' % (username, message))
    notify_internal(api_key, username, message)
