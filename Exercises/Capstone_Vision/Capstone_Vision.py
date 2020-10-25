import numpy as np
import cv2
import sys

def main(argv):
    ## [load file]
    default_file = 'capstone_coins.png'
    filename = argv[0] if len(argv) > 0 else default_file

    # Loads an image
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    ## [load]

    ## [convert_to_gray]
    # Convert it to gray
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ## [convert_to_gray]

    ## [reduce_noise]
    # Reduce the noise to avoid false circle detection
    gray = cv2.medianBlur(gray, 5)
    ## [reduce_noise]

    ## [houghcircles]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.9, 220,
                               param1=50, param2=27,
                               minRadius=80, maxRadius=160)
    ## [houghcircles]

    ## [get brightness of circles]
    def av_pix(img, circles, size):
        av_value = []
        for coords in circles[0,:]:
            col = np.mean(img[coords[1] - size:coords[1] + size, coords[0] - size:coords[0] + size])
            #print(img[coords[1] - size:coords[1] + size, coords[0] - size:coords[0] + size])
            av_value.append(col)
        return av_value

    radius_list = []

    ## [draw]
    if circles is not None:
        circles = np.uint16(np.around(circles))
        count = 1
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(src, center, 1, (0, 100, 100), 3)
            #cv2.putText(src, str(count), center, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
            count += 1
            # circle outline
            radius = i[2]
            radius_list.append(radius)
            print(radius_list)
            cv2.circle(src, center, radius, (255, 0, 255), 3)
    ## [draw]

    bright_values = av_pix(src, circles, 20)
    print(bright_values)

    ## [Using brightness to identify value of coins]
    values = []
    for a,b in zip(bright_values, radius_list):
        if a > 160 and b > 120:
            values.append(10)
        elif a > 160 and b <= 120:
            values.append(5)
        elif a < 150 and b > 140:
            values.append(2)
        elif a <= 130 and b <= 140:
            values.append(1)
        print(a, b, values)
    print(values)
    

    ##[Drawing of values on coins]
    count_2 = 0
    for i in circles[0,:]:
        cv2.putText(src, str(values[count_2]) + "p", (i[0], i[1]), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2 , (0, 0, 0), 2)
        count_2 += 1
    cv2.putText(src, "ESTIMATED TOTAL VALUE: " + str(sum(values)) + "p", (200, 100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.3, 255)

  ## [display]
    src = cv2.resize(src, (960, 540))  
    cv2.imshow("detected circles", src)
    cv2.waitKey(0)
    ## [display]

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])