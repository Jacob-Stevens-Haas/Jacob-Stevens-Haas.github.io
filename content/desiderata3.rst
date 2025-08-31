#################################################
Mitosis: Making reproduction (and the rest) easy.
#################################################

:title: Experimental Thoughts 3: Technical Implementation
:tags: mitosis, experiments, research
:category: Experiments
:summary: How I built a tool to fulfill the experimental desiderata.
:date: 2025-05-29 12:06



So we know we need a tool to help our experiments.
This begins by asking what we demand from our experiments.
But any tool only exists in a workflow;
some of our demands will be met by a technical solution,
others will need to be met convention and skill.

Let's collect thoughts
---------------------------------
To recap, we want experiments to be:

Reproducibile
   Ran in a separate process, from start to finish, with
   dependency list, environment variables, and git information automatically
   recorded.

Reusable
   Experiments are and importable ``Callable``, written with important factors
   exposed as parameters and metrics as return types.  Individual runs, or
   trials, result in artifacts separate from the experiment definition.

Describable
   A dictionary is used to name arguments or groups of arguments.
   This dictionary enforces a single source of truth, so that different trials
   using the same argument name must result in object equality.
   Should be a way to distinguish parameters that matter and those that don't.

Composable
   Some experiments should be thought of experiment steps, providing their
   data as well as intermediate metrics.
   The experiment runner needs to parse their output and forward the data to
   the correct parameter of the next step.

It is also worth exploring some challenges and opportunities.
The kinds of equality checks across processes in *reproducible* and
*describable* require some sort of serialization to disk, as well as either
deserialization or a correspondence between serialization equality and object
equality.
Secondly, multiple processes querying the disk will imply some sort of
distributed systems challenges.

Of smaller significance, we should note that we'll need to prepare the trial
output with graphics.
It also might be nice to have an experiment browser.
Finally, we'll note that running the experiment is likely the dominant cost;
loading parameters, etc.
In almost all cases, we'll consider the admin work of an experiment runner
as effectively free.

The experiment runner
--------------------------------
We have stripped several parts of what some consider an experiment into a
project-independent experiment runner, yet other project-specific parts,
like the argument definition dictionary, remain unhomed.

Project layout
^^^^^^^^^^^^^^^^^^^^^^^^^^^
At this point, let me share the project organization that works for me.

* A package with the method undre investigation.
* A package of experiments, exposed as a library of functions.
  Some methods are wrapped in local ``sklearn.BaseEstimator`` to support the
  dichotomoy of of data-independent initialization and data-dependent fitting.
* A project-independent runner (mitosis)
* An overall repository configured with what experiments to investigate,
  a dictionary of plain english names for arguments to investigate,
  a script file of all the experiments to run,
  and a directory for mitosis to write experiment artifacts.
  This is usually symlinked to a shared directory for multiple users
  and if necessary rsync'd with a cron job to other lab servers.
  It also sometimes has the LaTeX files for writing a paper,
  as well as a ``post`` package for generating final images for papers/talks
  from experiment records.

A graphical example is below:

.. figure:: images/research-project.png
    :alt: Organization of methods, experiments, investigation, and runner for research project.

    A depiction of the project organization for the plumes project.
    This consists of
    a package to process plume videos into various reduced-order models,
    a package to run experiments to evaluate different parameterizations
    of those reduced order models,
    a copy of ``mitosis``,
    and a project that represents the investigations in the paper and presentation,
    specifying the particular choices of parameters to investigate.
    This layout was used for several hundred invocations of experiments
    as we improved and debugged the experiments
    and identified the best parameterizations.

Since the investigation often evolves alongside the methods and experiments
I prefer to leave those as separate distribution packages but git submodules
within the overall investigation repository.
It also works to have method and experiments both part of the investigation
repository and distribution package, but as different import packages.
Regardless, this separation of concerns helps force decisions about what
choices are generally applicable and which are specific to the data in an
investigation.
Long term, this helps people further innovate the methods without stopping to
wonder why decisions were made that don't truly belong with the code they're
editing.

Lookup dictionary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The main reason to specifying the arguments of interest as a dictionary is
to give them human names, names that they would be called anyways,
which become standard among collaborators.
Otherwise, these parameters occur in a variety of default values and
spread throughout a notebooks definition.
However, an unintended benefit is how concise the the ``git diff`` of a
declarative syntax can be.

The diff becomes a form of communication, and tools that generate communication
from work products are a huge aid to collaboration.
To take a case in point, it's easy to see from the example below what my kinds
of experiments my colleague below was working on:

.. figure:: images/helpful-diff.png
   :alt: a git diff of a declarative argument definition file

   When experiments are factored well, its easy to see what parameters other
   people are investigating.


Dependency inversion 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The relationship between the experiment runner and experiments is the perfect
situation to use dependency inversion.
That is, in order for the runner to be project independent, it cannot depend
upon the experiments.
Yet to run experiments always through the same CLI means that the runner
must import and access those experiments.
At the same time, I don't want to make experiments import the runner;
I want them to be more portable than that.

I admit I fumble a bit pinning down dependency inversion, but this example is
the essence of it:
The existence of the higher level facility (runner) does not depend upon the
lower-level library, and the lower level library does not of course depend upon
the higher level runner. 

The Python facility for entry points is a good example of how this works.
Normally, the lower-level library has responsibility for registering the entry
point.
Our separation of concerns, however, puts that responsibility on the
investigation.
The investigation's pyproject.toml includes a ``tool.mitosis`` table for naming
different experiments and associating their lookup dictionaries.
This has the added benefit of allowing references to short names of experiments
but still disambiguating any name conflicts.  E.g. I can use experiments written
by other folks such as ``grad_project.utils.dmd_fit_eval`` and
``lab_utils.dmd.dmd_fit_eval``, but refer them locally as
``ryan_dmd``, and ``lab_dmd``.

OBTW: The use of ex.sh
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It's also useful to keep a file ``ex.sh`` in the investigation repository to
track the current "official" experiments.  This allows you to move experiments
to a new machine in case you get left off the email that the funding agency
is yoinking back those expensive GPU servers.