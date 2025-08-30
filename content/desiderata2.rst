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
I can reproduce your experiment, I can believe the results you present.
If I can run your experiment on different data, different parameters, or a different method,
I can believe the conclusions you draw.
As with reproducibility, **reusability** is a matter of both technical solutions and conventions.
This hints at the challenges of defining a notebook as an experiment.
While there are tools that can parametrize notebook runs (e.g. papermill),
they don't do well with passing arbitrary objects as parameters.
On the other hand, the problem of a defined but parametrized procedure is obviously functions.

Writing reusable experiments largely comes down to choosing to expose the parameters of interest
and methods of comparison/metrics.
In lieu of a formal hypothesis for an investigation
(which I argue isn't part of the experiment, but rather the investigation, but more on that distinction later),
spcifying the metrics that matter and the parameters of interest goes a long way to
achieving Francis Bacon's desired rubric.
Thus, reusability is more a question of practice than technological solution.
The only reservation to this is that, to be as reusable as possible,
it's nice for the experiment to not depend upon the experiment runner (again, the distinction for later).


Show *and* tell
-------------------------------------
**describable** 
refers to a vernacular for its parameterization and a single source of truth
for what that vernacular means.
Mitosis contributes this by diligently checking all named variants against a database,
with appropriate considerations for repeatable serialization.
The dictionary definition of vernacular is a semi-declarative syntax, as shown in figure 5.2. This figure shows value of a declarative
syntax: its simple to see what someone is experimenting on by reviewing the diff of named
parameterizations. 


Sic parvum magnus
-----------------------------------
**composable**.

Composability refers to the use of the experiment in some type of series.
Methods like pysindy are often used not only for scientific discovery, but also in engineering
systems like `SINDy-RL`_. Therefore, providing the option of composing the experiment's processing
with evaluation of a latter step helps make the experiment more useful to researchers. Similar to reusability, the definition of an experiment as a callable makes it composable as well.
Since experiments in mitosis do not need to depend upon mitosis, the avoid any additional
obstacles to reusability due to dependencies.

.. _SINDy-RL: https://github.com/nzolman/sindy-rl

.. figure:: images/research-project.png
    :alt: Organization of methods, experiments, investigation, and runner for research project.

    A depiction of the project organization for the plumes project.
    This consists of
    a package to process plume videos into various reduced-order models,
    a package to run experiments to evaluate different parameterizations
    of those reduced order models,
    a copy of \lstinline|mitosis|,
    and a project that represents the investigations in the paper and presentation,
    specifying the particular choices of parameters to investigate.
    This layout was used for several hundred invocations of experiments
    as we improved and debugged the experiments
    and identified the best parameterizations.
