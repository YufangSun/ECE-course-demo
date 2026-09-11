---
title: Galton Board
emoji: 🎲
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: 5.45.0
app_file: app.py
pinned: false
thingy_author: Yufang Sun
---

# Galton Board

Every peg is one Bernoulli trial. A ball goes right with probability `p`, and the
bin it lands in counts how many rights it took — so the pile that accumulates is
a Binomial(n, p) distribution, built out of physical coin flips.

- **Follow one ball.** Set the fall speed to *slow* (or press "Drop 1 ball") and a
  single ball falls on its own, trailing the route it took. The letters under the
  board are its left/right sequence, and its bin is just the number of R's.
- **The exact pmf is drawn before any ball falls** — the green steps are
  C(n,k)p^k(1−p)^(n−k). The blue bars climb to meet them, which is the law of
  large numbers acting on each bin's relative frequency.
- **The dashed orange curve is de Moivre–Laplace**, the central limit theorem's
  first historical special case: Binomial(n, p) ≈ N(np, np(1−p)). At 4 rows the
  fit is poor; at 20 it is excellent.
- **Skew the pegs.** At p = 0.1 the pile bunches against the wall and the normal
  approximation overhangs into impossible negative bins — the usual guidance is
  that np and n(1−p) should both exceed about 5.
- **Two convergences at once.** The lower-left panel plots the total variation
  distance between the measured histogram and the true pmf; it shrinks like
  1/√(balls), independently of how good the normal approximation is.

Built for ECE 302 (Probabilistic Methods in Electrical and Computer Engineering).
Part of a larger collection at https://yufangsun.github.io/ECE-course-demo/
