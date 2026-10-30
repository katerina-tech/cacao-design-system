# Cacao · design system

Design system and page designs for **«Алхимия сердца»**, an Inner Journey cacao and sound ceremony in Berlin (29 November).

Built on the **Signal** starter from [hoomanab01/web-style-guide](https://github.com/hoomanab01/web-style-guide): same file structure, token names and components, re-valued for cacao. Warm, deep and bold instead of technical.

## What's in here
| File | What it is |
|---|---|
| `storybook.html` | Every colour, type size and component on one page. Open it first. |
| `prototypes/home.html` | The event landing page, built only from the system |
| `assets/tokens.css` | All values: colours, fonts, sizes, radii, motion |
| `assets/components.css` | All components, built from tokens only |
| `assets/site.js` | Mobile menu and reveal-on-scroll. No dependencies. |
| `SKILL.md` | The design rules, written for Claude |
| `CLAUDE.md` | The context file. Point every new chat or Claude Code session at it. |
| `netlify.toml` | Publishes the folder as it is; `/` shows the landing page |

## What changed from Signal
| | Signal | Cacao |
|---|---|---|
| Background | `#0B0D10` graphite | `#140D0A` roasted cacao |
| Text | cool white | cream `#F2E6DA` |
| Accent | lime `#C8F135` | heart gold `#E7B07A` |
| Display font | Space Grotesk (no Cyrillic) | Unbounded (Latin + Cyrillic) |
| Body / labels | Inter / JetBrains Mono, Latin only | same fonts, Latin + Cyrillic |
| Labels | mono, sentence case | mono, uppercase, spaced |
| Shape | 10–14px corners | pill buttons, 20px cards, round marks |
| Hero | flat | warm terracotta glow (`--gradient-hero`) |
| New components | | `facts` (event details), `tbd` (visible placeholder) |

## Preview
Open `prototypes/home.html` or `storybook.html` in a browser. No build step.

## Fonts
Self-hosted in `assets/fonts` (Latin + Cyrillic subsets, from Fontsource). All under the SIL Open Font License; licence files are included.
