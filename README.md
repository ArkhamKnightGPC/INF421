# INF421

Programming project from the course INF421: Design and Analysis of Algorithms at École Polytechnique. The [problem statement](problem_statement.pdf) is provided.

## Overview

In this project we consider the **pseudo-boolean optimization problem**. Let $n \in \mathbb{N}^*$ denote a positive integer and $V = \\{1, 2, ..., n \\} $. We shall consider functions $f : \\{0, 1 \\}^n \to \mathbb{R}$ in $n$ binary variables $x_1, x_2, ..., x_n$ representing subsets of $V$ (i.e. $x_i = 1$ if element $i$ is in the subset and $x_i = 0$ otherwise). Such functions are called *pseudo-boolean functions* or *set functions*.

Our goal is to compute $$x^* = \mathrm{arg opt}_{x \in \\{0, 1 \\}^n} f(x)$$ using the $(\mu + \lambda)$ evolutionary strategy. For further details, please check the [project report](report.pdf).

## Requirements

The project was implemented using the [Nim programming language](https://nim-lang.org/). In Linux, install using $$\texttt{sudo apt install nim}$$

A script is provided for compiling and running the unit tests.

## Useful resources

For further reading: [Andrew N. Sloss and Steven Gustafson; 2019 Evolutionary Algorithms Review](https://arxiv.org/pdf/1906.08870.pdf)