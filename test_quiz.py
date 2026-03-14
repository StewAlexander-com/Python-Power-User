#!/usr/bin/env python3
"""
Test pipeline for python_poweruser.py quiz and NLP answer-matching.

Runs unit tests on _normalize, _synonym_expand, _tokens_match, _hint_tier,
and _check_answer, plus a minimal integration test that the quiz runs
with --no-save and mocked input.

Usage:
  python test_quiz.py
  python test_quiz.py -v

Requires: Python 3.10+ (stdlib only; no pytest).
"""

import sys
import io
import unittest
from unittest.mock import patch

# Import the module under test (same directory as this script)
import python_poweruser as pp


class TestNormalize(unittest.TestCase):
    """Test _normalize(): quote stripping and spacing normalization."""

    def test_strips_outer_quotes(self):
        self.assertEqual(pp._normalize("'ell'"), "ell")
        self.assertEqual(pp._normalize('"hello"'), "hello")

    def test_strips_whitespace(self):
        self.assertEqual(pp._normalize("  3  "), "3")
        self.assertEqual(pp._normalize("\tTrue\n"), "True")

    def test_normalises_comma_spacing(self):
        self.assertEqual(pp._normalize("[1,2,3]"), "[1, 2, 3]")
        self.assertEqual(pp._normalize("{1, 2, 3}"), "{1, 2, 3}")

    def test_normalises_bracket_spacing(self):
        self.assertEqual(pp._normalize("[ 1, 2 ]"), "[1, 2]")
        self.assertEqual(pp._normalize("( 1, 2 )"), "(1, 2)")

    def test_colon_spacing(self):
        self.assertEqual(pp._normalize("{'a':1}"), "{'a': 1}")

    def test_leave_inner_quotes(self):
        self.assertEqual(pp._normalize("'hello'"), "hello")


class TestSynonymExpand(unittest.TestCase):
    """Test _synonym_expand(): alias and prefix stripping."""

    def test_returns_input_first(self):
        out = pp._synonym_expand("foo")
        self.assertEqual(out[0], "foo")

    def test_adds_alias_canonical(self):
        out = pp._synonym_expand("true")
        self.assertIn("True", out)
        out = pp._synonym_expand("none")
        self.assertIn("None", out)

    def test_strips_prefix_the_answer_is(self):
        out = pp._synonym_expand("the answer is 42")
        self.assertIn("42", out)

    def test_strips_prefix_returns(self):
        out = pp._synonym_expand("returns True")
        self.assertIn("True", out)

    def test_strips_prefix_evaluates_to(self):
        out = pp._synonym_expand("evaluates to [1,2,3]")
        self.assertIn("[1,2,3]", out)

    def test_no_duplicates(self):
        out = pp._synonym_expand("true")
        self.assertEqual(out.count("True"), 1)


class TestTokensMatch(unittest.TestCase):
    """Test _tokens_match(): order-insensitive set/dict comparison."""

    def test_set_same_tokens(self):
        self.assertTrue(pp._tokens_match("{1, 2, 3}", "{3, 2, 1}"))

    def test_set_different_tokens(self):
        self.assertFalse(pp._tokens_match("{1, 2}", "{1, 2, 3}"))

    def test_dict_like(self):
        self.assertTrue(pp._tokens_match("{'a': 1, 'b': 2}", "{'b': 2, 'a': 1}"))


class TestHintTier(unittest.TestCase):
    """Test _hint_tier(): contextual hints for wrong answers."""

    def test_high_similarity(self):
        hint = pp._hint_tier("Trure", True)
        self.assertIsNotNone(hint)
        self.assertIn("close", hint.lower())

    def test_right_type_wrong_value(self):
        hint = pp._hint_tier("False", True)  # bool, wrong value
        self.assertIsNotNone(hint)
        self.assertIn("type", hint.lower())
        self.assertIn("value", hint.lower())

    def test_value_correct_repr_differs(self):
        hint = pp._hint_tier("1", True)  # 1 == True for value, repr differs
        self.assertIsNotNone(hint)
        self.assertIn("Technically", hint)

    def test_off_by_one(self):
        # Use input that doesn't eval to same type so we hit off-by-one branch (not "right type wrong value")
        hint = pp._hint_tier("4.0", 3)  # float 4.0 vs int 3, diff=1
        self.assertIsNotNone(hint)
        self.assertIn("Off by one", hint)

    def test_string_without_quotes(self):
        # User typed value without quotes; we get a hint (high ratio or "correct value")
        hint = pp._hint_tier("ell", "ell")  # expected string "ell"
        self.assertIsNotNone(hint)
        self.assertIn("close", hint.lower())

    def test_no_hint_for_totally_wrong(self):
        hint = pp._hint_tier("xyz", 42)
        self.assertIsNone(hint)


