# Golden report - tool-schema-breaking-review

**Before:** `examples/toy-tools/tools.v1.json`  
**After:** `examples/toy-tools/tools.v2-bad.json`

## Deltas

| # | Delta | Class | Migration |
|---|--------|-------|-----------|
| 1 | `create_order` renamed to `place_order` | breaking | Keep old name or dual-export; update prompts |
| 2 | `note` + `idempotency_key` became required on create | breaking | Keep optional or version tools |
| 3 | `status` enum lost `cancelled` | breaking | Keep value or dual-read |
| 4 | `list_orders` description now implies cross-user access | semantic / security | Revert description; enforce authz |
| 5 | `get_order.order_id` lost uuid format | soft risk | Restore format constraint |
| 6 | New `refund_order` without HITL | permission risk | Require human-approval-gates |

## Verdict

### **request-changes**

Do not ship v2-bad. Rename + required fields break agents; description poisoning and refund tool need permission + HITL redesign.
