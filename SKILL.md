---
name: cacao-design-system
description: Use when designing or building any page, section or component for the cacao ceremony website («Алхимия сердца»). Builds only from the Cacao design system.
---

# Cacao design system

Built on the **Signal** starter from [web-style-guide](https://github.com/hoomanab01/web-style-guide): same structure, token names and components, re-valued for a cacao ceremony.

The look: warm, deep, bold. Roasted-cacao dark background, cream text, one heart-gold accent, a soft terracotta glow in the hero. Wide, confident display type (Unbounded), calm body text (Inter), spaced uppercase mono labels (JetBrains Mono). Round shapes: pill buttons, circular marks.

Source of truth: `assets/tokens.css` (values) and `assets/components.css` (components). The storybook (`storybook.html`) shows every token and component.

## Language
- Pages are in Russian (`<html lang="ru">`). English is allowed for the «Inner Journey» label.
- Fonts include Latin and Cyrillic subsets. Do not add a font without a Cyrillic subset.
- Avoid the arrow glyph (→) in display type; write «превращается в …» instead.

## Hard rules
1. Use tokens only. Never write a colour, font, size, radius, shadow or duration directly in a page. If a value is missing, propose adding a token first.
2. Use existing components before inventing new ones. If a page needs something new, say so, propose it as a component, and add it to `components.css` and the storybook once agreed.
3. One `display` or `h1` per page. Sections use `h2`, items inside sections use `h3`.
4. One primary button per view. Button labels start with a verb (Записаться, Узнать).
5. One inverse (gold) section per page, used for the closing call to action.
6. Every page works on a phone at 390px wide, with no horizontal scroll and touch targets of at least 44px.
7. Text contrast at least 4.5:1. Errors are shown in words, not colour alone.
8. Motion is subtle and slow: elements rise and fade in once with `data-reveal`. Respect reduced motion.
9. No fake testimonials, reviews, numbers or event details. Unknown values (time, address, price, booking link) stay visibly marked with `tbd` until replaced.
10. Copy about the ceremony comes from the organisers' own text. Don't invent promises, effects or bios.
11. Design decisions are made in Claude chat and recorded in the design system or a prototype. When building (Claude Code), never decide design: if something isn't defined, stop and ask with two or three options.

## Components (class names)
- Layout: `container`, `section`, `section--surface`, `section--inverse`, `section--tight`, `section-head`, `grid grid--2|grid--3`, `split`, `stack`
- Type: `display`, `h1`, `h2`, `h3`, `lead`, `body`, `small`, `eyebrow`, `measure`
- Actions: `btn btn--primary`, `btn btn--secondary`, `btn-row`, `link`
- Blocks: `nav`, `hero` (with warm glow), `hero__meta`, `page-hero`, `card`, `card__icon`, `steps` / `step`, `price` / `price--featured`, `badge`, `list`, `quote`, `faq`, `cta`, `footer`
- Event: `facts` / `facts__row` (event details as a `<dl>`), `tbd` (visible placeholder)
- Forms: `form`, `form__row`, `field`, `label`, `input`, `field__error`
- Nav toggle labels: `data-label-open="Меню" data-label-close="Закрыть"`

## Page patterns
- Event landing (`prototypes/home.html`): hero (eyebrow, display title, lead, two buttons, meta: date · city · format), what awaits (3 cards), the alchemy (steps), details (split: head + facts), closing CTA (inverse)
- Pricing, about, contact: as in the Signal starter, when needed

## Before you deliver
- [ ] Only tokens and existing components used
- [ ] Phone, tablet and desktop checked; no horizontal scroll
- [ ] One h1, one primary button per view, one inverse section
- [ ] Contrast and form errors checked
- [ ] Cyrillic renders in all three fonts
- [ ] Placeholders replaced or clearly marked with `tbd`
- [ ] Impressum and Datenschutz linked before the page goes live in Germany

## Keeping this skill current
When a decision changes the system (a new token, a new component, a new rule), update this file in the same change. Claude chat should suggest it: "This should go into the design skill."
