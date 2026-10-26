# AMG MCP guide journey: proposal, not inspected downstream

## Current evidence
R1 = real-case-observation.json / real-case-page-copy.txt, a real read-only public-page DOM text capture; not a synthetic fixture. The route is https://get.aimoneygroup.com/ultimate-claude-code-mcp-guide.[1]

| Stage | Provenance/status | Evidence and limits |
|---|---|---|
| Traffic | unknown / Cannot verify | No incoming campaign artifact or analytics supplied |
| Page | observed / mixed, see worked-audit.md | R1 “FREE 23-PAGE GUIDE + DEMO KIT”, “Get the PDF by email.”, “YES, SEND ME THE MCP GUIDE”; internal contents mismatch documented as F1[1] |
| Confirmation/delivery | unknown / Cannot verify | “Get the PDF by email.” is a promise, not proof of submission, redirect, queue, inbox receipt or access[1] |
| First result | unknown / Cannot verify | R1 promises “Use the included fictional brief demo to retrieve source facts before creating a marketing draft.” Actual resource and task completion unseen[1] |
| Next offer | unknown / Cannot verify | No approved next offer supplied; do not invent one |
| Follow-up | unknown / Cannot verify | R1 says “relevant AI Money Group emails” and “Unsubscribe anytime.” Actual messages, consent records and suppression uninspected[1] |

All unseen downstream stages remain **unknown**, not absent, defective or verified. “STEP 1 OF 3” appears in R1; it does not prove what steps 2 and 3 contain.[1]

## Proposed continuity plan
Every entry below is **proposed**, contingent on owner confirmation and resource review. No new offer, automation, tracker or email has been created. No action is authorized by this document.

| Stage | Proposed experience | Approval/consent/fallback | Proposed observable events; limits |
|---|---|---|---|
| Traffic → page | Continue the exact approved resource promise | Obtain actual source first; do not write a fictional acquisition claim | landing_view with permitted non-personal source ID; does not prove ad exposure or reading |
| Page → confirmation/delivery | After an accepted request, explain the actual access/delivery process and recovery route for this same guide | Verify existing flow and expected timing before writing details; do not promise instant delivery. Separate resource purpose from optional marketing consent | request_accepted once per logical accepted request; delivery_provider_accepted distinct from inbox receipt; resource_access distinct from reading |
| Delivery → first result | If the guide supports it, help the reader retrieve fictional approved-brief facts and produce one marketing draft, then verify facts/permissions | Review actual kit first; keep publishing/sending behind human approval. Offer recovery instructions from the verified resource; no private brief text in tracking | first_result_reported only for optional explicit user confirmation; task_completed_observed only if actual completion is observable. Download/click is not completion |
| First result → next offer | Owner decision pending; keep optional next step relevant to the completed task | No approved paid offer, price or terms supplied. Do not substitute an invented product or label a hub link an upsell | next_offer_view/action only if an approved offer exists; otherwise not applicable, not zero conversions |
| Next offer → follow-up | Provide state-appropriate help; offer next step only when approved and allowed | Verify resource-delivery purpose and applicable marketing consent separately. Unknown consent means do not recommend sending optional marketing. Suppress on unsubscribe; do not infer task success from opens | followup_eligible, opted_out; provider acceptance/open/click never proves useful first result; delivery and marketing eligibility stay separate |

## Proposed measurement contract
- Events are candidate names, **not installed or verified tracking**. Baseline, counts, conversion rates, attribution, reporting period and expected gains are **unknown**.
- Before implementation, owner defines trigger, source of truth, once-per-logical-request deduplication, retries, allowed opaque IDs, consent gate, retention and reporting window. No email/name/private brief/prompt content in analytics.
- Compare compatible populations only: permitted landing views → accepted requests → resource accesses → separately reported/observed first results → approved next-offer actions. Document missing consent, cross-device loss, internal traffic and bots rather than treating missing observations as zero.
- Optional **test hypothesis**: a resource-matched contents list improves comprehension. Proposed primary outcome: correctly identifying the resource and first task in a supplied comprehension study. Business conversion metric, baseline, sample, window and decision rule remain owner decisions. Guardrails: inaccurate promises, access errors and complaint/unsubscribe signals. No test is run here; no forecast is supplied.

## Needed to replace unknowns
Exact traffic artifact; approved PDF/demo kit/version; redacted confirmation and delivery states; first-use task evidence; approved next offer or explicit no-offer decision; actual follow-up and consent/suppression policy; anonymized event dictionary and report. Request supplied artifacts instead of submitting a form or sending messages.

## Sources
[1] https://get.aimoneygroup.com/ultimate-claude-code-mcp-guide
