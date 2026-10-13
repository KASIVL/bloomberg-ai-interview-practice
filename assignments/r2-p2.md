# Ticket: Failed orders incorrectly affect inventory

## Problem

A customer reports that inventory becomes unavailable after an order fails during payment. Investigate the order flow across the route, order service, payment adapter, inventory, and repository.

## Acceptance criteria

- Invalid orders fail without corrupting state.
- Inventory is reserved or deducted only as defined by the successful-order workflow.
- Failed payment authorization does not permanently reduce available inventory.
- A successful order does not deduct inventory more than once.
- Retrying a completed order with the same identifier does not duplicate its effects.
- Payment uses the included in-memory fake; no external service is needed.

## Investigation

Follow one order from request validation through inventory and payment state changes. Identify what happens on success, failure, and retry. Check whether the tests assert the inventory invariant and whether they would catch a regression. Make a focused fix and add regression tests for the state transitions you verify.
