.. 8DC00 documentation master file, created by
   sphinx-quickstart on Fri Aug  6 16:31:49 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to the Medical Image Analysis course (8DC00) !
======================================================

| *Course website*: https://github.com/tueimage/8dc00-mia
| *Course edition*: Fall 2021
| *Virtual reader*: https://8dc00-mia-docs.readthedocs.io/en/latest/

This course is a sequel to the second year introductory imaging course. In that course the basic principles of image analysis were covered. 
In 8DC00 we will concentrate on the more advanced image analysis methods and on how they can be used to tackle clinical problems. 
Topics covered include image registration and computer-aided diagnosis (CAD).

Interactive notebooks
=====================

.. toctree::
   :caption: Software guide
   :maxdepth: 2

   reader/0.1_Software_guide

.. toctree::
   :caption: Image registration
   :maxdepth: 1

   reader/1.1_Geometrical_transformations
   reader/1.2_Point-based_registration
   reader/1.3_Image_similarity_metrics
   reader/1.4_Intensity-based_registration
   reader/1.5_Validation_in_medical_image_analysis
   reader/1.6_Registration_project

.. toctree::
   :caption: Computer-aided diagnosis
   :maxdepth: 1

   reader/2.1_Linear_regression
   reader/2.2_Logistic_regression
   reader/2.3_Building_blocks_of_neural_networks
   reader/2.4_Unsupervised_learning_PCA
   reader/2.5_CAD_project

.. toctree::
   :caption: Optional
   :maxdepth: 1
   
   reader/OPTIONAL_active_shape_models