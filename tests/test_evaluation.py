from app.evaluation.evaluator import (
    evaluate_response
)

result = evaluate_response(
    question="What concerns were raised about parking?",
    retrieved_context=[
        "Parking exemptions...",
        "Affordable housing..."
    ],
    answer="Concerns included parking exemptions and development costs."
)

print(result)