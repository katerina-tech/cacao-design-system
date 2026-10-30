# Context

Read this first in every new chat or Claude Code session.

## What we're building
A small website for **«Алхимия сердца» (The Alchemy of the Heart)**, an Inner Journey cacao and sound ceremony in Berlin on 29 November. Led by Светлана Делле (Света-Яра), with sound healing by Анастасия and Оксана. Audience: Russian-speaking people in Berlin. The page invites them and gets them to sign up.

## Our Git
- Design system: github.com/katerina-tech/cacao-design-system
  Tokens (`assets/tokens.css`), components (`assets/components.css`), the storybook (`storybook.html`), the design skill (`SKILL.md`), and page designs in `prototypes/`.
- Website: github.com/katerina-tech/cacao-website (to be created)
  The pages Claude Code builds. `main` is the live site, `staging` is the rehearsal, every change goes through a pull request.
- The design system repository is the source of truth. The website only uses what is in it.

## Stack
Plain HTML, CSS and a little JavaScript. No build step. Hosted on Netlify. Fonts self-hosted (Latin + Cyrillic), no requests to Google.

## Pages
`prototypes/home.html`: the event landing page (one page, in-page anchors).

## How we work: the loop
1. Design in Claude chat: prototype the page, try versions, check phone and desktop.
2. Update the design system: anything reused or a rule goes into tokens, components, storybook and SKILL.md. The page goes into `prototypes/`.
3. Push the design system repository to GitHub.
4. Claude Code, in the website repository: get the latest design system, update tokens and components to match, build the page from its prototype, on a new branch.
5. Test on localhost: phone and desktop, every link, Lighthouse. Not OK? The report goes back to Claude chat.
6. Pull request, check the Netlify preview link, merge. The site goes live.

## Rules for Claude Code
- Never make a design decision. Colours, fonts, spacing, layout, copy, motion and imagery are decided in Claude chat and live in the design system or the prototype.
- If something isn't defined there, stop and ask. Offer two or three options with a short reason for each. Don't pick one yourself.
- Use only tokens from `assets/tokens.css` and components from `assets/components.css`. Never hard-code a value.
- Work on a branch, never directly on `main`.
- After building, run the site locally, test phone and desktop, and report what you built, what you tested and every open question, before opening a pull request.

## Current state
- Done: Cacao design system (from the Signal starter), storybook, landing page prototype in Russian.
- Open (marked `tbd` on the page): start time, address, price, booking link. Impressum and Datenschutz pages before going live.
- Next: fill the open details, create `cacao-website`, build from `prototypes/home.html`.
