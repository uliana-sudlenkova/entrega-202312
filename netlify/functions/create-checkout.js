const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  try {
    const { priceId } = JSON.parse(event.body);

    const ALLOWED_PRICES = [
      process.env.PRICE_4_SESSIONS,
      process.env.PRICE_8_SESSIONS,
      process.env.PRICE_12_SESSIONS,
    ];

    if (!ALLOWED_PRICES.includes(priceId)) {
      return { statusCode: 400, body: JSON.stringify({ error: 'Invalid price' }) };
    }

    const session = await stripe.checkout.sessions.create({
      mode: 'payment',
      locale: 'ru',
      line_items: [{ price: priceId, quantity: 1 }],
      success_url: `${process.env.BASE_URL}/success.html`,
      cancel_url: `${process.env.BASE_URL}/#pricing`,
    });

    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url: session.url }),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: err.message }),
    };
  }
};
