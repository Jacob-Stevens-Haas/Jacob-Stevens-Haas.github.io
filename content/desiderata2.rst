############################################
More than just reproducibility
############################################

:title: Experimental Desiderata 2
:tags: mitosis, experiments, research
:category: Blog
:summary: What experiments should have
:date: 2025-05-29 12:06


So we know we need a tool to help our experiments.
This begins by asking what we demand from our experiments.
But any tool only exists in a workflow;
some of our demands will be met by a technical solution,
others will need to be met convention and skill.


At least reproducibility
---------------------------------
We know that experiments need to be reproducible.
If I'm reading a paper, I'd like to be able to recreate the experiments and see the same results.
In the world of software, **reproducibility** typically refers to the evironment,
a set of operating-system variables and dependency versions.
Given that software has users, it also implies a relatively simple invocation, e.g.
"run all cells" or "copy and paste on command line".
After all, as a `witty guide to technical project management`_ emphasizes,
“If the process takes any more than one step, it is prone to errors.”
Beware, however, nuance: not everything about the environment matters.
To wit:

* Which GPU your experiment ran on
* The folder in which you saved the output
* Whether you plotted intermediate figures.

So reproducibility is both a matter of *record-keeping* and *judicious choices*.
A technical solution can manage the former.
The latter relies on humans, but a technical solution must provide for useful convention.
That is to say, a user's choice of which environmental parameters don't matter
should be easy for a human to write, read, and spot errors.

.. _witty guide to technical project management: https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/

The n-trick pony
---------------------------------------
If I can reproduce your experiment, I can believe the results you present.
If I can run your experiment on different data, different parameters, or a different method,
I can believe the conclusions you draw.
As with reproducibility, **reusability** is a matter of both technical solutions and conventions.
This hints at the challenges of defining a notebook as an experiment.
While there are tools that can parametrize notebook runs (e.g. papermill),
they don't do well with passing arbitrary objects as parameters.
On the other hand, the problem of a parametrized procedure is obviously solved by importable functions.
This does mean that the experiment can't run itself - it is a library item,
and some sort of experiment-running application is needed.
In an ideal world, the experiment would not depend upon the experiment runner (again, the distinction for later).

Writing reusable experiments largely comes down to choosing to expose the parameters of interest
and methods of comparison/metrics.
In lieu of a formal hypothesis for an investigation
(which I argue isn't part of the experiment, but rather the investigation, but more on that distinction later),
spcifying the metrics that matter and the parameters of interest goes a long way to
achieving Francis Bacon's desired rubric.


Show *and* tell
-------------------------------------
We're not just running experiments; we're talking, and ideally writing about them.
That means that experiments and parameters need to be **describable**.
If an experiment accepts a simulation noise parameter, then we might want to talk
conversationally about the high-noise case, a low-noise but correlated case, and a heavy-tailed case.
Parameters have a name and a type such as ``float``, ``statsmodels.frozendistribution``, etc.
To talk about experiments, however, arguments or groups of arguments should have names. 

To jump to the point - a vernacular translation requires a dictionary.
That dictionary must serve as a single source of truth against which an experiment is checked,
so that all collaborators discussing the "low noise" case mean the same thing.
There are different ways of achieving this, but they largely come down to
whether you allow experimental parameters to be arbitrary code objects or restrict them
to primitive types.

Regardless of technical solutions, these definitions should all occur in the same location
in a mostly declarative syntax.
Adding a single named parameterization to a repository is a one-line diff,
as compared with changing and rerunning a jupyter notebook.


Sic parvis magna
-----------------------------------
The final desiderata I've identified is **composability**.
An investigation may include a data preprocessing step, which results in its own metric
for comparison, followed by a modeling/prediction step.
Both steps may have their own metrics, and the best first-step on its own metric
may not be the best in the composite method.
A case in point is pysindy: (also differentiation/optimizer)
Composability refers to the use of the experiment in some type of series.
Methods like pysindy are often used not only for scientific discovery, but also in engineering
systems like `SINDy-RL`_. Therefore, providing the option of composing the experiment's processing
with evaluation of a latter step helps make the experiment more useful to researchers. Similar to reusability, the definition of an experiment as a callable makes it composable as well.
Since experiments in mitosis do not need to depend upon mitosis, the avoid any additional
obstacles to reusability due to dependencies.

.. _SINDy-RL: https://github.com/nzolman/sindy-rl


Final thoughts
-------------------------
This list of four is by no means exhaustive.
There may be more qualities of excellent experiments that we can distill.
What do you think?  Can you send me examples of great experiments?