import test_circles

if __name__ == "__main__":
    suite = test_circles.unittest.TestLoader().loadTestsFromTestCase(test_circles.TestCircle)
    test_circles.unittest.TextTestRunner(verbosity=2).run(suite)