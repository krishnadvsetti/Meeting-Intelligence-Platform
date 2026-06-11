def evaluate_response(
    question,
    retrieved_context,
    answer
):
    score = {
        "context_found": len(retrieved_context) > 0,
        "answer_length": len(answer),
        "context_chunks": len(retrieved_context)
    }

    return score