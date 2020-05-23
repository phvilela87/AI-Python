# Build-in modules
import logging
import os
import sys

# Added modules
import cv2
import numpy as np
from imutils import paths, build_montages
from skimage import feature
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder

model = None

# Print in software terminal
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s | %(process)d | %(name)s | %(levelname)s:  %(message)s',
                    datefmt='%d/%b/%Y - %H:%M:%S')

logger = logging.getLogger(__name__)


def quantify_image(image):
    # compute the histogram of oriented gradients feature vector for the input image
    features = feature.hog(image, orientations=9,
                           pixels_per_cell=(10, 10), cells_per_block=(2, 2),
                           transform_sqrt=True, block_norm="L1")

    # return the feature vector
    return features


def load_split(path):
    # grab the list of images in the input directory, then initialize the list of data (i.e., images) and class labels
    image_paths = list(paths.list_images(path))
    data = []
    labels = []

    # loop over the image paths
    for imagePath in image_paths:
        # extract the class label from the filename
        label = imagePath.split(os.path.sep)[-2]

        # load the input image, convert it to grayscale, and resize
        # it to 200x200 pixels, ignoring aspect ratio
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (200, 200))

        # threshold the image such that the drawing appears as white
        # on a black background
        image = cv2.threshold(image, 0, 255,
                              cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        # quantify the image
        features = quantify_image(image)

        # update the data and labels lists, respectively
        data.append(features)
        labels.append(label)

    # return the data and labels
    return np.array(data), np.array(labels)


def application():
    """" All application has its initialization from here """
    global model
    logger.info('Main application is running!')

    # Store current working directory
    path = os.path.abspath('')

    # Append current directory to the python path
    sys.path.append(path)

    # define the path to the training and testing directories
    training_path = path + '/dataset/spiral/training'
    testing_path = path + '/dataset/spiral/testing'

    n_trials = 20

    # loading the training and testing data
    logger.info("[INFO] loading data...")
    (trainX, trainY) = load_split(training_path)
    (testX, testY) = load_split(testing_path)

    # encode the labels as integers
    le = LabelEncoder()
    trainY = le.fit_transform(trainY)
    testY = le.transform(testY)

    # initialize our trials dictionary
    trials = {}

    # loop over the number of trials to run
    for i in range(0, int(n_trials)):
        # train the model
        logger.info("[INFO] training model {} of {}...".format(i + 1, int(n_trials)))
        model = RandomForestClassifier(n_estimators=100)
        model.fit(trainX, trainY)

        # make predictions on the testing data and initialize a dictionary to store our computed metrics
        predictions = model.predict(testX)
        metrics = {}

        # compute the confusion matrix and and use it to derive the raw accuracy, sensitivity, and specificity
        cm = confusion_matrix(testY, predictions).flatten()
        (tn, fp, fn, tp) = cm
        metrics["acc"] = (tp + tn) / float(cm.sum())
        metrics["sensitivity"] = tp / float(tp + fn)
        metrics["specificity"] = tn / float(tn + fp)

        # loop over the metrics
        for (k, v) in metrics.items():
            # update the trials dictionary with the list of values for the current metric
            l = trials.get(k, [])
            l.append(v)
            trials[k] = l

    # loop over our metrics
    for metric in ("acc", "sensitivity", "specificity"):
        # grab the list of values for the current metric, then compute the mean and standard deviation
        values = trials[metric]
        mean = np.mean(values)
        std = np.std(values)

        # show the computed metrics for the statistic
        logger.info(metric)
        logger.info("=" * len(metric))
        logger.info("u={:.4f}, o={:.4f}".format(mean, std))
        logger.info("")

    # randomly select a few images and then initialize the output images for the montage
    testing_paths = list(paths.list_images(testing_path))
    idxs = np.arange(0, len(testing_paths))
    idxs = np.random.choice(idxs, size=(25,), replace=False)
    images = []

    # loop over the testing samples
    for i in idxs:
        # load the testing image, clone it, and resize it
        image = cv2.imread(testing_paths[i])
        output = image.copy()
        output = cv2.resize(output, (128, 128))

        # pre-process the image in the same manner we did earlier
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (200, 200))
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        # quantify the image and make predictions based on the extracted features using the last trained Random Forest
        features = quantify_image(image)
        preds = model.predict([features])
        label = le.inverse_transform(preds)[0]

        # draw the colored class label on the output image and add it to the set of output images
        color = (0, 255, 0) if label == "healthy" else (0, 0, 255)
        cv2.putText(output, label, (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        images.append(output)

    # create a montage using 128x128 "tiles" with 5 rows and 5 columns
    # montage = build_montages(images, (128, 128), (5, 5))[0]
    # show the output montage
    # cv2.imshow("Output", montage)
    # cv2.waitKey(0)

    new = path + '/image/pedro.jpeg'
    images = []

    # load the testing image, clone it, and resize it
    image = cv2.imread(new)
    output = image.copy()
    output = cv2.resize(output, (512, 512))

    # pre-process the image in the same manner we did earlier
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (200, 200))
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # quantify the image and make predictions based on the extracted features using the last trained Random Forest
    features = quantify_image(image)
    preds = model.predict([features])
    label = le.inverse_transform(preds)[0]

    # draw the colored class label on the output image and add it to the set of output images
    color = (0, 255, 0) if label == "healthy" else (0, 0, 255)
    cv2.putText(output, label, (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    images.append(output)

    # create a montage using 128x128 "tiles" with 5 rows and 5 columns
    montage = build_montages(images, (512, 512), (1, 1))[0]

    # show the output montage
    cv2.imshow("Output", montage)
    cv2.waitKey(0)
