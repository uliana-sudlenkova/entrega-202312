# Security Check

Run a full security audit on the project.

## Instructions

Use the `security` agent to audit the following files:
1. `netlify/functions/create-checkout.js` — Stripe integration, secret handling
2. `index.html` — inline scripts, Stripe frontend code, form handling
3. All other `*.html` pages — XSS surface, form fields
4. `assets/js/main.js` — DOM manipulation, event handlers
5. `package.json` — dependency versions

## Focus areas (in priority order)
1. Stripe secret key exposure
2. `priceId` whitelist validation
3. XSS via `innerHTML` or jQuery `.html()`
4. Information disclosure in error responses
5. Outdated `stripe` npm package

## Output
Return the full security audit report from the security agent.
After the report, provide a one-line deploy recommendation:
- `✅ SAFE TO DEPLOY` — no Critical or High findings
- `⚠️ DEPLOY WITH CAUTION` — Medium findings only
- `🚫 DO NOT DEPLOY` — Critical or High findings present
