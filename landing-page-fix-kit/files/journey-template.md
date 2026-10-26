# Journey map: [offer/version]

Traffic → page → confirmation/delivery → first result → next offer → follow-up.

## Current state: evidence only
Unknown does not mean absent or broken. A CTA's wording is not evidence that its destination works. Quote inspected/provided artifacts; leave unseen downstream unknown.

| Stage | Provenance | Artifact/location + exact quote | User expectation / next action | Rubric status | Unknowns |
|---|---|---|---|---|---|
| Traffic | unknown | Not supplied | unknown | Cannot verify | Actual source message/audience |
| Page | | | | | |
| Confirmation/delivery | unknown | Not inspected | unknown | Cannot verify | Receipt, access, timing, recovery |
| First result | unknown | Not inspected | unknown | Cannot verify | Task, prerequisites, completion evidence |
| Next offer | unknown | Not supplied | unknown | Cannot verify | Approved offer, relevance, price/terms |
| Follow-up | unknown | Not supplied | unknown | Cannot verify | Actual messages, consent and suppression |

## Proposed journey: not a description of the live flow
All recommendations in this table are **proposed**. Populate only with approved offers; otherwise use “owner decision pending.” Do not invent a new paid offer. Separate transactional resource delivery from optional marketing; inspect applicable policy before recommending contact or tracking.

| Stage | Proposed job/action | Continuity/acceptance condition | Consent, privacy and fallback | Proposed observable event and limitation |
|---|---|---|---|---|
| Traffic | Continue exact approved incoming promise | Supply source before writing campaign copy | Only approved channel/audience | source_landing_view: allowed landing view with non-personal source ID; not proof the person read the ad |
| Page | State verified resource and one clear action | CTA, contents, terms agree | Disclose data use; no bundled consent assumptions | resource_request_accepted: authoritative acceptance, once per logical request; CTA click alone is intent |
| Confirmation/delivery | Confirm receipt; explain actual delivery/access and recovery | Same resource/version; queue state ≠ delivered | Contact only for approved purpose; do not expose email in event properties | delivery_provider_accepted and resource_access: different events; neither proves inbox receipt or reading |
| First result | Complete one defined useful task from verified resource | Completion cue and recovery path are explicit | No private inputs sent to analytics; optional self-report must be labeled | first_result_reported or task_completed_observed: distinguish self-report from directly observed task completion |
| Next offer | Present only owner-approved optional next step after value | Link identity/terms and relevance verified | Respect eligibility and choice; do not gate already-promised resource | next_offer_view / next_offer_action: not purchase or acceptance without authoritative confirmation |
| Follow-up | State-appropriate assistance and optional next step | Stop obsolete reminders when outcome confirmed | Verify purpose-specific consent before sends; unsubscribe suppression; unknown consent means no optional marketing recommendation to send | followup_eligible / opted_out: eligibility ≠ sent; send/open/click ≠ first result |

## Event dictionary and decision plan (proposed, not installed)
For each event record: precise trigger, source of truth, once-per-logical-action dedupe key, allowed properties, consent requirement, data owner, retention, failure meaning, denominator and period. Use opaque IDs; no names, emails, prompt contents or private source material. Minimize linkable identifiers. No raw IP or device fingerprinting recommendation.

Measure separately: allowed page views → accepted requests → resource accesses → observable/self-reported first results → approved next-offer actions. Document attribution window, bots/internal traffic, retries, consent-denied traffic, cross-device loss and missing observations. No supplied data means baseline and conversion rates **unknown**. Do not divide incompatible populations or present missing events as zero.

Hypothesis: [falsifiable behavioral prediction, not a fact]. Primary metric: [defined numerator/denominator]. Guardrails: [access errors, unsubscribe/complaint signals, privacy, task success]. Evaluation rule/sample/window: [owner agreement pending; no made-up significance]. Execution is outside this read-only audit; no trackers or test leads are created.

## Evidence required before approval
[Exact traffic artifact; approved resource; captured confirmation/delivery states; approved next-offer brief or no offer; redacted follow-up and consent/suppression policy; anonymized event evidence.]
