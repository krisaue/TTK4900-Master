#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/features2d.hpp"
#include "opencv2/xfeatures2d.hpp"
#include <iostream>

void detectFeat(cv::Mat img,std::string descriptor){
    std::vector<cv::KeyPoint> keypoints;
    if(descriptor == "SURF"){
        int minHessian = 10;
        cv::Ptr<cv::xfeatures2d::SURF> detector = cv::xfeatures2d::SURF::create(minHessian);
        detector->detect(img,keypoints);
    }
    else if(descriptor == "SIFT")
    {
        cv::Ptr<cv::xfeatures2d::SIFT> detector = cv::xfeatures2d::SIFT::create();
        detector->detect(img,keypoints);
    }
    else if(descriptor == "ORB")
    {
        cv::Ptr<cv::FeatureDetector> detector = cv::ORB::create();
        detector->detect(img,keypoints);
    }

    cv::Mat img_keypoints;
    cv::drawKeypoints(img,keypoints,img_keypoints);
    cv::imshow("SURF keypoints", img_keypoints);
    cv::waitKey(0);
    std::cout<<"The test image with "<<descriptor<<" as descriptor found "<<keypoints.size()<<" keypoints."<<std::endl;
    std::string imgName = descriptor+"_features2.png";
    std::cout<<imgName<<std::endl;
    //cv::imwrite(imgName,img_keypoints);
}