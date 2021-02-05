#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/features2d.hpp"
#include "opencv2/xfeatures2d.hpp"
#include "testFunctions.h"
#include <iostream>


int main()
{
    std::string image_path = "images/test_2.bmp";
    cv::Mat img = imread(image_path, cv::IMREAD_COLOR);

    if(img.empty())
    {
        std::cout << "Could not read the image: " << image_path << std::endl;
        return 1;
    }
    cv::imshow("Display window", img);

    cv::Rect myROI(880,560,50,35);
    cv::Mat croppedImg = img(myROI);
    cv::imshow("cropped",croppedImg);
    cv::waitKey(0); // Wait for a keystroke in the window
    std::cout<<croppedImg.size()<<std::endl;
    detectFeat(croppedImg,"SURF");

    return 0;
}