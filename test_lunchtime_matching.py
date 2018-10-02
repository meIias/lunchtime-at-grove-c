"""
test_lunchtime_matching.py

- unittests around the lunch/coffee matching algorithms
"""

import unittest

import lunchtime_matching

SAMPLE_USERLIST = ["john", "dave", "test", "blue", "sky", "green", "red", "z", "tes", "r"]


class TestLunchtimeMatching(unittest.TestCase):

    def test_find_coffeemate_new_user(self):
        store = {
            "USER_LIST": SAMPLE_USERLIST
        }
        result = lunchtime_matching.find_coffeemate(store, "newguy")

        self.assertTrue("newguy" in store)
        self.assertTrue(result in SAMPLE_USERLIST)
        self.assertTrue(len(store["newguy"]["coffee_matches"]) == 1)

    def test_find_coffeemate_existing_user(self):
        original_matchlist = ["dave"]
        store = {
            "USER_LIST": SAMPLE_USERLIST,
            "john": {
                "coffee_matches": [v for v in original_matchlist],
                "lunch_matches": []
            }
        }
        result = lunchtime_matching.find_coffeemate(store, "john")

        self.assertTrue(result not in original_matchlist)
        self.assertTrue(len(store["john"]["coffee_matches"]) == 2)
        
        results = []
        for i in range(10):
            results.append(lunchtime_matching.find_coffeemate(store, "john"))
        
        self.assertTrue(len(store["john"]["coffee_matches"]) == len(SAMPLE_USERLIST) - 1)

    def test_find_coffeemate_full_matchlist(self):
        store = {
            "USER_LIST": SAMPLE_USERLIST,
            "john": {
                "coffee_matches": [s for s in SAMPLE_USERLIST if s != "john"],
                "lunch_matches": []
            }
        }
        result = lunchtime_matching.find_coffeemate(store, "john")

        self.assertTrue(result == "")

    def test_find_lunchmates_new_user(self):
        store = {
            "USER_LIST": SAMPLE_USERLIST
        }
        result = lunchtime_matching.find_lunchmates(store, "newguy")

        self.assertTrue("newguy" in store)
        self.assertTrue(3 <= len(result) <= 5)
        self.assertTrue(len(store["newguy"]["lunch_matches"]) == len(result))

    def test_find_lunchmates_existing_user(self):
        store = {
            "USER_LIST": SAMPLE_USERLIST,
            "john": {
                "coffee_matches": [],
                "lunch_matches": ["dave", "test", "blue"]
            }
        }
        result = lunchtime_matching.find_lunchmates(store, "john")

        self.assertFalse("john" in result)
        self.assertTrue(len(store["john"]["lunch_matches"]) == len(result) + 3)

    def test_find_lunchmates_full_matchlist(self):
        store = {
            "USER_LIST": SAMPLE_USERLIST,
            "john": {
                "coffee_matches": [],
                "lunch_matches": [v for v in SAMPLE_USERLIST]
            }
        }
        result = lunchtime_matching.find_lunchmates(store, "john")
        
        self.assertEqual(len(result), len(store["john"]["lunch_matches"]))


    def test_find_lunchmates_not_enough_users(self):
        store = {
            "USER_LIST": ["john", "dave"],
            "john": {
                "coffee_matches": [],
                "lunch_matches": []
            }
        }
        result = lunchtime_matching.find_lunchmates(store, "john")
        
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
