# QA Check

Run a full QA pass to catch bugs before deploying.

## Instructions

Use the `qa` agent to test the following:

### Always check
- Payment flow: `buyPackage()` → `create-checkout` function → Stripe → `success.html`
- Pricing toggle: RUB/EUR switch works correctly
- All internal navigation links point to existing pages
- JS initializations (Slick, Odometer, Magnific Popup) target elements that exist

### Check if recently changed
- Any HTML pages modified — validate structure, links, class names
- `create-checkout.js` — function handles all edge cases
- `main.js` — no broken selectors or event handlers

## Output
Return the full QA report from the qa agent.
After the report, provide a deploy recommendation:
- `✅ READY TO DEPLOY` — no Blockers or Majors
- `⚠️ MINOR ISSUES` — only Minor bugs (can deploy, fix in follow-up)
- `🚫 NOT READY` — Blocker or Major bugs found
