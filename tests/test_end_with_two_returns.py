import os
import sys
import unittest

import nbformat


sys.path.insert(0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), os.pardir
        )
    )
)


import end_with_two_returns as tr


class TestFile(unittest.TestCase):
    def setUp(self):
        self.fp = open(
            os.path.join(
                os.path.dirname(__file__), 
                'sample.ipynb'
            ), 
            encoding = 'utf-8'
        )
    
        self.nb = nbformat.read(self.fp, nbformat.NO_CONVERT)

        self.fp.seek(0)
    
    def tearDown(self):
        del self.nb
        self.fp.close()

    def test_gen_cells(self):
        for cell in tr.gen_cells(self.fp):
            self.assertIsInstance(cell, nbformat.notebooknode.NotebookNode)

    def test_get_source_from_cell(self):
        cell = self.nb['cells'][0]
        source = tr.get_source_from_cell(cell)
        self.assertIsInstance(source, str)


if "__main__" == __name__:
    unittest.main()
