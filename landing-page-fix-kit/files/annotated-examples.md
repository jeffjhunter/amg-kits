# Annotated examples

These are illustrative audit patterns, not page analytics or proof of business results. Example 2 uses the preserved real AMG observation; the others are explicitly synthetic teaching artifacts. Never merge synthetic evidence into a real audit.

## 1. Good: leave it alone (synthetic teaching example)
Artifact S1, supplied sample header: “Free checklist. Get the PDF by email.” CTA: “Email me the checklist.”
- Provenance: **provided** synthetic copy, not a live page observation.
- A1 action semantics: **Meets**, within copy-only scope. The action and promised delivery agree.
- Recommendation: leave the CTA alone. No defect finding. Form behavior, layout and inbox delivery **Cannot verify**.
- Wrong: “Make the button orange to increase conversions.” There is no visual or outcome evidence.

## 2. Real copy mismatch: one supported finding
Artifact R1 = real-case-page-copy.txt, original real-case-observation.json, live public page recorded by read-only DOM text inspection; not a synthetic fixture.[1]
Header: “FREE 23-PAGE GUIDE + DEMO KIT”. Intro: “Connect tools with MCP, retrieve an approved brief, and turn it into a useful marketing draft. Start with a read-only demo, then learn how to connect a real service safely.” Lower WHAT YOU GET: “One-page Claude model decision tree” and “Four-part task complexity test”.[1]
- Provenance: **observed**, text-only. M2: **Needs work**. Type: **observed defect** (internal contents/offer mismatch).
- Interpretation: the lower contents list introduces a different model-selection/task-complexity promise from the MCP workflow described above. This is a copy contract inconsistency, not proof of lost leads or proof of what the PDF actually contains.
- Proposed correction: verify the actual guide and align the lower contents list to it. Do not add a new resource or invent contents. See worked-audit.md for exact candidate wording and approval gate.
- Wrong: “The Facebook ad is misleading and conversion fell 20%.” No traffic artifact or analytics was inspected.

## 3. Invalid proof pairing (synthetic teaching example)
Artifact S3, supplied fictional claim/proof pair: “Our workflow doubles client bookings.” Proof card: “I liked the clean template.”
- Provenance: **provided** synthetic pair. P2/P3: **Needs work** for the inspected pairing. Type: **rubric concern**.
- Exact mismatch: liking a template does not substantiate doubling bookings. It does not establish the quantitative claim is false; other substantiation is **unknown**.
- Proposed correction: request relevant source/method, denominator and period; otherwise narrow/remove the unsupported outcome claim with owner approval. Do not invent a case study or replace it with another number.
- Wrong: “Add a verified success story.” None has been supplied. A testimonial is not causal outcome evidence merely because it has a name.

## 4. Blocked view (synthetic teaching example)
Artifact S4, hypothetical supplied access log: “403 Forbidden”. No screenshots or page copy supplied.
- Provenance: **provided**, synthetic failure report. Page rubric: **Cannot verify**. This is a verification gap, not an observed page defect.
- Correct response: “I cannot inspect the page from this artifact. Please supply exact copy and full-page desktop/mobile screenshots, including CTA, form and footer. I cannot assess layout, mobile usability, offer clarity or downstream behavior yet.”
- A failure log can be quoted as access evidence; it cannot support findings about the unseen page. Do not fill a five-finding quota.
- Wrong: “Your hero is cluttered, the mobile button is hidden and the offer lacks proof.” None is visible.

## Sources
[1] https://get.aimoneygroup.com/ultimate-claude-code-mcp-guide
