---
name: stripe-checkout
description: Patterns and conventions for implementing Stripe Checkout in this project. Use when creating or modifying payment flows, adding packages, or implementing webhooks.
user-invocable: false
---

# Stripe Checkout Skill

## Current integration

- **SDK:** `stripe@^14` via CommonJS `require('stripe')`
- **Mode:** `payment` (one-time, not subscription)
- **Locale:** `ru`
- **Entry point:** `netlify/functions/create-checkout.js`

## Pattern: creating a checkout session

```js
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  locale: 'ru',
  line_items: [{ price: priceId, quantity: 1 }],
  success_url: `${process.env.BASE_URL}/success.html`,
  cancel_url: `${process.env.BASE_URL}/#pricing`,
  // Optional enhancements:
  allow_promotion_codes: true,
  customer_email: customerEmail,  // prefill email if known
  metadata: { package: '4_sessions' },
  payment_intent_data: { description: '4 psychology sessions — Ulyana Grau' },
});
return { statusCode: 200, headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ url: session.url }) };
```

## Pattern: validating priceId (mandatory)

```js
const ALLOWED_PRICES = [
  process.env.PRICE_4_SESSIONS,
  process.env.PRICE_8_SESSIONS,
  process.env.PRICE_12_SESSIONS,
];
if (!ALLOWED_PRICES.includes(priceId)) {
  return { statusCode: 400, body: JSON.stringify({ error: 'Invalid price' }) };
}
```

## Pattern: webhook handler

```js
// netlify/functions/stripe-webhook.js
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event) => {
  const sig = event.headers['stripe-signature'];
  let stripeEvent;
  try {
    stripeEvent = stripe.webhooks.constructEvent(
      event.body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET
    );
  } catch (err) {
    return { statusCode: 400, body: `Webhook Error: ${err.message}` };
  }

  if (stripeEvent.type === 'checkout.session.completed') {
    const session = stripeEvent.data.object;
    // handle post-payment logic here
  }

  return { statusCode: 200, body: JSON.stringify({ received: true }) };
};
```

## Adding a new package — steps

1. Create product + price in Stripe Dashboard → copy Price ID
2. Add env var `PRICE_X_SESSIONS` in Netlify site settings
3. Add to `ALLOWED_PRICES` array in `create-checkout.js`
4. Add HTML card + `buyPackage('...')` button in `index.html`
5. Add RUB and EUR price elements with toggle classes
6. Update `CLAUDE.md` pricing table

## Frontend call pattern (inline in index.html)

```js
async function buyPackage(priceId) {
  const res = await fetch('/.netlify/functions/create-checkout', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ priceId }),
  });
  const data = await res.json();
  if (data.url) window.location.href = data.url;
}
```

## Security rules (non-negotiable)

- `STRIPE_SECRET_KEY` only in Netlify Function files — never in HTML/JS
- Always validate `priceId` server-side against whitelist
- Never set price amounts client-side
- Webhook handlers MUST verify `stripe-signature`
- Return generic error messages — never raw Stripe errors to client

## Test cards (Stripe test mode)

- Success: `4242 4242 4242 4242`
- Decline: `4000 0000 0000 0002`
- 3D Secure: `4000 0025 0000 3155`
- Any future date as expiry, any 3-digit CVV
