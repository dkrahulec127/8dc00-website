.. 8DC00 documentation master file, created by
   sphinx-quickstart on Fri Aug  6 16:31:49 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to the Medical Image Analysis course (8DC00) !
======================================================

| *Course website*: https://github.com/tueimage/8dc00-mia
| *Course edition*: Fall 2021 (Sep. 1 - Dec. 20) - to be updated
| *Virtual reader*: https://8dc00-website.readthedocs.io/en/latest/
| *Course instructors*: Maureen van Eijnatten, Mitko Veta, Friso Heslinga
| *Documentation, notebooks*: Daniel Krahulec, Evi Huijben

This course is a sequel to the second year introductory imaging course. In that course the basic principles of image analysis were covered. 
In 8DC00 we will concentrate on the more advanced image analysis methods and on how they can be used to tackle clinical problems. 
Topics covered include image registration and computer-aided diagnosis (CAD).

Use of canvas
-------------

This GitHub page contains information about the course and the study material. 
The Canvas page of the course will be used only for sharing course information that cannot be made public (e.g. Microsoft Teams links), 
submission of the practical work and posting questions to the instructors and teaching assistants (in the Discussion section). 
Students are highly encouraged to use the Discussion section in Canvas for general questions (e.g., issues with programming environment, methodology questions).

TLDR: GitHub is for content, Canvas for communication and submission of assignments.


Hybrid schedule due to the coronavirus pandemic
-----------------------------------------------

The 2020 edition of the course will be given in a hybrid manner, combining on-campus and online education. We have a limited capacity of 52 student on Tuesdays and 32 students on Thursdays to attend the lectures on-campus. In order to attend the lectures on campus, you have to subscribe for that lecture in Canvas (details on Canvas). All lectures will also be streamed online via Microsoft Teams for the students that want to attend remotely. All practical sessions (guided self-study) will only be online.

The schedule is as follows:

- **Lectures**: Tuesdays 13:30 – 15:30 (location: Atlas 0.820 or via MS Teams) & Thursdays 10:45 – 12:45 (location: Atlas 6.225 or via MS Teams)
- **Guided self-study**: Tuesdays 15:30 - 17:30 & Thursdays 8:45 - 10:45 (via MS Teams)

Since the practical sessions are scheduled immediately before or after the lectures, if you attend the lectures on-campus you might not have sufficient time to travel home for the guided self-study. The University is working on ensuring that there are sufficient number of safe workspaces on-campus so that you can log in from there.

Feedback, Questions or Contributions
------------------------------------

This is the first time we present these notebooks during the Medical Image Analysis course. 
As with any other project, small bugs and issues are expected. 
We highly appreciate any feedback from students, whether it is about a spelling mistake, implementation bug, or suggestions for improvements/additions to the notebooks. 
Please use the following `link <https://docs.google.com/forms/d/e/1FAIpQLSeIhwrFSHlDSWGAgCN-RcTKm7Sn7P6bxzIyzIGge6xId1K8DQ/viewform?usp=sf_link>`_ 
to submit feedback, or feel free to reach out to me directly per mail (mitko dot veta at tue dot nl), or raise your hands during any TA session.

Assessment
----------

The assessment will be performed in the following way:

- Project work: 30% of the grade (both projects have equal contribution)
- Final exam: 70% of the grade

Grading of the assignments will be done per group, however, it is possible that individual students get a separate grade from the rest of the group (e.g. if they did not sufficiently participate in the work of the group). 
More info on the assessment criteria can be found `in this table <https://github.com/dkrahulec127/8dc00-website/blob/main/docs/source/data/rubric.md>`_.


Lecturers and teaching assistants
---------------------------------

**Course instructors:**

- Maureen van Eijnatten
- Mitko Veta

**Guest lecturers:**

- Cornel Zachiu (UMC Utrecht)
- Geert-Jan Rutten (Elisabeth-TweeSteden Ziekenhuis)

**Teaching assistants:**

- Friso Heslinga (PhD candidate)
- Leander van Eekelen (MSc student)
- Glenn Bouwman (MSc student)
- Stijn Bunk (MSc student)
- Luuk van de Hoek (MSc student)

Interactive notebooks
=====================

.. toctree::
   :caption: Software guide
   :maxdepth: 2

   reader/0.1_Help_for_Jupyter_and_Python

.. toctree::
   :caption: Image registration
   :maxdepth: 1

   reader/1.1_Registration_geometrical-transformations
   reader/1.2_Registration_point-based-registration
   reader/1.3_Registration_image-similarity-metrics
   reader/1.4_Registration_intensity-based-registration
   reader/1.5_Registration_active-shape-models
   reader/1.6_CAD_validation_metrics
   reader/Registration_project

.. toctree::
   :caption: Computer-aided diagnosis
   :maxdepth: 1

   reader/2.1_CAD_linear_regression
   reader/2.2_CAD_kNN_decision_trees
   reader/2.3_CAD_generalization_overfitting
   reader/2.4_CAD_logistic_regression
   reader/2.5_CNNs_fundamental_building_blocks
   reader/2.6_CNNs_unsupervised_learning_PCA
   reader/CAD_project