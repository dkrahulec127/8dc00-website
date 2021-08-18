.. 8DC00 documentation master file, created by
   sphinx-quickstart on Fri Aug  6 16:31:49 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to the Medical Image Analysis course (8DC00) !
======================================================

| *Course website*: https://github.com/tueimage/8dc00-mia
| *Course edition*: Fall 2021
| *Virtual reader*: https://8dc00-website.readthedocs.io/en/latest/

This course is a sequel to the second year introductory imaging course. In that course the basic principles of image analysis were covered. 
In 8DC00 we will concentrate on the more advanced image analysis methods and on how they can be used to tackle clinical problems. 
Topics covered include image registration and computer-aided diagnosis (CAD).

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