Categories: latex
Tags: markdown
      latex

## Overview

- Most error free way to insert latex with the built in wordpress latex plugin is to use the following format


        <p>$latex [your equation] $</p>

## Overbrace

- To insert text for an overbrace:

        \overbrace{p_11}^{overbrace text}

## Sum

- To insert a superscript above a `sum`:
  - Insert a sum (`\sum`)
  - Select the `\displaystyle`
  - Use `^` and `_` to insert text above and below the sum symbol (as you would with subscript/superscript variables).

## Aligned Equations

- The only environment that works with the built in wordpress latex environment is the `aligned` environment.
- Note the `eqnarray` and AMS environments DO NOT work.