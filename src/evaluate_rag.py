from generate_answer import generate_answer

# each test case has a question, and the source file we expect it to be grounded in
TEST_CASES = [
    {
        "question": "What model was used for churn prediction?",
        "expected_source": "Churn_project.txt"
    },
    {
        "question": "What was the ROC-AUC of the churn prediction model?",
        "expected_source": "Churn_project.txt"
    },
    {
        "question": "What dataset was used in the e-commerce pipeline project?",
        "expected_source": "olist_project.txt"
    },
    {
        "question": "What cloud storage service was used for the Olist project?",
        "expected_source": "olist_project.txt"
    },
    {
        "question": "What model achieved the best WAPE in the supply chain forecasting project?",
        "expected_source": "supply_chain_project.txt"
    },
    {
        "question": "What technique was used to compute safety stock in the inventory project?",
        "expected_source": "supply_chain_project.txt"
    }
]


def evaluate():
    correct_retrieval = 0
    total = len(TEST_CASES)

    print(f"Running {total} evaluation questions...\n")

    for i, case in enumerate(TEST_CASES, start=1):
        result = generate_answer(case["question"])

        retrieved_correct_source = case["expected_source"] in result["sources"]
        if retrieved_correct_source:
            correct_retrieval += 1

        status = "PASS" if retrieved_correct_source else "FAIL"

        print(f"[{status}] Q{i}: {case['question']}")
        print(f"Expected source: {case['expected_source']}")
        print(f"Actual sources: {result['sources']}")
        print(f"Answer: {result['answer'][:150]}...")
        print("-" * 60)

    accuracy = (correct_retrieval / total) * 100
    print(f"\nRetrieval accuracy: {correct_retrieval}/{total} ({accuracy:.1f}%)")


if __name__ == "__main__":
    evaluate()