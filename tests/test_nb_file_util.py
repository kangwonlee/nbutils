import os
import unittest

import nb_file_util as nbutils

null = dir(nbutils)


class TestNotebookFileUtil(unittest.TestCase):
    def setUp(self):
        self.input_file_name = os.path.join('tests', 'sample.ipynb')
        self.file_processor = nbutils.FileProcessor(self.input_file_name)

    def test_use_default_filename_if_missing(self):
        self.assertTrue(os.path.exists(self.file_processor.use_default_filename_if_missing(None)))

    def test_sample_ipynb(self):
        # should run without an exception
        self.file_processor.execute()

    def test_read_notebook(self):
        result = self.file_processor.read_file()
        self.assertIn('cells', result)
        self.assertIn('nbformat', result)
        self.assertIn('nbformat_minor', result)

    def test_is_ignore(self):
        ignore_these = ('__pycache__', '.ipynb_checkpoints', '.git', '.cache', '.idea', 'nbutils', 'tests', '.vscode')
        for ig in ignore_these:
            self.assertTrue(nbutils.is_ignore(ig), msg=f"arg = {ig}")

        do_not_ignore_these = ('01', '02', 'ch02', )
        for dont_ig in do_not_ignore_these:
            self.assertFalse(nbutils.is_ignore(dont_ig), msg=f"arg = {dont_ig}")


if __name__ == '__main__':
    unittest.main()
    # finished running
