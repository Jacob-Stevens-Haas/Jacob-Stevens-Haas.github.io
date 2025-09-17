############################################
Separation of Concerns in Research
############################################

:title: Separation of Concerns in Research
:tags: mitosis, experiments, research
:category: Thoughts
:summary: Method != experiment != experiment runner
:date: 2024-06-08

The most important lesson I've learned in research engineering practice is
separating the method and experiment API.

Slow is smooth, smooth is fast
=================================

Some research provides an API to the method/intervention, but rarely to the
experiments.
In practice, people tend to manually run experiments in notebooks or scripts,
without providing a user or reader any intentional API.

Let's disambiguate.  The method is what someone uses on their data.
The experiment is what they use to prove that the method works.  In an ideal
world, two methods compete directly, and you can simply swap them out in the
same experiment.  As long as the experiment is well posed, it's easy to see
which method is better
(I'll talk about experimental desiderata in a later post).

In pseudocode, the work of an experiment could look like:

.. code::

    data = experiment.load_or_generate_data()
    predictions_1 = method_1(data)
    predictions_2 = method_2(data)
    evaluation_1 = experiment.evaluate(predictions_1)
    evaluation_2 = experiment.evaluate(predictions_2)

The point to take away is that an experiment should have an API,
and if the API enforces the scientific method,
it becomes infrastructure for rapid iteration in research.
Often people discuss rapid innovation as a sort of shoestring approach,
via jupyter notebooks.
To me, that isn't convincing.
At best, it provides initial results that are hard to scale to meaningful ones.
What is convincing is being able to reuse and interrogate an experiment.

But there's one more bunch of code that ought to be separated - the experiment
runner.

Experiment runner
===================

See, when I was working on my first project as a PhD student, I'd get some
results on a Tuesday to present to my advisor on Friday.
In the interim,
I would fix a bug, try out some different parameterizations, etc.
Come Friday, I couldn't quite reproduce the results the same as I had earlier.
I became anxious - how much had I actually learned from running the code
beforehand?  If I couldn't convince my advisor, I couldn't convince myself.

I more manual experiments, scientists record experimental protocols in a lab
notebook.
Diligence comes with a cost, but so does running the experiment.
Grad student hours are cheap.
`Experimental apparati can be expensive <https://www.science.org/content/blog-post/how-not-do-it-ruining-stuff>`_.
On the other hand, if I discover a mistake in a jupyter notebook
it costs nothing to fix the mistake, change another parameter, and rerun it.
Research admin would take a relatively larger amount of time,
so it isn't done.

I contest that with only a small amount of rigor in coding math experiments,
we can use an experiment runner to provide the rest of the helpful admin.
That admin, just like for physical experiments has a real benefit:
It makes it easier to determine which results should be trusted.

I'm going to segue into a series on why I built an experiment runner,
`mitosis <https://pypi.org/pyrojects/mitosis>`_,
a python package for running and administering experiments,
how it fits into a workflow,
and what benefits such an experiment workflow provides.

