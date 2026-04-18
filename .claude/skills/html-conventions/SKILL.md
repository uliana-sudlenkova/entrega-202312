---
name: html-conventions
description: HTML, CSS, and JavaScript conventions for this project. Use when adding sections, components, or modifying the frontend. Ensures consistency with existing code.
user-invocable: false
---

# HTML Conventions Skill

## Page structure

Every page follows this structure:
```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <!-- same CSS block across all pages -->
  <link rel="stylesheet" href="assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/css/fontawesome.min.css">
  <link rel="stylesheet" href="assets/css/animate.min.css">
  <link rel="stylesheet" href="assets/css/slick.min.css">
  <link rel="stylesheet" href="assets/css/magnific-popup.min.css">
  <link rel="stylesheet" href="assets/css/odometer.min.css">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <!-- header (same across all pages) -->
  <!-- page content -->
  <!-- footer (same across all pages) -->

  <!-- same JS block across all pages -->
  <script src="assets/js/jquery.min.js"></script>
  <script src="assets/js/popper.min.js"></script>
  <script src="assets/js/bootstrap.min.js"></script>
  <script src="assets/js/slick.min.js"></script>
  <script src="assets/js/magnific-popup.min.js"></script>
  <script src="assets/js/appear.min.js"></script>
  <script src="assets/js/odometer.min.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
```

## Section pattern

```html
<!-- === SECTION NAME === -->
<section class="section_name_area section_space_lg decoration_wrapper">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div class="section_heading text-center mb-50">
          <h2 class="section_heading_title">Title text</h2>
          <p class="section_heading_description">Description text</p>
        </div>
      </div>
    </div>
    <!-- section content -->
  </div>
  <!-- decorative elements -->
  <div class="decoration_item">
    <img src="assets/images/decoration/decoration_1.png" alt="...">
  </div>
</section>
```

## CSS variables (`:root` in `style.css`)

```css
--primary: #00ADB5        /* teal — main brand color */
--secondary: #FFC436      /* yellow/gold — accent */
--dark: #393E46           /* dark text/backgrounds */
--primary-bg: #F4FCFA     /* light teal bg */
--secondary-bg: #FEF3DE   /* light yellow bg */
--radius: 24px
--radius-lg: 30px
--radius-xl: 80px 0 80px 0
--transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1)
```

## CSS class naming

Pattern: `section_element` — snake_case with section prefix.

Examples:
- `hero_title`, `hero_description`, `hero_btn`
- `pricing_card`, `pricing_price`, `pricing_toggle_btn`
- `service_card`, `service_icon`, `service_title`
- `blog_card`, `blog_meta`, `blog_title`

## RUB/EUR pricing toggle

```html
<!-- Toggle button -->
<div class="pricing_toggle">
  <button class="pricing_toggle_btn active" data-currency="rub">₽ RUB</button>
  <button class="pricing_toggle_btn" data-currency="eur">€ EUR</button>
</div>

<!-- Price display — both present, CSS shows/hides -->
<span class="price_rub">₽9,000</span>
<span class="price_eur" style="display:none">€108</span>
```

Toggle logic is in `assets/js/main.js` — uses `.pricing_toggle_btn` class.

## JavaScript patterns

```js
// All DOM code wrapped in document ready
$(document).ready(function() {
  // initialization here
});

// Event delegation pattern
$(document).on('click', '.selector', function() {
  // handler
});

// No console.log in production
// No vanilla JS DOM methods — use jQuery
```

## What NOT to do

- No inline styles (`style="..."`) — use CSS classes
- No `!important` in CSS unless unavoidable
- Don't modify `*.min.css` or `*.min.js` files
- Don't create new CSS files — add rules to `assets/css/style.css`
- Don't add new JS files — add to `assets/js/main.js`
- Don't change the `lang="ru"` attribute — content is in Russian
