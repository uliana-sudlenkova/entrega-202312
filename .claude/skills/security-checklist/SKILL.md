---
name: security-checklist
description: Security audit checklist for this project. Preloaded into security agent. Covers Stripe secret handling, XSS, injection, and OWASP Top 10 issues relevant to this stack.
user-invocable: false
---

# Security Checklist Skill

## Priority 1: Stripe & Payments (CRITICAL)

- [ ] `STRIPE_SECRET_KEY` referenced ONLY in `netlify/functions/` — never in HTML, JS, or any frontend file
- [ ] `priceId` validated against `ALLOWED_PRICES` server-side before creating a session
- [ ] No price amounts set client-side — prices come from Stripe product configuration
- [ ] `success_url` and `cancel_url` use `process.env.BASE_URL` — not hardcoded
- [ ] Stripe checkout sessions use HTTPS URLs only (Netlify enforces HTTPS in production)
- [ ] Webhook handler (if exists) validates `stripe-signature` before processing any event

## Priority 2: XSS (Cross-Site Scripting)

- [ ] No `innerHTML`, `document.write`, `eval()`, or `$.html()` called with untrusted data
- [ ] Form field values never inserted directly into the DOM without sanitization
- [ ] jQuery selectors don't use user-supplied strings
- [ ] Contact form uses Netlify Forms built-in handling — no custom DOM injection

## Priority 3: Netlify Functions

- [ ] HTTP method checked before any other processing
- [ ] `JSON.parse(event.body)` in try/catch — null body handled
- [ ] No raw Stripe error messages returned to client
- [ ] No dynamic `require()` with user-controlled paths
- [ ] No `console.log` of secret values or tokens
- [ ] Error responses use generic messages (no stack traces, no internal paths)

## Priority 4: Information Disclosure

- [ ] No `.env` file committed (verify `.gitignore` includes `.env`)
- [ ] No debug HTML comments exposing architecture, credentials, or file paths
- [ ] No Stripe Price IDs or secret key fragments visible in HTML source
- [ ] `package.json` `stripe` version is current (check for known CVEs)

## Priority 5: Form Security

- [ ] Contact form uses Netlify Forms (no custom server-side handler exposed)
- [ ] No hidden form fields that bypass business logic if manipulated
- [ ] No sensitive data in GET query parameters

## Audit report format

```
## Security Audit Report

### Summary
Overall risk: LOW | MEDIUM | HIGH | CRITICAL

### Findings

#### 🔴 Critical
- [file:line] Vulnerability — Impact — Remediation

#### 🟠 High
- [file:line] Vulnerability — Impact — Remediation

#### 🟡 Medium
- [file:line] Vulnerability — Impact — Remediation

#### 🔵 Informational
- [file:line] Observation — Recommendation

### Sign-off
PASS | FAIL — [brief justification]
```

## Sign-off criteria

- **PASS**: No Critical or High findings
- **FAIL**: Any Critical or High finding present
