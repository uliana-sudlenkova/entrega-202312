# Project Context

## Business
- **Owner:** Ulyana Grau, psychologist specializing in BPD treatment
- **Audience:** Russian-speaking clients (primarily based in Spain/Europe)
- **Goal:** Book therapy sessions and provide information about services

## Key pages
| Page | Purpose |
|------|---------|
| `index.html` | Main landing page (hero, services, pricing, FAQ, contact) |
| `about.html` | About Ulyana |
| `blog.html` | Blog listing |
| `blog-1.html`, `blog-2.html` | Individual blog posts |
| `contact.html` | Contact page |
| `oferta.html` | Public offer / legal terms (Russian) |
| `private-police.html` | Privacy policy (Russian) |
| `success.html` | Post-payment confirmation |

## Payments
- 3 packages: 4 sessions (₽9,000/€108), 8 sessions (₽16,000/€192), 12 sessions (₽21,000/€252)
- Flow: `buyPackage(priceId)` → `/.netlify/functions/create-checkout` → Stripe → `success.html`
- Currency toggle: `.pricing_toggle_btn` switches between RUB and EUR display

## Environment variables (Netlify)
- `STRIPE_SECRET_KEY` — Stripe secret key (server only)
- `PRICE_4_SESSIONS`, `PRICE_8_SESSIONS`, `PRICE_12_SESSIONS` — Stripe Price IDs
- `BASE_URL` — e.g. `https://ulyanagrau.com`

## Contact
- Phone: +34 66 08 63 998
- Email: ulyanagrau@gmail.com
- Social: Instagram, WhatsApp
