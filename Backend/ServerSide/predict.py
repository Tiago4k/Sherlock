import os

from fastai.vision import load_learner, open_image


def get_prediction(weights, path):

    learn = load_learner(weights)

    img = open_image(path)

    pred_class, pred_idx, confidence = learn.predict(img)

    if str(pred_class) == 'Tampered':
        conf = float(confidence[1])
    elif str(pred_class) == 'Authentic':
        conf = float(confidence[0])

    conf = conf * 100

    if conf >= 65:
        return (pred_class, conf)

    return 'Unable to confidently provide a prediction for this image.'
