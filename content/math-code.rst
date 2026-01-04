############################################
Writing math code isn't like writing a paper
############################################

:title: Writing math code isn't like writing a paper
:tags: math, coding, research
:category: Thoughts
:summary: Fighting words: Variable names in code shouldn't match variable
    names in the manuscript
:date: 2025-09-22

.. epigraph::

    Many things have not been named

    -- Susan Sontag, Notes on Camp

My goal with pysindy is to support the research field.
It's not just about translating a paper into a runnable algorithm,
but about maintaining the correctness and ability to innovate.
I've had several years of reviewing pull requests and reading code
for a variety of papers that into different areas of math.
I've had to read and understand things closesly in order to ward off and catch
subtle math errors when accepting or refactoring code.
I've learned some math from reading code, rather than paper,
and that means I've learned a thing or two about how to communicate
math via code.

In this post, I'll defend a controversial point,
but which hopefully gets people to reconsider how they name variables:

**Variable names in code shouldn't match variable names in the
associated manuscript**

That's right.  I'm tired of seeing code that looks like

.. code::

    loss += jnp.sqrt(N) /(2 * sigma ** 2) * jnp.sum(jnp.square(x_hat - x))

That's how most people write the math code for papers.
Instead, I'd like to see variable names that reflect the name in the text
of the paper, rather than the symbol in the equations.

.. code::

    pred_error = x_hat_prediction - x_true_state
    meas_loss = jnp.sqrt(n_colloc) /(2 * meas_var) * jnp.sum(jnp.square(pred_error))
    loss += meas_loss


Let's consider with me the different roles and constraints on variables in a
manuscript versus those in a software library.
I'll dwell on each point after the table.

Different considerations for variable names in math manuscripts and in code
================================================================================

    =========================     ===================================
    Manuscript                    Code
    =========================     ===================================
    Single namespace              Namespaces are a honking great idea
    Manuscripts are trees         Code is a directed graph
    Brevity counts more           Readability counts more
    Most text is text             Most text is code
    Statements without proof      Everything has an implementation
    Self-contained                Just one piece of an ecosystem
    Greek letters allowed         Keep it as ascii as possible
    Published once                Editable forever
    Few references have links     IDEs let you follow references
    =========================     ===================================

Namespaces
----------------
A manuscript needs to share a single namespace.
It's wildly confusing when a paper switches notation in the middle.
Manuscripts aren't exactly atomic, meant to be digested whole,
but they are expected to be able to be digested by any subset of their lines.
E.g. read the abstract, skip the intro, focus on one part of the method,
scan experiments to find where that part is tested, jump to conclusion.
So name changes are jarring, and there's a certain economy to the namespace.
More symbols added for convenience increase the chance that a human reader
skipped the definition and will need to backtrack.

By comparison, code is based around nested scopes, and names only matter
in their immediate context.
This means that a portion of a theorem can use different names
than the rest of the theorem.
That sounds crazy at first, but think about calculating when a frictionless
projectile will strike the ground.
Let this be one component of a larger problem.
The problem, posed in terms of acceleration, velocity, position, and time,
is

.. code:: python

    t_f = (-1 * v_i + np.sqrt(v_i ** 2 + 4 * g * x_0)) / 2
 
That's all well and good, but consider the alternative

.. code:: python

    def quadratic_root(a: float, b: float, c:float) -> tuple[complex, complex]:
        """Calculate the roots of a quadratic equation

        Args:
            a: the quadratic coefficient
            b: the linear coefficient
            c: the constant coefficient

        Returns both roots as a tuple of complex numbers.  Roots are ordered
            from smallest to largest real component, then smallest to largest
            imaginary component.
        """
        discriminant = np.sqrt(complex(b**2 - 4 * a * c))
        return (-b - discriminant) / 2, (-b + discriminant) / 2

    t_f = quadratic_roots(a=-g/2, b=v_i, c=x_0)[1]

