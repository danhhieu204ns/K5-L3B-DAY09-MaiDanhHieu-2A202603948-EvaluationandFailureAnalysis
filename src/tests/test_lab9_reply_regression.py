"""A fluent refund reply cannot claim more than the committed ledger amount."""
import pytest

pytestmark = pytest.mark.student


def test_reply_amount_matches_ledger_for_fixed_but_not_regression():
    from pydantic_evals.evaluators import EvaluatorContext
    from lab9.graders import ReplyLedgerConsistent
    from lab9.trace_case import investigate

    grader = ReplyLedgerConsistent()
    scores = {}
    for shape in ("fixed", "seeded_regression"):
        case = investigate(shape, "C-008", 11)
        ctx = EvaluatorContext(name="C-008@11", inputs={}, metadata=None,
                               expected_output=case["label"], output=case["trial"],
                               duration=0.0, _span_tree=None, attributes={}, metrics={})
        scores[shape] = grader.evaluate(ctx).value
    assert scores == {"fixed": True, "seeded_regression": False}
