# PR: Add student access code validation

## Summary

This change adds a small validator for student access codes before they are accepted by the club registration flow.

## Expected behavior

- A valid code is a string containing exactly six ASCII digits (`0` through `9`).
- Leading zeros are meaningful and valid.
- Every other value is invalid and returns `False`.
- Invalid strings must be handled as ordinary validation failures, without raising an exception.

## Review task

Review the proposed implementation and its tests against the behavior above. Make the necessary corrections in the implementation and tests. Run the test suite and explain which cases give you confidence in the result.
