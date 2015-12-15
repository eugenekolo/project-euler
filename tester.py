#!/usr/bin/python3
import unittest, subprocess, time
import glob, importlib, sys, os
import eulerlib

stdout = eulerlib.stdoutToggle()
stdout.off()
for solution in [solution.strip('.py') for solution in glob.glob('euler[0-9]*.py')]:
    mymodule = importlib.import_module(solution)
    globals().update({solution:mymodule})
stdout.on()

class TestEuler(unittest.TestCase):
    testInfo = {} # Keys: name, result, status, time

    def setUp(self):
        self.startTime = time.time()
    
    def tearDown(self):
        self.testInfo['time'] = time.time() - self.startTime
        print("{name:>12} == {result:>18} {status:>18} {time:>10.3f}s".format(**self.testInfo))
    
    def run_test(self, name, result):
        self.testInfo['name'] = name
        self.testInfo['result'] = result
        try:
            self.testInfo['status'] = "FAILED"
            self.assertEqual(eval(name).solve(),result)
            self.testInfo['status'] = "PASSED"
        except NameError:
            self.testInfo['status'] = "NOTFOUND"
        except AttributeError:
            self.testInfo['status'] = "NOTIMPL"
        except Exception as e:
            self.testInfo['status'] = str(e)
        
    #[Todo] Get this working with non-py scripts
    #def test_euler001(self):
    #    print("Testing euler001 == 233168 ... ",end="")
    #    self.assertEqual(int(subprocess.check_output(['perl', 'euler001.pl'])), 233168)
    #    print("passed\n")
    def test_euler015(self):
        self.run_test("euler015",137846528820)
    def test_euler019(self):
        self.run_test("euler019",171)
    def test_euler020(self):
        self.run_test("euler020",648)
    def test_euler021(self):
        self.run_test("euler021",31626)
    def test_euler022(self):
        self.run_test("euler022",871198282)
    def test_euler023(self):
        self.run_test("euler023",4179871)
    def test_euler024(self):
        self.run_test("euler024",2783915460)
    def test_euler025(self):
        self.run_test("euler025",4782)
    def test_euler026(self):
        self.run_test("euler026",983)   
    def test_euler027(self):
        self.run_test("euler027",-59231)
    def test_euler028(self):
        self.run_test("euler028",669171001)
    def test_euler029(self):
        self.run_test("euler029",9183) 
    def test_euler030(self):
        self.run_test("euler030",443839) 
    # TODO(eugenek): Broken test ATM
    #def test_euler031(self):
    #    self.run_test("euler031",73682) 
    def test_euler032(self):
        self.run_test("euler032",45228) 
    def test_euler033(self):
        self.run_test("euler033",100) 
    def test_euler034(self):
        self.run_test("euler034",40730) 
    def test_euler035(self):
        self.run_test("euler035",55) 
    def test_euler036(self):
        self.run_test("euler036",872187) 
    def test_euler037(self):
        self.run_test("euler037",748317) 
    def test_euler038(self):
        self.run_test("euler038",932718654) 
    def test_euler039(self):
        self.run_test("euler039",840) 
    def test_euler040(self):
        self.run_test("euler040",210) 
    def test_euler041(self):
        self.run_test("euler041",7652413) 
    def test_euler042(self):
        self.run_test("euler042",162) 
    def test_euler043(self):
        self.run_test("euler043",16695334890) 
    def test_euler044(self):
        self.run_test("euler044",5482660)
    def test_euler045(self):
        self.run_test("euler045",1533776805)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEuler)
    unittest.TextTestRunner(verbosity = 0).run(suite)
