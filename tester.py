#!/usr/bin/python3
import unittest
import time, sys, os
from subprocess import check_output, CalledProcessError
from eulerlib import num

PATH = os.path.realpath(__file__)

class TestEuler(unittest.TestCase):
    testInfo = {} # Keys: name, result, status, time

    def setUp(self):
        self.startTime = time.time()
        self.testInfo['result'] = "NONE"
        self.testInfo['name'] = "NONE"
        self.testInfo['status'] = "NONE"

    def tearDown(self):
        self.testInfo['time'] = time.time() - self.startTime
        print("{name:>12} == {result:>18} {status:>18} {time:>10.3f}s".format(**self.testInfo))
    
    def run_test(self, name, result):
        self.testInfo['name'] = name
        self.testInfo['result'] = result
        try:
            self.testInfo['status'] = "FAILED"
            self.assertEqual(num(check_output(["./" + name + " 2>/dev/null"], shell=True)), result)
            self.testInfo['status'] = "PASSED"
        except NameError:
            self.testInfo['status'] = "NOTFOUND"
        except AttributeError:
            self.testInfo['status'] = "NOTIMPL"
        except CalledProcessError:
            self.testInfo['status'] = "NOTIMPL"
        except Exception as e:
            self.testInfo['status'] = str(e)

    def test_euler001(self):
        self.run_test("euler001.pl",233168)
    def test_euler002(self):
        self.run_test("euler002.pl",4613732)
    def test_euler003(self):
        self.run_test("euler003.pl",6857)
    def test_euler004(self):
        self.run_test("euler004.pl",906609)
    def test_euler005(self):
        self.run_test("euler005.pl",232792560)
    def test_euler006(self):
        self.run_test("euler006.pl",25164150)
    def test_euler007(self):
        self.run_test("euler007.pl",104743)
    def test_euler008(self):
        self.run_test("euler008.pl","BROKEN")
    def test_euler009(self):
        self.run_test("euler009.pl",31875000)
    def test_euler010(self):
        self.run_test("euler010.pl",142913828922)
    def test_euler011(self):
        self.run_test("euler011.py",70600674)
    def test_euler012(self):
        # TODO(eugenek): Make cpp ones work
        self.run_test("euler012","BROKEN")
    def test_euler013(self):
        # TODO(eugenek): Make cpp ones work
        self.run_test("euler013","BROKEN")
    def test_euler014(self):
        # TODO(eugenek): Make cpp ones work
        self.run_test("euler014","BROKEN")
    def test_euler015(self):
        self.run_test("euler015.py",137846528820)
    def test_euler016(self):
        # TODO(eugenek): Make cpp ones work
        self.run_test("euler016","BROKEN")
    def test_euler017(self):
        # TODO(eugenek): Make cpp ones work
        self.run_test("euler017","BROKEN")
    def test_euler018(self):
        self.run_test("euler018", "TODO")
        pass
    def test_euler019(self):
        self.run_test("euler019.py",171)
    def test_euler020(self):
        self.run_test("euler020.py",648)
    def test_euler021(self):
        self.run_test("euler021.py",31626)
    def test_euler022(self):
        self.run_test("euler022.py",871198282)
    def test_euler023(self):
        self.run_test("euler023.py",4179871)
    def test_euler024(self):
        self.run_test("euler024.py",2783915460)
    def test_euler025(self):
        self.run_test("euler025.py",4782)
    def test_euler026(self):
        self.run_test("euler026.py",983)   
    def test_euler027(self):
        self.run_test("euler027.py",-59231)
    def test_euler028(self):
        self.run_test("euler028.py",669171001)
    def test_euler029(self):
        self.run_test("euler029.py",9183) 
    def test_euler030(self):
        self.run_test("euler030.py",443839) 
    # TODO(eugenek): Broken test ATM
    #def test_euler031(self):
    #    self.run_test("euler031.py",73682) 
    def test_euler032(self):
        self.run_test("euler032.py",45228) 
    def test_euler033(self):
        self.run_test("euler033.py",100) 
    def test_euler034(self):
        self.run_test("euler034.py",40730) 
    def test_euler035(self):
        self.run_test("euler035.py",55) 
    def test_euler036(self):
        self.run_test("euler036.py",872187) 
    def test_euler037(self):
        self.run_test("euler037.py",748317) 
    def test_euler038(self):
        self.run_test("euler038.py",932718654) 
    def test_euler039(self):
        self.run_test("euler039.py",840) 
    def test_euler040(self):
        self.run_test("euler040.py",210) 
    def test_euler041(self):
        self.run_test("euler041.py",7652413) 
    def test_euler042(self):
        self.run_test("euler042.py",162) 
    def test_euler043(self):
        self.run_test("euler043.py",16695334890) 
    def test_euler044(self):
        self.run_test("euler044.py",5482660)
    def test_euler045(self):
        self.run_test("euler045.py",1533776805)
    def test_euler046(self):
        pass
    def test_euler047(self):
        pass
    def test_euler048(self):
        pass
    def test_euler049(self):
        pass
    def test_euler050(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEuler)
    unittest.TextTestRunner(verbosity = 0).run(suite)
