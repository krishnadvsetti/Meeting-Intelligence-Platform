from app.evaluation.faithfulness import (
    score_faithfulness
)

score = score_faithfulness(
    question="What concerns were raised about parking?",
    context="""
Parking exemptions were discussed.
Affordable housing impacts were discussed.
""",
    answer="""
Parking exemptions affected affordability.
"""
)

print(score)