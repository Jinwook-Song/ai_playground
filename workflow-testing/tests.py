import pytest
from main import graph


@pytest.mark.parametrize(
    "email, category, priority_score",
    [
        ("i have an offer for you!", "spam", 1),
        ("i have an urgent message for you!", "urgent", 10),
        ("i have a normal message for you!", "normal", 5),
    ],
)
def test_full_graph(email, category, priority_score):
    result = graph.invoke({"email": email})

    assert result["category"] == category
    assert result["priority_score"] == priority_score


def test_individual_nodes():
    # categorize_email
    result = graph.nodes["categorize_email"].invoke(
        {"email": "i have an offer for you!"}
    )

    assert result["category"] == "spam"

    # assing_priority
    result = graph.nodes["assing_priority"].invoke({"category": "spam"})
    assert result["priority_score"] == 1

    # draft_response
    result = graph.nodes["draft_response"].invoke({"category": "spam"})
    assert "Go away" in result["response"]
