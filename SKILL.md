---
name: cacao-design-system
description: Use when designing or building any page, section or component for the cacao ceremony website («Алхимия сердца»). Builds only from the Cacao design system.
---

# Cacao design system

Built on the **Signal** starter from [web-style-guide](https://github.com/hoomanab01/web-style-guide): same structure, token names and components, re-valued for a cacao ceremony.

The look: candle-lit cacao dark, an editorial high-contrast serif in normal case for headings (Playfair Display, like a café menu: «Алхимия сердца»), small spaced capitals in a clean sans for labels and subtitles (Inter, like «ПУТЕШЕСТВИЕ К СЕБЕ»), Inter for reading, handwritten names (Marck Script), thin gold line icons in rings, fading gold dividers with a four-point star, and a chocolate & cacao photo in the hero. Calm, warm, ceremonial. Pill buttons, round portraits.

Source of truth: `assets/tokens.css` (values) and `assets/components.css` (components). The storybook (`storybook.html`) shows every token and component.

## Hosts
Светлана Делле (Светлана-Яра) is the main host and always comes first, larger. Then Оксана, then Анастасия (sound healing).

## Language
- Pages are in Russian (`<html lang="ru">`). English is allowed for the «Inner Journey» label.
- Fonts include Latin and Cyrillic subsets. Do not add a font without a Cyrillic subset.
- The title «Алхимия сердца» stays on one line; «сердца» is the italic gold accent (`<em>`).
- Headings are in normal case (`--display-case: none`). Labels and subtitles are set in spaced capitals by `--label-case`; write everything in normal case in the HTML.
- The script font is for people's names only. Never for headings or body text.
- Avoid the arrow glyph (→) in display type; write «превращается в …» instead.

## Hard rules
1. Use tokens only. Never write a colour, font, size, radius, shadow or duration directly in a page. If a value is missing, propose adding a token first.
2. Use existing components before inventing new ones. If a page needs something new, say so, propose it as a component, and add it to `components.css` and the storybook once agreed.
3. One `display` or `h1` per page. Sections use `h2`, items inside sections use `h3`.
4. One primary button per view. Button labels start with a verb (Записаться, Узнать).
5. One inverse (ember) section per page, used for the closing call to action.
6. Every page works on a phone at 390px wide, with no horizontal scroll and touch targets of at least 44px.
7. Text contrast at least 4.5:1. Errors are shown in words, not colour alone.
8. Motion is subtle and slow: elements rise and fade in once with `data-reveal`; Lenis smooth scroll on every page (`assets/vendor/lenis.*` + `assets/motion.js`); one Vanta fog per page at most, behind the hero (`data-vanta="fog"`), wide screens only, colours from the `--vanta-*` tokens. Everything stops for visitors who prefer reduced motion.
9. No fake testimonials, reviews, numbers or event details. Unknown values (time, address, price, booking link) stay visibly marked with `tbd` until replaced.
10. Copy about the ceremony comes from the organisers' own text. Don't invent promises, effects or bios.
11. Images: the organisers' own photos (the poster, host portraits), original illustrations, or photos the organisers have a licence for (the chocolate photo, `assets/img/chocolate.jpg`, was supplied by Ekaterina). No other web photos.
12. Sign-up goes to Telegram: https://t.me/katrin_berlin (opens in a new tab). Every «Записаться» button links there.
13. Design decisions are made in Claude chat and recorded in the design system or a prototype. When building (Claude Code), never decide design: if something isn't defined, stop and ask with two or three options.

## Components (class names)
- Layout: `container`, `section`, `section--surface`, `section--inverse`, `section--tight`, `section-head`, `grid grid--2|grid--3`, `split`, `stack`
- Type: `display`, `h1`, `h2`, `h3`, `subtitle`, `script` (names only), `lead`, `body`, `small`, `eyebrow`, `measure`
- Ornament: `divider` (gold lines + star), `brand__mark` (the same star)
- Actions: `btn btn--primary`, `btn btn--secondary`, `btn-row`, `link`
- Blocks: `nav`, `hero` (candle glow), `hero--cinema` + `hero__frame` + `hero__facts` (full-bleed photo, gold frame, facts strip), `hero--photo` (photo on the right, fades in), `hero--center`, `hero__date`, `hero__meta`, `page-hero`, `section-head--center`, `card--center`, `icon-ring` (inline SVG line icon), `card`, `card__icon`, `steps` / `step`, `price` / `price--featured`, `badge`, `list`, `quote`, `faq`, `cta`, `footer`
- Cacao artwork: `has-cacao` (hero sides), `has-beans` (closing section corners). Original SVGs in `assets/img/`, regenerate with `tools/cacao-art.py`.
- Event: `facts` / `facts__row` (event details as a `<dl>`), `tbd` (visible placeholder), `host-lead` (main host, larger, with text), `hosts` / `hosts--pair` / `host` / `host__photo`, `poster` (framed event poster)
- Forms: `form`, `form__row`, `field`, `label`, `input`, `field__error`
- Motion: `data-reveal`, `data-vanta="fog"`. Every page loads `vendor/lenis.css`, `vendor/lenis.min.js` and `motion.js` (three.js and Vanta load on demand).
- Nav toggle labels: `data-label-open="Меню" data-label-close="Закрыть"`

## Page patterns
- Event landing (`prototypes/home.html`): cinema hero (full-bleed chocolate photo, gold frame with eyebrow, «Алхимия *сердца*» on one line, lead, Записаться + «Что вас ждёт →», facts strip: когда · где · формат), what awaits (3 icon-ring cards), hosts (Светлана first as `host-lead`, then Оксана and Анастасия), the alchemy (steps), details (split: facts + poster), closing CTA (inverse, with divider)
- Pricing, about, contact: as in the Signal starter, when needed

## Before you deliver
- [ ] Only tokens and existing components used
- [ ] Phone, tablet and desktop checked; no horizontal scroll
- [ ] One h1, one primary button per view, one inverse section
- [ ] Contrast and form errors checked
- [ ] Cyrillic renders in all three fonts; numbers are lining (15:00, not old-style)
- [ ] Placeholders replaced or clearly marked with `tbd`
- [ ] Impressum and Datenschutz linked before the page goes live in Germany

## Keeping this skill current
When a decision changes the system (a new token, a new component, a new rule), update this file in the same change. Claude chat should suggest it: "This should go into the design skill."
