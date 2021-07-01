# Visual Odometry (VO) Utilizing Outdoor Environment Using Optical Flow
##### Advisor : Dr. Chuang-Jan Chang
**Create By : Cj-Heru05**                                                                                                                                   
**Date : Juni 10, 2021**

1. **Introduction** 

    Currently, 3D structure acquisition of real objects is a digital storage and recording technology that has various application requirements in scientific and     engineering fields such as object modeling, scene modeling, realistic rendering, robot navigation, target recognition, and 3D measurement. Technology-based       research in computer vision will be applied in this study based on 3D reconstruction techniques and trajectory trajectories based on paths and pose               estimations which have great theoretical research value and are significant in practical applications, this study uses visual odometry by estimating the           beginning of the camera odometry change to each poses, and each visual odometry group was estimated to have a different scale.

2. **Analisys Research**

    ![z](https://user-images.githubusercontent.com/60929939/124069183-54dd9e80-da6e-11eb-8f0d-ad2467cd3dbe.png)

3. **Methodology Imlementation**
     - Features Detection
     ```
      1. LK Shi-Tomasi
      
      2. LK Fast
     ``` 
     - Features Descriptor
     ```
      (SHI_TOMASI_ORB, FAST_ORB, ORB, BRISK, AKAZE, FAST_FREAK, SIFT, ROOT_SIFT, SURF, SUPERPOINT, FAST_TFEAT)
     ``` 
     - Features Matching
     ```
      1. Bruce Force (BF) and Nearest Neighbors
      
      2. Fast Library for Approximate Nearest Neighbors (FLANN)
     ``` 
     - Optical FLow
     ```
      1. Motion field and optical flow
      
      2. Optical flow constraint equation
      
      3. Lucas Kanade (LK) method
      
      4. Coarse to fine flow estimation
      
      5. Application of optical flow

      # Refferences from (Shree K. Nayar) Computer Vision Columbia, New York
     ``` 
     - FLowchart
     ```
      Coming Soon
     ``` 
     
4. **How to use this apps**

   Follow these steps to installation apication: 
     - Open your terminal by clicking Ctrl + Alt + T 
   Step 1:
     - Type the command for a permissions
     ```
      $ git clone https://github.com/Herusyahputra/Visual-Odometry.git
     ``` 
     ```
      $ cd Visual-Odometry
     ```
     ```
      $ cd src/python3 main_vo.py
     ``` 
   
   Steps 2:
     - Type the command for a permissions
     ```
      $ chmod +x autoSetUp
     ``` 
     - Type the command for installation application
     ```
      $ ./autoSetUp
     ```
   Note: If you find the problem can't open the video, please Download [datasets](https://mcut-my.sharepoint.com/:f:/g/personal/m09158023_o365_mcut_edu_tw/Epup_-IDnudBgm_EUjRumkEB5K4iHOlKZRkjatFcv3fKIg?e=DxOsdE), replace the video file that is in the Visual-Odometry/src/datasets folder
      
5. **Referencess**                                                                                                         
    [1]. CamOdoCal: Automatic intrinsic and extrinsic calibration of a rig with multiple generic cameras and odometry, Link: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6696592                                                                                         
    [2]. Research Monocolar Visual Odometry Based on 3D-2D Motion Estimation, Link: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7904314         
    [3]. Monocolar Visual Odometry based on Optical Flow and Feature Matching, Link: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7979301             
    [4]. Real-time Monocolar Visual Odometry Using Optical  Flow: Study on Navigation of Quadrotors, LInk: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8011864                                                                                                                                       
    [5]. Monocolor Visual Odometry for Trajectory Estimation of a Moving Object Using Ground Plane Geometry, LInk: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8993259
