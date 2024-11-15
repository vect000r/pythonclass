import test_rectangles

if __name__ == "__main__":
    suite = test_rectangles.unittest.TestLoader().loadTestsFromTestCase(test_rectangles.TestRectangle)
    test_rectangles.unittest.TextTestRunner(verbosity=2).run(suite)