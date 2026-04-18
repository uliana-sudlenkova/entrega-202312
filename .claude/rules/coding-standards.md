# Coding Standards

## HTML
- Content language is Russian — preserve all existing Russian text exactly
- Class names: `section_element` snake_case with section prefix (e.g. `hero_title`, `pricing_card`)
- Section wrapper pattern: `<section class="section_space_lg decoration_wrapper">`
- No inline styles — use CSS classes
- All pages share the same `<head>` CSS block and `<body>` JS block

## CSS (assets/css/style.css)
- Use CSS custom properties: `var(--primary)`, `var(--secondary)`, `var(--dark)`, `var(--primary-bg)`
- Primary: `#00ADB5` | Secondary: `#FFC436` | Dark: `#393E46`
- Font: Montserrat / Noto Sans, base 18px (20px desktop)
- Border radius: `var(--radius)` = 24px, `--radius-lg` = 30px
- Transitions: `var(--transition)` = `all 0.4s cubic-bezier(0.25, 1, 0.5, 1)`
- Never modify `*.min.css` files

## JavaScript
- jQuery base — all DOM manipulation via jQuery
- Wrap DOM code in `$(document).ready(function() { ... })`
- No `console.log` in production
- Never modify `*.min.js` files

## Netlify Functions
- File: `netlify/functions/<name>.js`
- Pattern: validate method → parse body → validate input → call Stripe → return response
- Always return `Content-Type: application/json` header on success
- Generic error messages to client — never expose stack traces

## Git
- Auto-deploy from `main` branch via Netlify
- Keep PRs focused — one feature or fix per PR
- Test payment flow locally with `netlify dev` before pushing
