import pandas as pd
import json


class Classifier:
    def __init__(self, dictionary):
        self._dict = dictionary

    def classify_into_groups(self, data, input_col, output_col_name="Category"):
        def assign_category(row):
            for category, titles in self._dict.items():
                if row[input_col] in titles:
                    return category
            return f"{row['org']} - {row[input_col]}"

        data[output_col_name] = data.apply(assign_category, axis=1)
        return data


if __name__ == '__main__':
    with open("job-categories.json", "r") as file:
        jobs_dict = json.load(file)

    job_classifier = Classifier(jobs_dict)
    df = pd.read_csv("(Copy) org_role_100K.txt", sep='\t')
    df_grpBy_dept = job_classifier.classify_into_groups(
        df, "role_original", "Department")

    print(df_grpBy_dept)
