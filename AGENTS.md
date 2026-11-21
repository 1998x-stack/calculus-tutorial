# Agent instructions

This repository is a static Chinese calculus course. Follow the pedagogy and engineering discipline in [Olah-style-posts](https://github.com/1998x-stack/Olah-style-posts), especially its progressive narrative, evidence discipline, semantic HTML, native MathML, accessible SVG and browser QA. Borrow the workflow, not its paper/article wording or assets.

## Content architecture
- Keep the 28 chapter URLs stable: `01.html` through `28.html`.
- Keep the homepage static and usable without JavaScript; search/filter is progressive enhancement.
- Keep `courses.json` and the homepage catalog synchronized.
- Shared design tokens and legacy chapter compatibility live in `assets/css/calculus.css`; `theme.css` remains a compatibility import for chapters 09–28.
- Shared interactions live in `assets/js/calculus.js`. Do not add a framework or CDN for a small interaction.
- New interactive lessons must work with a meaningful static default before JavaScript runs.

## Mathematical correctness
1. State definitions with quantifiers and domain assumptions.
2. Distinguish intuition, theorem, proof, numerical experiment and worked example.
3. Check endpoint inclusion, one-sided limits, sign, units and radian assumptions.
4. Distinguish `o`, `O`, `Θ` and asymptotic equivalence; `O` alone does not mean same order.
5. Use equivalent infinitesimal substitutions only where algebraic structure preserves the limit; never discard cancellation in sums/differences.
6. For two-sided limits, explicitly compare left and right limits.
7. A numerical demo is an illustration, not a proof. State rounding and stopping criteria.
8. Cross-check nontrivial theorems and definitions against an established calculus text (OpenStax or MIT OCW).

## Formula and figure standards
- Use native MathML elements (`mfrac`, `msub`, `msup`, `munderover`, `mtable`) for substantial formulas.
- Every `math` element needs an accurate `aria-label`; long display formulas live inside a keyboard-focusable `[tabindex="0"]` scroll region.
- Never nest MathML inside SVG. SVG labels should remain short and use normal SVG text.
- Each SVG requires a `title`, `desc`, accessible labeling and a human-readable figcaption.
- Color is redundant with labels and line styles; keep meanings consistent within a lesson.
- Use native controls with visible labels, keyboard focus and `aria-live` status.

## Required checks

```bash
python scripts/validate_site.py
npm install
npx playwright install chromium
npm test
```

Review at 1440px, 768px, 390px and 360px. Check print emulation, MathML namespace/geometry, SVG clipping, no document-level horizontal overflow, browser console errors, and at least one meaningful interaction per updated chapter. Report checks not run as “not verified”; never convert skips into passes.

## Publishing
- GitHub Pages publishes the repository root; keep all assets on relative paths so the site works under the `/calculus-tutorial/` project prefix.
- Do not introduce root-absolute asset URLs such as `/assets/...`.
- Verify the latest Pages workflow after changes to `main`; do not claim the site is live until deployment and the public URL are checked.
- Keep chapters 09–28 accessible while refining chapters in batches.
