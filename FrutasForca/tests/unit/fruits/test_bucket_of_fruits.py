import unittest

from app.fruits.bucket_of_fruits import BucketOfFruits


class TestBucketOfFruits(unittest.TestCase):
    def test_if_buckect_is_a_instance_of_bucket_of_fruits(self):
        buck = BucketOfFruits()
        self.assertIsInstance(buck, BucketOfFruits)

    def test_if_get_a_random_fruit_really_return_a_random_fruit(self):
        buck = BucketOfFruits()
        result = buck.get_a_random_fruit()
        assert result in buck.list_of_fruits
