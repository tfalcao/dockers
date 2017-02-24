import cv2
import numpy as np
import matplotlib as mp


def main():
	print 'OpenCV     : %s' % cv2.__version__
	print 'numpy      : %s' % np.__version__
	print 'matplotlib : %s' % mp.__version__


if __name__ == "__main__":
    main()