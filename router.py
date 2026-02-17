def route_question(question):

    q = question.lower()

    if "forecast" in q or "predict" in q:
        return "forecast"

    if "trend" in q or "over time" in q:
        return "trend"

    if "compare" in q or "difference" in q:
        return "compare"

    if "chart" in q or "plot" in q:
        return "chart"

    return "sql"
