import unittest
from RtTupple import RtTupple as Rtt
import logging

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger("tests logger")

class RtTuppleUnitTests(unittest.TestCase):
    def test_RtTuppleAsAPoint(self):
        logger.debug("start test_RtTuppleAsAPoint... ")

        p1 = Rtt.RtTupple(0, 0, 0, 1)

        self.assertTrue(p1.isPoint())
        self.assertFalse(p1.isVector())

        logger.debug("end test_RtTuppleAsAPoint... ")

    def test_RtTuppleAsAVector(self):

        v1 = Rtt.RtTupple(0, 0, 0, 0)

        self.assertTrue(v1.isVector())
        self.assertFalse(v1.isPoint())


if __name__ == '__main__':
    unittest.main()
