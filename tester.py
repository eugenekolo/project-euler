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
        print("{name:>12}   {result:>18} {status:>18} {time:>10.3f}s".format(**self.testInfo))
    
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
        self.run_test("euler008.pl",23514624000) 
    def test_euler009(self):
        self.run_test("euler009.pl",31875000)
    def test_euler010(self):
        self.run_test("euler010.pl",142913828922)
    def test_euler011(self):
        self.run_test("euler011.pl",70600674)
    def test_euler012(self):
        self.run_test("euler012.elf",76576500)
    def test_euler013(self):
        self.run_test("euler013.elf",5537376230)
    def test_euler014(self):
        self.run_test("euler014.elf",837799)
    def test_euler015(self):
        self.run_test("euler015.py",137846528820)
    def test_euler016(self):
        self.run_test("euler016.elf",1366)
    def test_euler017(self):
        self.run_test("euler017.elf",21124)
    def test_euler018(self):
        self.run_test("euler018.xx", "TODO")
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
    def test_euler031(self):
        self.run_test("euler031.py","BROKEN") 
    def test_euler032(self):
        self.run_test("euler032.py",45228) 
    def test_euler033(self):
        self.run_test("euler033.py","TODO") 
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
        self.run_test("euler043.py","TODO") 
    def test_euler044(self):
        self.run_test("euler044.py","TODO")
    def test_euler045(self):
        self.run_test("euler045.py",1533776805)
    def test_euler046(self):
        self.run_test("euler046.py",5777)
    def test_euler047(self):
        self.run_test("euler047.py",134043)
    def test_euler048(self):
        self.run_test("euler048.py",9110846700)
    def test_euler049(self):
        self.run_test("euler049.py",296962999629)
    def test_euler050(self):
        self.run_test("euler050.py","WRONG_ANSWER")

    ## These are out of order and random...
    def test_euler100(self):
        self.run_test("euler100.py","TODO")
    def test_euler152(self):
        self.run_test("euler152.pl","BROKEN")
    def test_euler205(self):
        self.run_test("euler205.py",0.5731441)
    def test_euler206(self):
        self.run_test("euler206.py",1389019170)

if __name__ == '__main__':
    testHeader = {"name":"name", "result":"expected result", "status":"status", "time":"time"}
    print("{name:>12}   {result:>18} {status:>18} {time:>10}".format(**testHeader))
    testHeader = {"name":"----", "result":"---------------", "status":"------", "time":"----"}
    print("{name:>12}   {result:>18} {status:>18} {time:>10}".format(**testHeader))
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEuler)
    unittest.TextTestRunner(verbosity = 0).run(suite)
