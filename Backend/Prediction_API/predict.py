import os

from fastai.vision import Path, load_learner, open_image


def get_prediction(path):
    """Returns confidence level and prediction of a given image.
    Params:
    path: path of the image to be predicted
    """

    cwd = os.getcwd()
    # weights_path = Path(cwd + '/Backend/Prediction_API/weights/')
    weights_path = Path(cwd + '/weights/')

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
