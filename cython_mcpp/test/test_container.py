import unittest, container_unit_tests, os

class EmplaceTest(unittest.TestCase):
    def test_emplace_object_move_vector(self):
        x=container_unit_tests.run_emplace_object_move_vector()
        self.assertEqual(x['size'],1)
        self.assertEqual(x['first'],2)
        self.assertEqual(x['second'],4)
    def test_emplace_object_move_map(self):
        x=container_unit_tests.run_emplace_object_move_map()
        self.assertEqual(x['size'],1)
        self.assertEqual(x['first'],2)
        self.assertEqual(x['second'],4)
    def test_emplace_move_vector(self):
        x=container_unit_tests.run_emplace_move_vector()
        self.assertEqual(x['size'],1)
        self.assertEqual(x['first'],2)
        self.assertEqual(x['second'],4)
    def test_emplace_vector_unique_ptr(self):
        x=container_unit_tests.run_emplace_vector_unique_ptr()
        self.assertEqual(x['size'],1)
        self.assertEqual(x['first'],2)
        self.assertEqual(x['second'],4)
    def test_emplace_vector(self):
        x=container_unit_tests.run_emplace_vector()
        self.assertEqual(x['size'],1)
        self.assertEqual(x['first'],2)
        self.assertEqual(x['second'],4)

class PushBackTest(unittest.TestCase):
    def test_push_back_move_vector(self):
        x=container_unit_tests.run_push_back_move_vector()
        self.assertEqual(x['size'],1)
        self.assertEqual(x['first'],2)
        self.assertEqual(x['second'],4)

