# Cacao · design system

Design system and page designs for **«Алхимия сердца»**, a cacao, sound healing and inner work ceremony in Berlin (29 November, 15:00–18:00).

Built on the **Signal** starter from [hoomanab01/web-style-guide](https://github.com/hoomanab01/web-style-guide): same file structure, token names and components, restyled after the event poster.

## What's in here
| File | What it is |
|---|---|
| `storybook.html` | Every colour, type size and component on one page. Open it first. |
| `prototypes/home.html` | The event landing page, built only from the system |
| `assets/tokens.css` | All values: colours, fonts, sizes, radii, motion |
| `assets/components.css` | All components, built from tokens only |
| `assets/site.js` | Mobile menu and reveal-on-scroll. No dependencies. |
| `assets/motion.js` | Lenis smooth scroll and the Vanta fog in the hero |
| `assets/vendor/` | Lenis, three.js (r134) and Vanta fog, self-hosted (MIT licences included) |
| `SKILL.md` | The design rules, written for Claude |
| `CLAUDE.md` | The context file. Point every new chat or Claude Code session at it. |
| `netlify.toml` | Publishes the folder as it is; `/` shows the landing page |

## What changed from Signal
The look now follows the event poster.

| | Signal | Cacao |
|---|---|---|
| Background | `#0B0D10` graphite | `#120A07` night cacao, amber candle glow |
| Text | cool white | cream `#F1E3CF` |
| Accent | lime `#C8F135` | poster gold `#DDB47C` |
| Display | Space Grotesk (no Cyrillic) | Playfair Display, normal case (Latin + Cyrillic) |
| Body / labels | Inter / JetBrains Mono | Inter; labels in spaced capitals |
| Hero | flat | full-bleed photo of ritual cacao in a gold frame |
| Names | | Marck Script |
| Ornament | | gold divider with a four-point star; star brand mark |
| Closing section | lime | ember room with candle glow |
| New components | | `subtitle`, `script`, `divider`, `icon-ring`, `hosts`, `poster`, `facts`, `tbd`, centred hero/heads |

## Preview
Open `prototypes/home.html` or `storybook.html` in a browser. No build step.

## Fonts
Self-hosted in `assets/fonts` (Latin + Cyrillic subsets, from Fontsource). All under the SIL Open Font License; licence files are included.
