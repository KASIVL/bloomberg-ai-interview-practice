# Ticket: Cancelled registrations still consume event capacity

## Problem

After a student cancels an event registration, another student may still be told that the event is full. Investigate the request path and determine why a cancelled registration continues to affect capacity.

## Acceptance criteria

- Each event has a fixed capacity.
- Active registrations consume capacity; cancelled registrations do not.
- A student cannot hold duplicate active registrations for the same event.
- Capacity is never exceeded.
- Cancelling an active registration frees its place for another student.
- Invalid or repeated cancellation attempts do not damage registration state.

## Investigation

Trace registration creation and cancellation through the route, service, repository, and data model. Compare behavior with the tests, and decide which assertions actually prove the ticket's requirements. Make a focused fix and add regression coverage for the behavior you reproduce.
