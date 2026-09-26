# Solutioning Examples

# Orchestration patterns

The core design object is a workflow, not a chatbot.

## Pattern 1 - Collections next-best-action
ERP + AR + CRM + documents + email.

**See:** invoice due, promise broken, dispute, customer risk.
**Think:** reconcile payment history, terms, dispute context and relationship.
**Act:** draft/send approved communication, route dispute, update worklist.
**Human:** collector owns negotiation and escalation.
**Measure:** DSO, productivity, promise-to-pay kept.

## Pattern 2 - Demand-to-supply
CRM + ERP + SCM + external signals.

Agent senses demand or supply changes, reasons through constraints, recommends a scenario and routes material trade-offs to a planner.

## Pattern 3 - Quote-to-conversion
CRM + product data + CPQ + documents + email.

Agent detects buying intent, assembles context, identifies gaps, prepares proposal inputs and coordinates follow-up. Seller owns commercial judgement.

## Pattern 4 - Service exception
CRM + service + telemetry + ERP.

Agent correlates entitlement, asset, history, parts and SLA, then schedules or routes the case. Critical decisions remain human.

## Pattern 5 - AI pilot-to-production fabric
AI apps + data + identity + governance + workflows.

Convert isolated pilots into reusable production patterns with monitoring, identity, policy and measurable outcomes.

## Design rule

Every SV system should be explainable as:

**signal → context → reasoning → action → human checkpoint → system update → KPI → learning**
