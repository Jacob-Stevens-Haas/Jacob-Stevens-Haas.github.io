############################################
Problems with my experiments
############################################

:title: Experimental Thoughts 1: Trials (and tribulations)
:tags: mitosis, experiments, research, glider
:category: Experiments
:summary: Struggles with experiments in data science and mathematics and a discussion of what they lack.
:date: 2025-05-29 12:06


A song as old as time
---------------------------------

I had a problem when I started my first PhD project.
I wanted to demonstrate the value of Kalman smoothing in improving
ocean glider navigation and current estimation.
These things are pretty cool: with their buoyancy engine
and Acoustic Doppler Current Profiler (ADCP),
they can operate autonomously for weeks,
at a pithy "half a knot on half a watt",
They take GPS fixes at the surface
and bounce doppler sonar off of plankton when submerged.
However, that doppler velocity is a relative measurement
of the vehicle's true velocity
minus current (since plankton are stationary in the water column).

..  image:: seaglider.png
    :width: 400
    :alt: A ocean glider.

Previous methods used a smoother that,
(a) assumed acceleration was instant
and (b) assumed true velocity was independent of current.
The first makes some sense, given the scale of the measurements.
The latter is a harder sell,
but could be justified if vehicle velocity was much larger than current velocity.
The assumptions weren't justified in the literature;
they were mathematical assumptions that would yield the existing method
as a maximum likelihood estimator.
That existing method did not make much use of probability language.
In reformulating a probabilistic approach that eschewed the assumptions,
I would also have to justify treating unknown quantities as random variables.
This is obvious to any Bayesian
(and indeed, a definition of what it means to be Bayesian),
but oceanographers questioned it nonetheless

I derived the maximum likelihood estimator for two stochastic processes,
and showed how certain unneccessary (and bad) assumptions gave rise
to the current method.
On the other hand, it was possible to derive a similar estimator
without those assumptions.
But it's only natural that reviewers from an applied field would (and did)
want more than math, even if the math was correct.

I needed experiments.

Empricism requires admin
--------------------------------

I would frequently get some good-looking results early in the week,
only to run into errors or different results right before my friday meetings
with my advisor and the project PI from the Applied Physics Lab (APL).
My experiments, built originally as jupyter notebooks and later scripts,
had a ton of parameters from the outset.
Without access to a research ship and months to collect data,
I was using simulated data,
which meant even more parameters.

Moreover, I was developing the method as I was building the experiments.
How could I know if a new result was due to a bugfix I had made during the week,
or a different parameter set?
Or had I introduced another bug?
So I began recording all of this.

..  image:: seaglider-record.png
    :width: 500
    :alt: A table of all the nonsense I tried to manually record.


Math has become an experimental field.
---------------------------------------
Methods papers propose a mathematically informed approach to problems
and publish tables and figures to convince the reader that the method is,
in fact,
good at a class of related problems.
These tables and figures often come from jupyter notebooks or scripts,
or more exotically, from an experiment runner like `sacred <https://github.com/IDSIA/sacred/>`_
or `mitosis <https://mitosis.readthedocs.io/en/latest/>`_
(disclaimer: I am the author of mitosis).
But unlike so many other experimental fields,
math and data science don't have much in the way of formal protocols.
That we can get away with this is probably due to the cost of running experiments
Grad student hours are free, but `experimental apparati aren't <https://www.science.org/content/blog-post/how-not-do-it-ruining-stuff>`_.


..  epigraph::

    The natural and spontaneous action of the mind is suspect...
    our only remaining hope and salvation is to begin...
    using mechanical aid

    -- Francis Bacon, Novum Organon

I have worked on about a half-dozen long-term projects between my PhD and
data science consulting.
I contend that the conclusions drawn in nearly all
exceeded where honest skepticism would draw a line.
As Francis Bacon tells us in *Novum Organon*, the canonical description
of scientific method:
we cannot both freely investigate and draw responsible conclusions.
His solution was to use a rubric.
He applied the rubric to the phenomenon of heat, e.g.
Consider things associated with heat
(friction, humidity, fire, gas expansion, ice melting)
and consider which can occur without heat?  Can heat occur without some of those things?
What does that tell us about the true nature of heat?

The idea of a gestalt rubric for investigating anything was suitable for his
time.  Let me propose a more mundane version of mechanical aid in the next article.