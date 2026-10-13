# PR: Manage Cappy's snack inventory

## Summary

This change adds basic restocking and reservation operations for the Coding Interview Club's snack inventory.

## Expected behavior

- Quantities are non-negative integers; invalid quantities are rejected consistently.
- Restocking a positive quantity increases available stock.
- A successful reservation decreases stock by the requested quantity.
- A reservation that cannot be fulfilled leaves inventory unchanged.
- Invalid operations must not corrupt inventory state.

## Review task

Review the implementation and tests against the inventory rules. Correct the implementation and any misleading or incomplete tests, then add useful regression coverage for state changes and invalid input.
