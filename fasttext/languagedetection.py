import fasttext
import logging

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

class LanguageIdentification:

    def __init__(self):
        # path to pretrained model
        path_to_pretrained_model = "models/lid.176.bin"
        # load model
        self.model = fasttext.load_model(path_to_pretrained_model)

    def language_classification(self, text, topmatches: int = 2):
        # lowercase
        text = text.lower()
        # Get predictions
        predictions = self.model.predict(text, k= topmatches) # returns top k predictions
        # extract predicted labels + accuracy
        labels, accuracy_list = predictions
        # convert tuple into list
        label_list = list(labels)
        # strip __label__ in predictions
        detected_labels = [label.replace("__label__","") for label in label_list]
        # get accuracy scores
        accuracy_scores = [float(acc) for acc in accuracy_list]
        # logging
        logging.info("detected language: {}".format(detected_labels))
        logging.info("accuracy score:    {}".format(accuracy_scores))
        # create a dictionary with labels and acc scores
        results = dict(zip(detected_labels, accuracy_scores))

        return results
    
    