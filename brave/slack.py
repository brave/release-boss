from slack import WebClient
from slack.errors import SlackApiError


def notify_channel_internal(api_key, channel, message):
    client = WebClient(token=api_key)
    try:
        _ = client.chat_postMessage(
            channel=channel,
            text=message)
        return True
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(f"Got an error: {e.response['error']} for channel {channel} and message {message}")
        return e.response["ok"] is False


def notify_user_internal(api_key, user_id, message):
    client = WebClient(token=api_key)
    try:
        _ = client.chat_postMessage(channel=user_id, text=message)
        return True
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(f"Got an error: {e.response['error']} for message {message}")
        return e.response["ok"] is False


def notify_user(api_key, username, message):
    # For testing...
    # notify_user_internal(api_key, 'U04PX1BUA', '[For %s] %s' % (username, message))
    notify_channel_internal(api_key, '#release-boss-audit-log', '[For %s] %s' % (username, message))
    notify_user_internal(api_key, username, message)
