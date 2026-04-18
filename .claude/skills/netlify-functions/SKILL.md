---
name: netlify-functions
description: Patterns for writing and modifying Netlify Functions in this project. Use when creating serverless functions, handling HTTP requests, or managing environment variables.
user-invocable: false
---

# Netlify Functions Skill

## Setup

- Functions live in `netlify/functions/`
- Bundled with esbuild (configured in `netlify.toml`)
- Runtime: Node.js, CommonJS (`require`)
- Invoked at `/.netlify/functions/<name>`

## Standard function template

```js
exports.handler = async (event) => {
  // 1. Validate HTTP method
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  // 2. Parse body safely
  let body;
  try {
    body = JSON.parse(event.body);
  } catch {
    return { statusCode: 400, body: JSON.stringify({ error: 'Invalid JSON' }) };
  }

  // 3. Validate inputs
  const { requiredField } = body;
  if (!requiredField) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Missing required field' }) };
  }

  // 4. Business logic
  try {
    const result = await doSomething(requiredField);
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ result }),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Internal server error' }),
    };
  }
};
```

## Environment variables

Access via `process.env.VAR_NAME`. All vars are set in:
- Netlify Dashboard → Site Settings → Environment Variables (production)
- `.env` file locally with `netlify dev` (never commit `.env`)

Current vars: `STRIPE_SECRET_KEY`, `PRICE_4_SESSIONS`, `PRICE_8_SESSIONS`, `PRICE_12_SESSIONS`, `BASE_URL`

## Local development

```bash
netlify dev   # starts local server at localhost:8888
              # functions available at localhost:8888/.netlify/functions/<name>
```

## Rules

- Always validate HTTP method first
- Always wrap `JSON.parse(event.body)` in try/catch — body can be null
- Validate all inputs against a whitelist when they map to sensitive values
- Return `Content-Type: application/json` on all success responses
- Return generic error messages — never stack traces or secret values
- Never `console.log` secret values