Here, we've changed the names of the variables.
We have access to scoped variable names, and inside the quadratic formula,
it's easier to talk about coefficients of a quadratic function.
(It's much easier to reason about tests of the relevant code, too.)
The significant mental stretch at this point in the code is to convince
yourself that an object in freefall experiences a constant downwards acceleration,
and that if we start above ground, we're looking for when it hits the ground in the future.
If we didn't want to think through ordering of cases with complex numbers,
we could of course just add caveats or guard code in case ``a * c > 0``

By comparison, you couldn't do this in a paper.
If this were merely a component in a larger expression, you *might* reference
the quadratic formula, leaving the reader to piece together the derivation.
Most of your readers may can do.
But it keeps your manuscript focused on a narrower class of reader than
could otherwise benefit.

Document Graph
----------------
A manuscript is a document, and documents tend to be thought of as ordered
trees.
Section 1 comes before section 2, subsection 1.1 lives inside section 1 and
comes before subsection 1.2, etc, and forward references are rare
(except in the last paragraph of the introduction).
This means, at any point in the document, a reader has a sense of global
context.
It's possible to depend upon symbol declarations at any point beforehand
in the paper.
In our mental model and in a pdf, the tree readily flattens, and symbols are
never tied down to just the location they're defined.

By comparison, code is a (potentially-cyclic) directed graph.
There may be entry points for thinking about code,
e.g. the public symbols a library exports, or registered console scripts,
but when reading some method or function,
your mind sits in the same stack frame as the code you're reading.


Brevity vs Readability
--------------------------------
Readability matters in academic work too, but journals have page limits.
An author's goal is to explain, but there's not enough room to explain
to everyone.
If enough people will understand a derivation without intermediate steps,
they don't get included, as they would in a lecture to more junior students.
On the other hand, the size of code doesn't matter at all.
There is a real opportunity to use code to teach where the manuscript
has to make compromises in it's target audience.

Another place where readability matters is search.
Searching for one or two-letter symbols with editor or browser tools is
impossible (also a problem with searching through PDFs).
E.g. a search for the symmetric component of a matrix, :math:`A^S`,
will find as many entries as there are docstrings with the word "as".
It's worst for indexes and cardinality:
Variables like :math:`N`, :math:`P`, :math:`M`, :math:`K` are probably defined
once in a paper,
but understanding what they mean in code requires searching through a paper.
That task might take a couple minutes, but spending an extra couple minutes
looking away from the thing you're trying to understand comes with a cognitive
cost.

Text language
----------------
Most of the length of a manuscript is in natural language.
Equations include a description, and some even include a derivation or proof.
Docstrings and comments can serve a similar purpose, but consider the following
two apothegmata:

    Code that is well written is self-documenting.
    Code that is well written makes it easy to see mistakes

Using longer variable names that reflect the text of the paper makes it more
likely that an equation takes up more than one line.
This is a good thing.
It forces the author to name the intermediate quantities in the equation,
which, at worst, helps a reader's mental model of what's going on
mathematically, and at best, includes a derivation of the equation.

Let's look at one of the many devilish examples I've seen in pysindy:

.. code::python
    def _linear_weights(x: Float1D, d: int, p: int):
        """
        One-dimensioal weights for integration against the dth derivative
        of the polynomial test function (1-x**2)**p. This is derived
        assuming the function to integrate is linear between grid points:
        f(x)=f_i+(x-x_i)/(x_{i+1}-x_i)*(f_{i+1}-f_i)
        so that f(x)*dphi(x) is a piecewise polynomial.
        The piecewise components are computed analytically, and the integral is
        expressed as a dot product of weights against the f_i.
        """
        ws = _phi_int(x, d, p)
        zs = _xphi_int(x, d, p)
        return np.concatenate(
            [
                [
                    x[1] / (x[1] - x[0]) * (ws[1] - ws[0])
                    - 1 / (x[1] - x[0]) * (zs[1] - zs[0])
                ],
                x[2:] / (x[2:] - x[1:-1]) * (ws[2:] - ws[1:-1])
                - x[:-2] / (x[1:-1] - x[:-2]) * (ws[1:-1] - ws[:-2])
                + 1 / (x[1:-1] - x[:-2]) * (zs[1:-1] - zs[:-2])
                - 1 / (x[2:] - x[1:-1]) * (zs[2:] - zs[1:-1]),
                [
                    -x[-2] / (x[-1] - x[-2]) * (ws[-1] - ws[-2])
                    + 1 / (x[-1] - x[-2]) * (zs[-1] - zs[-2])
                ],
            ]
        )


T

.. example: nesterov's acceleration

Statment vs Implementation
-------------------------------
.. LEAN project

The document in an ecosystem
-------------------------------
.. Concrete links vs convention

Unicode ಠ_ಠ
----------------

Don't use greek letters in code.
Even if your language and editor allows it, do all your IDE plugins support it?
Do all the potential pre-commit hooks and linters support it?


Legacy and longevity
----------------------
Take this code that finds the symmetric part of a matrix:

.. code::

    (J + J.T) / 2

Symmetric parts of matrices play a role in many different fields.
They're a bit part of the trapping theorem of SC

In lieu of refactoring the code into components where its possible
to reason about tests,
or at least read and verify correctness,
the best way to prevent errors is to derive things on pen and paper,
then verify you've copied what's on the paper correctly into the code.


What instead?
===========================
Let's return to the first example:

.. code::

    np.sqrt(N) /(2 sigma ** 2) * jnp.sum(jnp.square(x_hat - x))

I don't necessarily know that lambda is a regularization weight until it gets consumed
and even then I potentially have to recognize the form of the equation to know that its
a regularization weight.  I probably know that sigma is a variance

.. code::

    reg_weight = np.sqrt(n_observations) /(2 * variance)




The moral of the story
============================
Math code as lab infrastructure

Longer names force you to explain intermediate quantities in equations
.. example: Woodbury matrix magic

Description closer to implementation


The hook:
===============
Next up: how to achieve readability and clarity on array axes and shape conventions!