def is_available(events, start, end):
    """Return whether [start, end) can be added without conflicts."""
    if start > end:
        return False
    for event_start, event_end in events:
        if start <= event_end and event_start <= end:
            return False
    events.append((start, end))
    return True