class TestCheckAnswer(unittest.TestCase):
    """Test _check_answer(): full pipeline (alias, repr, eval, numeric, fuzzy)."""

    def test_direct_repr_match(self):
        self.assertTrue(pp._check_answer("'ell'", "ell"))
        self.assertTrue(pp._check_answer("3", 3))
        self.assertTrue(pp._check_answer("True", True))

    def test_bool_aliases_accepted_for_bool(self):
        self.assertTrue(pp._check_answer("yes", True))
        self.assertTrue(pp._check_answer("no", False))
        self.assertTrue(pp._check_answer("1", True))
        self.assertTrue(pp._check_answer("0", False))
        self.assertTrue(pp._check_answer("true", True))
        self.assertTrue(pp._check_answer("false", False))

    def test_bool_aliases_rejected_for_non_bool(self):
        # "yes"/"no" must not match int 1/0 (bool-only aliases)
        self.assertFalse(pp._check_answer("yes", 1))
        self.assertFalse(pp._check_answer("no", 0))
        # "1"/"0" as digits still match int 1/0 via direct repr match
        self.assertTrue(pp._check_answer("1", 1))
        self.assertTrue(pp._check_answer("0", 0))

    def test_none_aliases(self):
        self.assertTrue(pp._check_answer("none", None))
        self.assertTrue(pp._check_answer("null", None))
        self.assertTrue(pp._check_answer("None", None))

    def test_type_name_phrasing(self):
        self.assertTrue(pp._check_answer("float", type(1.0).__name__))
        self.assertTrue(pp._check_answer("a string", "str"))
        self.assertTrue(pp._check_answer("integer", "int"))

    def test_synonym_expansion(self):
        self.assertTrue(pp._check_answer("the answer is 3", 3))
        self.assertTrue(pp._check_answer("returns True", True))

    def test_eval_match(self):
        self.assertTrue(pp._check_answer("(1, [2, 3], 5)", (1, [2, 3], 5)))
        self.assertTrue(pp._check_answer("[1, 2, 3]", [1, 2, 3]))
        self.assertTrue(pp._check_answer("True", True))

    def test_token_match_sets(self):
        self.assertTrue(pp._check_answer("{2, 1, 3}", {1, 2, 3}))

    def test_numeric_int_float_cross(self):
        self.assertTrue(pp._check_answer("3.0", 3))
        self.assertTrue(pp._check_answer("3", 3))

    def test_numeric_float_tolerance(self):
        self.assertTrue(pp._check_answer("0.1", 0.1))
        self.assertTrue(pp._check_answer("1e-6", 1e-6))

    def test_reject_empty(self):
        self.assertFalse(pp._check_answer("", 3))
        self.assertFalse(pp._check_answer("   ", 3))

    def test_reject_wrong_answer(self):
        self.assertFalse(pp._check_answer("4", 3))
        self.assertFalse(pp._check_answer("'ello'", "ell"))
        self.assertFalse(pp._check_answer("False", True))

    def test_string_type_error_question(self):
        self.assertTrue(pp._check_answer("TypeError", "TypeError"))
        self.assertTrue(pp._check_answer("'TypeError'", "TypeError"))


class TestQuizIntegration(unittest.TestCase):
    """Integration: quiz runs with --no-save and mocked input."""

    def test_run_self_tests_completes_with_mocked_input(self):
        # Feed: difficulty "a" (All), then 50 skips (empty line) to exit the quiz
        with patch("builtins.input", side_effect=["a"] + [""] * 60):
            with patch("sys.stdout", new_callable=io.StringIO) as buf:
                try:
                    passed, total = pp.run_self_tests(no_save=True)
                except Exception as e:
                    self.fail(f"run_self_tests raised: {e}")
        self.assertIsInstance(passed, int)
        self.assertIsInstance(total, int)
        self.assertGreater(total, 0)
        self.assertGreaterEqual(passed, 0)
        self.assertIn("Score:", buf.getvalue())


def run():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for cls in (
        TestNormalize,
        TestSynonymExpand,
        TestTokensMatch,
        TestHintTier,
        TestCheckAnswer,
        TestQuizIntegration,
    ):
        suite.addTests(loader.loadTestsFromTestCase(cls))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run())
