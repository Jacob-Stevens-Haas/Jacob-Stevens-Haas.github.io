############################################
More than just reproducibility
############################################

:title: Experimental Thoughts 2: Desiderata
:tags: mitosis, experiments, research
:category: Thoughts
:summary: What can we ask of experiments in an ideal world?
:date: 2025-02-05


In the `last article`_, my paper had been rejected
for unconvincing experiments, and I looked at Francis Bacon's *Novum Organon*
for suggestions.
To summarize his magnum opus with a recklessness bordering on abuse,
he told us we need to develop *mechanical aid*, which I interpreted as
a combination of software and technical convention.

This article is about what makes an experiment convincing,
with the aim to building software that facilitates such desiderata.

.. _last article: experimental-thoughts-1-trials-and-tribulations.html

At least reproducibility
---------------------------------
If I'm reading a paper, I'd like to be able to recreate the experiments
and see the same results.
In the world of software, **reproducibility** typically refers to the
evironment,
a set of operating-system variables and dependency versions.
Given that software has users, the goal of reproducibility also implies
a relatively simple invocation, e.g.
"run all cells" or "copy and paste on command line".
After all, as a `witty guide to technical project management`_ emphasizes,
“If the process takes any more than one step, it is prone to errors.”
Beware, however, nuance: not everything about the environment matters.
To wit:

* Which GPU your experiment ran on
* The folder in which you saved the output
* Whether you plotted intermediate figures.

So reproducibility is both a matter of *record-keeping* and
*judicious choices*.
A technical solution can manage the former,
The latter relies on humans,
but a technical solution must allow for useful convention.
That is to say, a user's choice of which environmental parameters don't matter
should be easy for a human to write, read, and spot errors.

.. _witty guide to technical project management: https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/

The n-trick pony
---------------------------------------
If I can reproduce your experiment, I can believe the results you present.
If I can run your experiment on different data, different parameters,
or a different method,
I can believe the conclusions you draw.
As with reproducibility, **reusability** is a matter of
both technical solutions and conventions.

This hints at the challenges of defining a notebook as an experiment.
While there are tools that can parametrize notebook runs (e.g. papermill),
they don't do well with passing arbitrary objects as parameters.
(Disclaimer: I haven't looked into papermill in the last year or so.)
On the other hand, the problem of a parametrized routine
is so obviously solved by functions.
Using functions, however, means that the experiment can't run itself
- it is a library item,
and some sort of experiment-runner is needed.

Metrics also matter.
It helps to provide enough metrics for researchers to understand
what's going on inside your model as well as summary scores.

So writing reusable experiments comes down to choosing
which parameters to expose
and what values to return.


Show *and* tell
-------------------------------------
We're not just running experiments; we're talking,
and ideally writing about them.
That means that experiments and parameters need to be **describable**.
If an experiment accepts a simulation noise parameter,
then we might want to talk conversationally about
a high-noise case, a low-but-correlated-noise case, and a heavy-tailed case.
Parameters have a name and a type such as
``float``, ``statsmodels.frozendistribution``, etc.
I contend that to talk about experiments, however,
arguments or groups of arguments need names.

To jump to the point - a vernacular translation requires a dictionary.
That dictionary must serve as a single source of truth
against which one can check each invocation of an experiment,
so that all collaborators discussing the "low noise" case mean the same thing.
There are different ways of achieving this, but they largely come down to
whether allow experimental parameters are allowed to be arbitrary code objects
or restrict them to primitive types.

Regardless of technical solutions,
these definitions should all occur in the same location
in a mostly declarative syntax.
The technical solution for checking object equality across runs
can be challenging,
and decisions there will affect the API one can design.


Sic parvis magna
-----------------------------------
The final desiderata I've identified is **composability**.
Composability refers to the use of the experiment in some type of series.
A case in point is `pysindy <https://github.com/pypi/projects/pysindy>`_,
which traditionally begins with a derivative estimation step.
This step itself can be evaluated for `accuracy and bias`_.
But the choice of parameters that optimizes those objectives
may not be the same as the choice which then leads to
the best equation discovery
(there are several different metrics for that, too).
Finally, methods like pysindy are often used not only for scientific discovery,
but also in engineering systems like `SINDy-RL`_.
Therefore, providing the option of composing the experiment's processing
with evaluation of a latter step helps make the experiment more useful to
researchers.

.. _accuracy and bias: https://ieeexplore.ieee.org/document/9241009
.. _SINDy-RL: https://github.com/nzolman/sindy-rl

Similar to reusability, the definition of an experiment as a callable
makes it composable.
However, for the callable to be useful in an experiment runner,
there needs to be a convention that separates the relevant metrics
from processed data.

Final thoughts
-------------------------
This list of four is by no means exhaustive.
There may be more qualities of excellent experiments that we can distill.
What do you think?  Do you have any examples of great experiments?
In the final article of this series, I share my thoughts on the tool I wrote
to fulfill these desiderata.
