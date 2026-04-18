# Project: Ulyana Grau — Psychology Practice Website

## Description
Personal/professional website for a psychologist. Static site deployed on Netlify with Stripe payment integration.

## Tech stack
- **Frontend:** Static HTML5 + Bootstrap 5 + jQuery
- **Styles:** Custom CSS in `assets/css/style.css`
- **Animations:** Animate.css, Slick (carousel), Magnific Popup, Odometer (counters)
- **Icons:** FontAwesome
- **Deploy:** Netlify (static site + Netlify Functions)
- **Serverless backend:** `netlify/functions/create-checkout.js` (Node.js)
- **Payments:** Stripe Checkout
- **Function bundler:** esbuild (configured in `netlify.toml`)

## Project structure
```
ulyana-web/
├── public/                     # Public directory — only this is served by Netlify
│   ├── index.html              # Main landing page (hero, services, pricing, blog, contact)
│   ├── about.html              # About page
│   ├── blog.html               # Blog listing
│   ├── blog-1.html             # Blog post 1
│   ├── blog-2.html             # Blog post 2
│   ├── blog_details.html       # Blog post detail
│   ├── contact.html            # Contact page
│   ├── oferta.html             # Public offer / legal terms (Russian)
│   ├── private-police.html     # Privacy policy (Russian)
│   ├── success.html            # Post-payment confirmation
│   └── assets/
│       ├── css/                # Styles (style.css is the main custom file)
│       ├── js/                 # Scripts (main.js is the main custom file)
│       ├── images/             # Images organized by section
│       └── fonts/              # FontAwesome and Slick fonts
├── netlify/
│   └── functions/
│       └── create-checkout.js  # Creates Stripe Checkout sessions (never served publicly)
├── netlify.toml                # Netlify configuration (publish = "public")
└── package.json                # Node dependencies (stripe only)
```

## Payment functionality
Three psychology session packages with dual RUB/EUR pricing:
- **4 sessions:** ₽9,000 / €108
- **8 sessions:** ₽16,000 / €192
- **12 sessions:** ₽21,000 / €252

**Flow:** `buyPackage(priceId)` button → Netlify Function `create-checkout` → Stripe Checkout → `success.html`

### Required environment variables (Netlify)
- `STRIPE_SECRET_KEY` — Stripe secret key
- `PRICE_4_SESSIONS` — Stripe Price ID for 4-session package
- `PRICE_8_SESSIONS` — Stripe Price ID for 8-session package
- `PRICE_12_SESSIONS` — Stripe Price ID for 12-session package
- `BASE_URL` — Site base URL (e.g. `https://ulyanagrau.com`)

## Code conventions

### HTML
- Primary content language: **Russian** (`lang="ru"`)
- CSS classes follow `section_element` snake_case pattern with section prefix
- Main sections use `section_space_lg decoration_wrapper` classes
- Every page includes the same CSS block in `<head>` and JS block before `</body>`

### CSS (`assets/css/style.css`)
- Colors and fonts defined as CSS custom properties in `:root`
- No `!important` except in exceptional cases
- Mobile-first with Bootstrap breakpoints

### JavaScript (`assets/js/main.js`)
- jQuery is the base library
- `buyPackage()` is inline in `index.html` alongside Stripe logic
- No JS framework — keep vanilla JS or jQuery

### Netlify Functions
- Node.js with CommonJS (`require`)
- Always validate HTTP method before processing
- Validate inputs against whitelist (see `ALLOWED_PRICES` in `create-checkout.js`)
- Environment variables via `process.env`

## Security
- Never expose `STRIPE_SECRET_KEY` in frontend code
- Netlify Functions are the only server-side contact point with Stripe
- Always validate `priceId` against the allowed prices whitelist

## Useful commands
```bash
# Install dependencies
npm install

# Local development with Netlify CLI
netlify dev

# Deploy
git push origin main  # Netlify auto-deploys from main
```

## Development notes
- When modifying prices or packages, update both the HTML and Netlify environment variables
- Images should be optimized (filename suffix `-min` indicates compressed version)
- RUB/EUR price toggle is implemented with the `pricing_toggle_btn` class in `index.html`

---

## Agents & Commands

Agents are in `.claude/agents/` — each handles a specific role in the development pipeline.

| Agent | File | Role |
|-------|------|------|
| `developer` | `.claude/agents/developer.md` | Implements features and fixes |
| `stripe` | `.claude/agents/stripe.md` | Stripe payments specialist |
| `reviewer` | `.claude/agents/reviewer.md` | Code quality review (read-only) |
| `security` | `.claude/agents/security.md` | Security audit (read-only) |
| `qa` | `.claude/agents/qa.md` | Bug detection (read-only) |
| `docs` | `.claude/agents/docs.md` | Updates documentation |

### Slash commands

| Command | When to use |
|---------|-------------|
| `/new-feature` | Full pipeline: implement → review → security → QA → docs |
| `/review` | Code quality + security review after manual changes |
| `/security-check` | Full security audit before deploy |
| `/qa-check` | Full QA pass before deploy |
| `/update-docs` | Sync CLAUDE.md and inline comments after a feature ships |

### Skills (preloaded into agents)

| Skill | File | Preloaded in |
|-------|------|-------------|
| `html-conventions` | `.claude/skills/html-conventions/SKILL.md` | developer |
| `netlify-functions` | `.claude/skills/netlify-functions/SKILL.md` | developer, stripe |
| `stripe-checkout` | `.claude/skills/stripe-checkout/SKILL.md` | stripe |
| `code-review-checklist` | `.claude/skills/code-review-checklist/SKILL.md` | reviewer |
| `security-checklist` | `.claude/skills/security-checklist/SKILL.md` | security |

### Hooks

System in `.claude/hooks/` — logs events and warns on dangerous Bash commands.
- `scripts/hooks.py` — main handler (macOS notifications + logging)
- `config/hooks-config.json` — enable/disable per event
- `config/hooks-config.local.json` — personal overrides (git-ignored)
- `logs/hooks-log.jsonl` — event log (git-ignored)

### Rules
- `.claude/rules/coding-standards.md` — HTML/CSS/JS/Function conventions
- `.claude/rules/project-context.md` — Business context, pages, env vars
