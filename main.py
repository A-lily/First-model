from utils import read_data
from model import RuleBasedModel
import sys

def main():

    train_file = 'data/train_data.txt'
    test_file = 'data/test_data.txt'
    variables = ['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']

    print ("========= Reading train dataset =========")
    # TO DO:
    train_data = read_data(train_file)
	# use the read data function you created to read the train data
    print ("======== Done reading =========.\n")

    print ("========= Reading test data =========")
    # TO-DO 
    test_data = read_data(test_file)
	# Read the test  data
    print ("========= Done reading =========.\n")

    print ("==== Training classifier =====")
	# TO-DO
    classifier = RuleBasedModel(train_data, test_data)
	# Initialize the classifier you built in model.py and return the necessary values
    print ("======== Done training classifier ===========.\n")

    print ("========= Classifying test samples =======")
	# TO-DO 
    pred_values = classifier.classify(test_data)
    accuracy, numCorrect, total_samples = classifier.calculate_accuracy(pred_values)
	# use your classifier to do predictions on all the test samples
    print ("========== Done classifying =======")

    # TO-DO
	# Evaluate your classifier with the Accuracy function you implemented and return the necessary outputs
    print(f"Model's Accuracy {round(accuracy)} %, model correctly predicted {numCorrect} out of {total_samples}")
    print('================================================================')
    if len(sys.argv) > 1 and '--check' in sys.argv:
        run_sample_classification(sys.argv[1:], classifier)
    print ("finished.\n")


def run_sample_classification(args, classifier):
    try:
        id_input = input("\n\nEnter the ID to predict: ")
        #print(f"ID:{id_input}, type: {type(id_input)}")
        id = int(id_input) if type(id_input) == str else -1
        if id == -1:
            print(f"{id_input} is not a valid ID .. try again")
            return
        class_ = classifier.classify_sample_using_id(id)
        print(f"\npredicted class: {class_}")
    except:
        print(f"\nInvalid Input .. please retry")
    
main()
