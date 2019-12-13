import os

from fastai.vision import Path, load_learner, open_image

from image_converter import ImageHandler


def get_prediction(path):
    """Returns confidence level and prediction of a given image.
    Params:
    path: path of the image to be predicted
    """

    cwd = os.getcwd()
    weights_path = Path(cwd + '/Backend/ServerSide/')

    learn = load_learner(weights_path)
    img = open_image(path)

    pred_class, pred_idx, confidence = learn.predict(img)

    if str(pred_class) == 'Tampered':
        conf = float(confidence[1])
    elif str(pred_class) == 'Authentic':
        conf = float(confidence[0])

    conf = conf * 100

    if conf >= 65:
        return (pred_class, conf)

    return 0


if __name__ == '__main__':

    # img_path = '/Users/tiagoramalho/Downloads/Demo_Images/mercedes.jpg'
    # img_obj = ImageHandler(path=img_path)

    # ela_img = img_obj.convert_to_ela()
    # result = get_prediction(ela_img)

    # print('*' * 100)
    # print('Prediction: {}'.format(result[0]))
    # print('Confidence: {:.3f}%'.format(result[1]))
    # print('*' * 100)

    pass
