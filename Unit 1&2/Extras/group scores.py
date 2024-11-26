group_scores = {
    "Group A": {"Math": 85, "Science": 88, "English": 90},
    "Group B": {"Math": 90, "Science": 80, "English": 89},
}


def update_average_score(group_name, subject, new_score):
    if group_name in group_scores:
        group = group_scores[group_name]
        if subject in group:
            group[subject] = new_score
        else:
            group[subject] = new_score
    else:
        group_scores[group_name] = {subject: new_score}
