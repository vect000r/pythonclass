import test_points

if __name__ == '__main__':
    suite = test_points.unittest.TestLoader().loadTestsFromTestCase(test_points.TestPoints)
    test_points.unittest.TextTestRunner(verbosity=2).run(suite)