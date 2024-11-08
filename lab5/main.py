import test_fracs

if __name__ == "__main__":
    suite = test_fracs.unittest.TestLoader().loadTestsFromTestCase(test_fracs.TestFractions)
    test_fracs.unittest.TextTestRunner(verbosity=2).run(suite)