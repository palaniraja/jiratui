from datetime import datetime


def format_relative_time(value: datetime | None) -> str:
    """Formats a datetime as a compact relative time string.

    Examples: "5 minutes ago", "in 2 hours".
    """

    if value is None:
        return ''

    now = datetime.now(value.tzinfo) if value.tzinfo else datetime.now()
    delta_seconds = int((now - value).total_seconds())
    is_future = delta_seconds < 0
    seconds = abs(delta_seconds)

    if seconds < 60:
        amount = seconds
        unit = 'second'
    elif seconds < 3600:
        amount = seconds // 60
        unit = 'minute'
    elif seconds < 86400:
        amount = seconds // 3600
        unit = 'hour'
    else:
        amount = seconds // 86400
        unit = 'day'

    plural = 's' if amount != 1 else ''
    if is_future:
        return f'in {amount} {unit}{plural}'
    return f'{amount} {unit}{plural} ago'