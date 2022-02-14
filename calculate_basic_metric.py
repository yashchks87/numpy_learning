import numpy as np

# create 2 numpy arrays for dummy variables
g_truth = np.random.choice([0,1], size=2000000)
# prediction array consists of probability scores
preds = np.random.rand(2000000)


# After doing timed module numpy implementation is much faster than the regular one.

def calculate_numpy_way(g_truth, preds, thres=0.5):
	# create updated labels with threshold as a score
    updated_labels = np.where(preds > thres, 1, 0)
    # Defining positive and negative....
    neg, pos = 0, 1
    # logical and is similar to and in if statement
    tp = np.sum(np.logical_and(updated_labels == pos, g_truth == pos))
    fp = np.sum(np.logical_and(updated_labels == pos, g_truth == neg))
    tn = np.sum(np.logical_and(updated_labels == neg, g_truth == neg))
    fn = np.sum(np.logical_and(updated_labels == neg, g_truth == pos))
    precision = tp / (tp+fp)
    recall = tp / (tp+fn)
    accuracy = (tp + tn) / (tp + fp + tn + fn)
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'Accuracy: {accuracy}')

def cal(g_truth, preds, thres = 0.5):
    updated_labels = [1 if x > thres else 0 for x in preds]
    tp, fp, tn, fn = 0, 0, 0, 0
    for x in range(len(g_truth)):
        if g_truth[x] == updated_labels[x] == 1:
            tp += 1
        elif g_truth[x] == updated_labels[x] == 0:
            tn += 1
        elif g_truth[x] == 1 and updated_labels[x] == 0:
            fn += 1
        elif g_truth[x] == 0 and updated_labels[x] == 1:
            fp += 1
    precision = tp / (tp+fp)
    recall = tp / (tp+fn)
    accuracy = (tp + tn) / (tp + fp + tn + fn)
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'Accuracy: {accuracy}')