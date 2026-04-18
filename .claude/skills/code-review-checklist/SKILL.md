---
name: code-review-checklist
description: Comprehensive code review checklist for this project. Preloaded into reviewer agent. Covers HTML, CSS, JS, and Netlify Functions quality checks.
user-invocable: false
---

# Code Review Checklist Skill

Use this checklist when reviewing code changes. Check each applicable category.

## HTML

- [ ] Semantic structure: correct heading hierarchy (h1→h2→h3), landmark elements
- [ ] Bootstrap classes correct and consistent with existing patterns
- [ ] Class names follow `section_element` snake_case convention
- [ ] No inline styles — CSS classes used instead
- [ ] No broken asset references (check image `src`, script `src`, link `href`)
- [ ] Russian text grammatically correct and consistent in tone
- [ ] Section wrapper uses `section_space_lg decoration_wrapper` pattern
- [ ] Same CSS/JS block as other pages (no missing or extra files)
- [ ] Header and footer identical to other pages

## CSS

- [ ] Uses CSS custom properties (`var(--primary)`, `var(--secondary)`, etc.)
- [ ] No hardcoded color values that should be variables
- [ ] No `!important` unless clearly justified with a comment
- [ ] Mobile-first: breakpoints use Bootstrap conventions (col-sm, col-md, col-lg)
- [ ] No duplicate rules already defined elsewhere in `style.css`
- [ ] Transition uses `var(--transition)` where appropriate

## JavaScript

- [ ] jQuery used consistently — no mixing with vanilla `document.querySelector`
- [ ] All DOM code inside `$(document).ready()`
- [ ] No `console.log` statements left in code
- [ ] No global variables (scope properly inside functions)
- [ ] Stripe/payment logic stays inline in `index.html` — not moved to `main.js`
- [ ] Event listeners use delegation where elements are dynamically added

## Netlify Functions

- [ ] HTTP method validated as first step
- [ ] `JSON.parse(event.body)` wrapped in try/catch
- [ ] `priceId` (or any sensitive param) validated against a server-side whitelist
- [ ] No secrets or sensitive values in response bodies or `console.log`
- [ ] All code paths return a response object (no implicit `undefined`)
- [ ] `Content-Type: application/json` header set on success responses
- [ ] Error messages to client are generic — no stack traces

## Performance

- [ ] Images use optimized versions (check for `-min` suffix)
- [ ] No unnecessary JS/CSS loaded on pages that don't need it
- [ ] No blocking scripts in `<head>` — scripts before `</body>`

## Verdict format

```
## Code Review Report

### Summary
[1-2 sentence overall assessment]

### Issues

#### 🔴 Critical (must fix before deploy)
- [file:line] Description and suggested fix

#### 🟡 Warning (should fix)
- [file:line] Description and suggested fix

#### 🔵 Suggestion (nice to have)
- [file:line] Description

### Verdict
APPROVE | REQUEST CHANGES | NEEDS DISCUSSION
```
