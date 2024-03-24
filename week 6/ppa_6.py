def get_marks(scores_dataset, subject):
    l = []
    for i in scores_dataset:
        l.append(tuple([i["Name"], i[subject]]))
    return l
