import pandas as pd
import re

roll_no = "1024170052"

# Question 1
fixed_entries = [
    {"question": "what is the annual fee", "answer": "The annual fee is Rs 500.", "keywords": "fee cost price charge", "category": "billing"},
    {"question": "how to reset password", "answer": "Go to Settings > Reset Password.", "keywords": "password reset login", "category": "account"},
    {"question": "what are your working hours", "answer": "We are open 9 AM to 5 PM.", "keywords": "hours timing open time", "category": "general"},
    {"question": "how can i pay the fee", "answer": "You can pay via UPI, card, or net banking.", "keywords": "pay payment upi fee", "category": "billing"}
]

categories = ["billing", "account", "general"]

last_two_digits = [int(digit) for digit in roll_no[-2:]]

personalized_entries = [
    {
        "question": "how can i contact customer support",
        "answer": "You can contact customer support through the Help section.",
        "keywords": "help support contact",
        "category": categories[last_two_digits[0] % 3]
    },
    {
        "question": "what services are available",
        "answer": "You can view all available services on the services page.",
        "keywords": "services options available",
        "category": categories[last_two_digits[1] % 3]
    }
]

entries = fixed_entries + personalized_entries
df = pd.DataFrame(entries)

print("Q1: Final Knowledge Base")
print(df)
print()

# Question 2
def score_query(query, data):
    query_words = set(re.findall(r"\w+", query.lower()))
    results = []

    for index, row in data.iterrows():
        text = row["question"] + " " + row["keywords"]
        entry_words = set(re.findall(r"\w+", text.lower()))
        score = len(query_words.intersection(entry_words))

        if score > 0:
            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "keywords": row["keywords"],
                "category": row["category"],
                "confidence": score
            })

    result_df = pd.DataFrame(results)

    if not result_df.empty:
        result_df = result_df.sort_values(by="confidence", ascending=False).reset_index(drop=True)

    return result_df

print("Q2: Query Scoring")
query = input("Enter a query: ")
print(score_query(query, df))
print()

# Question 3
def same_category(category_name, data):
    return data[data["category"].str.lower() == category_name.lower()]

selected_category = personalized_entries[0]["category"]

print("Q3: Entries in category:", selected_category)
print(same_category(selected_category, df))
print()

# Question 4
print("Q4: Add a new keyword")
entry_index = 0
new_keyword = input("Enter a new keyword for the first entry: ")
df.loc[entry_index, "keywords"] = df.loc[entry_index, "keywords"] + " " + new_keyword
file_name = roll_no + "_faq_data.csv"
df.to_csv(file_name, index=False)
print("Updated DataFrame")
print(df)
print("Saved as", file_name)
print()

# Question 5
print("Q5: Number of entries per category")
print(df.groupby("category").size())
print()

# Question 6
def score_query_with_ties(query, data):
    result_df = score_query(query, data)

    if result_df.empty:
        print("No matching entries found.")
        return result_df

    highest_score = result_df["confidence"].max()
    highest_matches = result_df[result_df["confidence"] == highest_score]

    if len(highest_matches) > 1:
        print("Multiple entries have the highest confidence score:")
        print(highest_matches)
    else:
        print("Best matching entry:")
        print(highest_matches)

    return result_df

print("Q6: Query producing a tie")
score_query_with_ties("fee", df)
print()

print("Q6: Query not producing a tie")
score_query_with_ties("password reset", df)
