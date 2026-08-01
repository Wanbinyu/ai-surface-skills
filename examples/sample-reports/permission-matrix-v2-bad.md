# Golden report - tool-permission-matrix on v2-bad

| tool | effect | sensitivity | read-only agent | coder | admin | HITL? |
|------|--------|-------------|-----------------|-------|-------|-------|
| list_orders | read (claimed cross-user) | PII | deny until fixed | deny | allow after authz fix | no |
| place_order | write / money | PII + money | deny | allow + idempotency | allow | optional |
| get_order | read | PII | allow (scoped) | allow | allow | no |
| refund_order | money / destructive | money | **deny** | **deny** | allow | **yes** |

## Default policy

- Read-only agent: only scoped `get_order` after list_orders is fixed  
- Never enable `refund_order` without human-approval-gates  
- Fix list_orders description/authz before any auto mode  
