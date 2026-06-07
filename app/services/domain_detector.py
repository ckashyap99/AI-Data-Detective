class DomainDetector:

    DOMAIN_KEYWORDS = {
        "Healthcare": [
            "patient",
            "blood",
            "cholesterol",
            "diagnosis",
            "disease",
            "hospital",
            "doctor",
            "bp",
            "heart",
            "age",
            "sex",
            "chestpain"
            "ECG"
        ],

        "Sales": [
            "sales",
            "revenue",
            "profit",
            "order",
            "customer",
            "product",
            "discount",
            "region"
        ],

        "Real Estate": [
            "property",
            "price",
            "sqft",
            "bedroom",
            "bathroom",
            "zipcode",
            "location",
            "latitude",
            "longitude",
            "median_income",
            "house_value",
            "population",
            "households"
        ],

        "HR": [
            "employee",
            "salary",
            "department",
            "attrition",
            "experience",
            "designation"
        ],

        "Finance": [
            "loan",
            "interest",
            "credit",
            "balance",
            "account",
            "transaction"
        ],

        "Education": [
            "student",
            "marks",
            "grade",
            "subject",
            "attendance",
            "school"
        ]
    }

    @staticmethod
    def detect_domain(df):

        column_names = [
            col.lower()
            for col in df.columns
        ]

        scores = {}

        for domain, keywords in DomainDetector.DOMAIN_KEYWORDS.items():

            score = 0

            for keyword in keywords:

                for col in column_names:

                    if keyword in col:
                        score += 1

            scores[domain] = score

        best_domain = max(
            scores,
            key=scores.get
        )

        confidence = scores[best_domain]

        if confidence == 0:
            best_domain = "Generic Business Dataset"

        return {
            "domain": best_domain,
            "scores": scores
        }