############################################
Separation of Concerns in Research
############################################

:title: Separation of Concerns in Research
:tags: mitosis, experiments, research
:category: Blog
:summary: Method != experiment != experiment runner
:date: 2024-06-08 12:06

The most important lesson I've learned in research engineering practice is
separating the method and experiment API.

Most research doesn't provide an API to either the method or the experiments.
In practice, many people manually run experiments in notebooks or scripts, without
providing a user or reader any intentional API.

Let's disambiguate.  The method is what someone uses on their data.
The experiment is what they use to prove that the method works.  In an ideal
world, two methods compete directly, and you can simply swap them out in the
same experiment.  As long as the experiment is well posed, it's easy to see
which method is better (I'll talk about experimental desiderata in a later post).

In pseudocode, it looks like:

.. code::

    data = experiment.load_or_generate_data()
    predictions_1 = method_1(data)
    predictions_2 = method_2(data)
    evaluation_1 = experiment.evaluate(predictions_1)
    evaluation_2 = experiment.evaluate(predictions_2)

One can imagine a hypothesizing which method performs better, reviewing the
evaluations, and deciding whether to accept the hypothesis.
Even when the experiment is imperfect, the scientific method provides
a framework for discussion.  But when the API also reflects the scientific method,
it becomes infrastructure for rapid iteration in research in a way that actually
convinces users - including yourself, the researcher.

But there's one more bunch of code that ought to be separated - the experiment
runner.

See, when I was working on my first project as a PhD student, I'd get some
results on a Tuesday to present to my advisor on Friday.  In the interim, I would
fix a bug, try out some different parameterizations, etc.  Come Friday, I couldn't
quite reproduce the results the same as I had earlier.  I became anxious - how
much had I actually learned from running the code beforehand?  If I couldn't
convince my advisor, I couldn't convince myself.

In non-mathematics research, the control and intervention methods and experiment
administration is often manual.  Data is collected in lab notebooks, and details
of the experiment are fastidiously recorded.  Lab members can review these
notebooks to recreate an experiment as exactly as possible.  That's necessary
when experiments are expensive.

Applied math experiments on commodity hardware are not expensive, so we run a lot
of them.  Manually adding rigor to quick, iterative experiments is too much overhead.
But with a small amount of rigor in coding the experiments, we can use an experiment
runner to provide the rest.  The benefit is that each experiment creates more
knowledge, or at least more confidence, in the result.

I wrote ``mitosis``, a python package for administering experiments.  That was
before I found out about ``sacred``, whose github lists some comparable other tools.

I've opened a few topics that I want to focus more specifically on in coming weeks:
details of the method API, desiderata for experiments, and the experiment runner.
