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
