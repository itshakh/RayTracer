import unittest
from RtTupple import RtTupple, RtVector, RtPoint
from RtLogger import RtLogger
import numpy as np


class RtTuppleUnitTests(unittest.TestCase):
    logger = RtLogger()

    def test_RtTuppleAsAPoint(self):
        RtTuppleUnitTests.logger.info("start test_RtTuppleAsAPoint... ")
        p1 = RtTupple(0, 0, 0, 1)

        self.assertTrue(p1.is_point())
        self.assertFalse(p1.is_vector())

        RtTuppleUnitTests.logger.info("Finished test_RtTuppleAsAPoint successfully")

    def test_RtTuppleAsAVector(self):
        RtTuppleUnitTests.logger("start test_RtTuppleAsAVector... ")

        v1 = RtTupple(0, 0, 0, 0)

        self.assertTrue(v1.is_vector())
        self.assertFalse(v1.is_point())
        RtTuppleUnitTests.logger.info("Finished test_RtTuppleAsAVector successfully")

    def test_RtCosntructVector(self):
        RtTuppleUnitTests.logger("start test_RtCosntructVector... ")

        v1 = RtVector(4, -4, 3)
        self.assertTrue(v1 == RtTupple(4, -4, 3, 0))
        RtTuppleUnitTests.logger.info("Finished test_RtCosntructVector successfully")

    def test_RtCosntructPoint(self):
        RtTuppleUnitTests.logger("start test_RtCosntructPoint... ")

        p1 = RtPoint(4, -4, 3)
        self.assertTrue(p1 == RtTupple(4, -4, 3, 1))
        RtTuppleUnitTests.logger.info("Finished test_RtCosntructPoint successfully")

    def test_RtTupleOperationsAdd(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsAdd... ")

        # point
        t1 = RtTupple(3, -2, 5, 1)
        # vector
        t2 = RtTupple(-2, 3, 1, 0)

        self.assertTrue(t1 + t2 == RtTupple(1, 1, 6, 1),
                        "RtTupple(3, -2, 5, 1) + RtTupple(-2, 3, 1, 0) != RtTupple(1, 1, 6, 1)")

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsAdd successfully")

    def test_RtTupleOperationsSubPoints(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsSubPoints... ")

        # point
        t1 = RtPoint(3, 2, 1)
        # vector
        t2 = RtPoint(5, 6, 7)

        self.assertTrue(t1 - t2 == RtVector(-2, -4, -6),
                        "RtPoint(3, 2, 1) - RtTupple(5, 6, 7) == RtVector(-2, -4, -6)")

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsSubPoints successfully")

    def test_RtTupleOperationsSubVectors(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsSubVectors... ")

        # point
        t1 = RtVector(3, 2, 1)
        # vector
        t2 = RtVector(5, 6, 7)

        self.assertTrue(t1 - t2 == RtVector(-2, -4, -6),
                        "RtPoint(3, 2, 1) - RtTupple(5, 6, 7) == RtVector(-2, -4, -6)")

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsSubVectors successfully")

    def test_RtTupleOperationsNegateVectors(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsNegateVectors... ")

        # point
        t1 = RtVector(0, 0, 0)
        # vector
        t2 = RtVector(1, -2, 3)

        self.assertTrue(t1 - t2 == RtVector(-1, 2, -3),
                        "RtVector(0, 0, 0) - RtVector(1, -2, 3) == RtVector(-1, 2, -3)")

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsNegateVectors successfully")

    def test_RtTupleOperationsNegateTupples(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsNegateTupples... ")

        t1 = RtTupple(1, -2, 3, -4)
        t2 = -t1

        self.assertTrue(t2 == RtTupple(-1, 2, -3, 4),
                        "-RtTupple(1, -2, 3, -4) == RtTupple(-1, 2, 3, 4)")

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsNegateTupples successfully")

    def test_RtTupleOperationsMultTupplesByScalar(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsMultTupplesByScalar... ")

        t1 = RtTupple(1, -2, 3, -4)
        t2 = t1 * 3.5

        self.assertTrue(t2 == RtTupple(3.5, -7, 10.5, -14),
                        "RtTupple(1, -2, 3, -4) * 3.5 == RtTupple(3.5, -7, 10.5, -14)")

        t2 = t1 * 0.5
        self.assertTrue(t2 == RtTupple(0.5, -1, 1.5, -2),
                        "RtTupple(1, -2, 3, -4) * 0.5 == RtTupple(0.5, -1, 1.5, -2)")

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsMultTupplesByScalar successfully")

    def test_RtTupleOperationsDivTupplesByScalar(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsDivTupplesByScalar... ")

        t1 = RtTupple(1, -2, 3, -4)
        t2 = t1 / 2

        self.assertTrue(t2 == RtTupple(0.5, -1, 1.5, -2),
                        "RtTupple(1, -2, 3, -4) / 2 == RtTupple(0.5, -1, 1.5, -2)")

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsDivTupplesByScalar successfully")

    def test_RtTupleOperationsVectorMagnitude(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsVectorMagnitude... ")

        t1 = RtVector(1, 0, 0)
        t2 = RtVector(0, 1, 0)
        t3 = RtVector(0, 0, 1)
        t4 = RtVector(1, 2, 3)
        t5 = RtVector(-1, -2, -3)

        self.assertEqual(t1.magnitude(), 1)
        self.assertEqual(t2.magnitude(), 1)
        self.assertEqual(t3.magnitude(), 1)
        self.assertEqual(t4.magnitude(), np.sqrt(14))
        self.assertEqual(t5.magnitude(), np.sqrt(14))

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsVectorMagnitude successfully")

    def test_RtTupleOperationsVectorNormalize(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsVectorNormalize... ")

        t1 = RtVector(4, 0, 0)
        t2 = RtVector(1, 2, 3)

        self.assertEqual(t1.normalize(), RtVector(1, 0, 0))
        self.assertEqual(t2.normalize(), RtVector(1 / np.sqrt(14), 2 / np.sqrt(14),3 / np.sqrt(14)))
        self.assertEqual(t2.normalize().magnitude(), 1)

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsVectorNormalize successfully")

    def test_RtTupleOperationsVectorDotProduct(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsVectorDotProduct... ")

        t1 = RtVector(1, 2, 3)
        t2 = RtVector(2, 3, 4)

        self.assertEqual(t1.dot(t2), 20)

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsVectorDotProduct successfully")

    def test_RtTupleOperationsVectorCrossProduct(self):
        RtTuppleUnitTests.logger("start test_RtTupleOperationsVectorCrossProduct... ")

        t1 = RtVector(1, 2, 3)
        t2 = RtVector(2, 3, 4)

        self.assertEqual(t1.cross(t2), RtVector(-1, 2, -1))
        self.assertEqual(t2.cross(t1), RtVector(1, -2, 1))

        RtTuppleUnitTests.logger.info("Finished test_RtTupleOperationsVectorCrossProduct successfully")


if __name__ == '__main__':
    unittest.main()
