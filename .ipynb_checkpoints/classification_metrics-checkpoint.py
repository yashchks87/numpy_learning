import numpy as np

class GenerateMetrics():
    def __init__(self, ground_truth, preds, pos = 1, neg = 0, thres = 0.5):
        self.g_truth = ground_truth
        self.preds = preds
        self.pos = pos
        self.neg = neg
        self.base_metrics()
    def base_metrics(self):
        self.TP = np.sum(np.logical_and(self.g_truth == self.pos, self.preds == self.pos))
        self.FP = np.sum(np.logical_and(self.g_truth == self.neg, self.preds == self.pos))
        self.TN = np.sum(np.logical_and(self.g_truth == self.neg, self.preds == self.neg))
        self.FN = np.sum(np.logical_and(self.g_truth == self.pos, self.preds == self.neg))
    def base_metrics_print(self):
        print(f'TP: {self.TP}')
        print(f'FP: {self.FP}')
        print(f'TN: {self.TN}')
        print(f'FN: {self.FN}')
    def precision(self):
        return self.TP / (self.TP + self.FP)
    def recall(self):
        return self.TP / (self.TP + self.FN)
    def accuracy(self):
        return (self.TP + self.TN) / (self.TP + self.TN + self.FP + self.FN)
    def f1_score(self):
        numer = self.precision() * self.recall()
        deno = self.precision() + self.recall()
        temp = numer / deno
        return 2 * temp
    
if __name__ == '__main__':
    GenerateMetrics()