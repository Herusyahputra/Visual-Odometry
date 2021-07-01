"""
Project: Visual Odometry
Name : Heru-05 | M09158023
Date : 10/06/2021
"""

from feature_tracker import feature_tracker_factory, FeatureTrackerTypes
from feature_manager import feature_manager_factory
from feature_types import FeatureDetectorTypes, FeatureDescriptorTypes, FeatureInfo
from feature_matcher import feature_matcher_factory, FeatureMatcherTypes
from parameters import Parameters  


# some default parameters 
kNumFeatures=Parameters.kNumFeatures    
kRatioTest=Parameters.kFeatureMatchRatioTest
kTrackerType = FeatureTrackerTypes.DES_BF      # default descriptor-based, brute force matching with knn 
#kTrackerType = FeatureTrackerTypes.DES_FLANN  # default descriptor-based, FLANN-based matching 
"""
A collection of ready-to-used feature tracker configurations 
"""
class FeatureTrackerConfigs(object):   
    # Test/Template configuration: you can use this to quickly test 
    # - your custom parameters and 
    # - favourite descriptor and detector (check the file feature_types.py)
    TEST = dict(num_features=kNumFeatures,                   
                num_levels = 8,                                  # N.B: some detectors/descriptors do not allow to set num_levels or they set it on their own
                scale_factor = 1.2,                              # N.B: some detectors/descriptors do not allow to set scale_factor or they set it on their own
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.ORB2, 
                match_ratio_test = kRatioTest,
                tracker_type = kTrackerType)
    
    # =====================================
    # LK trackers (these can only be used with VisualOdometry() ... at the present time)
    
    LK_SHI_TOMASI = dict(num_features=kNumFeatures,
                         num_levels = 3,
                         detector_type = FeatureDetectorTypes.SHI_TOMASI,
                         descriptor_type = FeatureDescriptorTypes.NONE, 
                         tracker_type = FeatureTrackerTypes.LK)

    LK_FAST = dict(num_features=kNumFeatures,
                   num_levels = 3,
                   detector_type = FeatureDetectorTypes.FAST, 
                   descriptor_type = FeatureDescriptorTypes.NONE, 
                   tracker_type = FeatureTrackerTypes.LK)

    # =====================================
    # Descriptor-based 'trackers' 
    
    SHI_TOMASI_ORB = dict(num_features=kNumFeatures,                   # N.B.: here, keypoints are not oriented! (i.e. keypoint.angle=0 always)
                          num_levels = 8, 
                          scale_factor = 1.2,
                          detector_type = FeatureDetectorTypes.SHI_TOMASI, 
                          descriptor_type = FeatureDescriptorTypes.ORB, 
                          match_ratio_test = kRatioTest,
                          tracker_type = kTrackerType)
    
    SHI_TOMASI_FREAK = dict(num_features=kNumFeatures,                     
                            num_levels=8,                      
                            scale_factor = 1.2,
                            detector_type = FeatureDetectorTypes.SHI_TOMASI, 
                            descriptor_type = FeatureDescriptorTypes.FREAK, 
                            match_ratio_test = kRatioTest,
                            tracker_type = kTrackerType)      

    FAST_ORB = dict(num_features=kNumFeatures,                         # N.B.: here, keypoints are not oriented! (i.e. keypoint.angle=0 always)
                    num_levels = 8, 
                    scale_factor = 1.2,
                    detector_type = FeatureDetectorTypes.FAST, 
                    descriptor_type = FeatureDescriptorTypes.ORB, 
                    match_ratio_test = kRatioTest,                         
                    tracker_type = kTrackerType) 
    
    FAST_FREAK = dict(num_features=kNumFeatures,                       
                      num_levels = 8,
                      scale_factor = 1.2,                    
                      detector_type = FeatureDetectorTypes.FAST, 
                      descriptor_type = FeatureDescriptorTypes.FREAK,      
                      match_ratio_test = kRatioTest,                          
                      tracker_type = kTrackerType)       

    BRISK = dict(num_features=kNumFeatures,                     
                num_levels = 4, 
                scale_factor = 1.2,
                detector_type = FeatureDetectorTypes.BRISK, 
                descriptor_type = FeatureDescriptorTypes.BRISK, 
                match_ratio_test = kRatioTest,                               
                tracker_type = kTrackerType)  
    
    BRISK_TFEAT = dict(num_features=kNumFeatures,                     
                       num_levels = 4, 
                       scale_factor = 1.2,
                       detector_type = FeatureDetectorTypes.BRISK, 
                       descriptor_type = FeatureDescriptorTypes.TFEAT, 
                       match_ratio_test = kRatioTest,                               
                       tracker_type = kTrackerType)        

    ORB = dict(num_features=kNumFeatures, 
               num_levels = 8, 
               scale_factor = 1.2, 
               detector_type = FeatureDetectorTypes.ORB, 
               descriptor_type = FeatureDescriptorTypes.ORB, 
               match_ratio_test = kRatioTest,                        
               tracker_type = kTrackerType)
    
    ORB2 = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.ORB2, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType)    
    
    BRISK = dict(num_features=kNumFeatures,
                 num_levels = 8,
                 detector_type = FeatureDetectorTypes.BRISK, 
                 descriptor_type = FeatureDescriptorTypes.BRISK,
                 match_ratio_test = kRatioTest,                           
                 tracker_type = kTrackerType)   

    KAZE = dict(num_features=kNumFeatures,
                num_levels = 8,
                detector_type = FeatureDetectorTypes.KAZE, 
                descriptor_type = FeatureDescriptorTypes.KAZE, 
                match_ratio_test = kRatioTest,                          
                tracker_type = kTrackerType)  
    
    AKAZE = dict(num_features=kNumFeatures,
                 num_levels = 8,
                 detector_type = FeatureDetectorTypes.AKAZE, 
                 descriptor_type = FeatureDescriptorTypes.AKAZE, 
                 match_ratio_test = kRatioTest,                          
                 tracker_type = kTrackerType)  
                
    SIFT = dict(num_features=kNumFeatures,
                detector_type = FeatureDetectorTypes.SIFT, 
                descriptor_type = FeatureDescriptorTypes.SIFT, 
                match_ratio_test = kRatioTest,                         
                tracker_type = kTrackerType)
    
    ROOT_SIFT = dict(num_features=kNumFeatures,
                     detector_type = FeatureDetectorTypes.ROOT_SIFT, 
                     descriptor_type = FeatureDescriptorTypes.ROOT_SIFT, 
                     match_ratio_test = kRatioTest,                              
                     tracker_type = kTrackerType)    
    
    # NOTE: SURF is a patented algorithm and not included in the new opencv versions 
    #       If you want to test it, you can install and old version of opencv that supports it: run 
    #       $ pip3 uninstall opencv-contrib-python
    #       $ pip3 install opencv-contrib-python==3.4.2.16
    SURF = dict(num_features=kNumFeatures,
                num_levels = 8,
                detector_type = FeatureDetectorTypes.SURF, 
                descriptor_type = FeatureDescriptorTypes.SURF, 
                match_ratio_test = kRatioTest,                         
                tracker_type = kTrackerType)
        
    SUPERPOINT = dict(num_features=kNumFeatures,                            # N.B.: here, keypoints are not oriented! (i.e. keypoint.angle=0 always)
                      num_levels = 1, 
                      scale_factor = 1.2,
                      detector_type = FeatureDetectorTypes.SUPERPOINT, 
                      descriptor_type = FeatureDescriptorTypes.SUPERPOINT, 
                      match_ratio_test = kRatioTest,                               
                      tracker_type = kTrackerType)

    CONTEXTDESC = dict(num_features=kNumFeatures,                   
                       num_levels = 1,                                  
                       scale_factor = 1.2,                              
                       detector_type = FeatureDetectorTypes.CONTEXTDESC, 
                       descriptor_type = FeatureDescriptorTypes.CONTEXTDESC, 
                       match_ratio_test = kRatioTest,
                       tracker_type = kTrackerType)
    
    KEYNET = dict(num_features=kNumFeatures,                   
                       num_levels = 1,                                  
                       scale_factor = 1.2,                              
                       detector_type = FeatureDetectorTypes.KEYNET, 
                       descriptor_type = FeatureDescriptorTypes.KEYNET, 
                       match_ratio_test = kRatioTest,
                       tracker_type = kTrackerType)
        
    DISK = dict(num_features=kNumFeatures,                   
                       num_levels = 1,                                  
                       scale_factor = 1.2,                              
                       detector_type = FeatureDetectorTypes.DISK, 
                       descriptor_type = FeatureDescriptorTypes.DISK, 
                       match_ratio_test = kRatioTest,
                       tracker_type = kTrackerType)
    
    # =====================================
    # Descriptor-based 'trackers' with ORB2
    
    ORB2_FREAK = dict(num_features=kNumFeatures, 
                      num_levels = 8, 
                      scale_factor = 1.2,                     
                      detector_type = FeatureDetectorTypes.ORB2, 
                      descriptor_type = FeatureDescriptorTypes.FREAK, 
                      match_ratio_test = kRatioTest,                        
                      tracker_type = kTrackerType)    
    
    ORB2_BEBLID = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.BEBLID, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType)    
    
    ORB2_HARDNET = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.HARDNET, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType)    
    
    ORB2_SOSNET = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.SOSNET, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType)   
    
    ORB2_L2NET = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.L2NET, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType) 
