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

    def test_is_ipynb(self):
        ipynb_set = {'ex05.002.numpy_sympy.BendingStress.T.section_simple.overhang_w.p.ipynb', 'ex06.008.sympy.moment_area.cantilever.w.P.ipynb', 'ch06.004.numpy.moment_area.ipynb', 'ex02.002.numpy.varying.width.ipynb', 'ex05.007.numpy_sympy.ShearStress.H.beam.v.ipynb', 'ch03.003.thin.wall.tube.ipynb', 'ex08.002.numpy_sympy.Offset_Tension.ipynb', 'ch08.006.numpy.Mohrs.Circle.ipynb', 'ex05.005.sympy.BendingStress.lightest.section_W_simple_v.ipynb', 'ex03.001.numpy_sympy.torsional.displacement.ipynb', 'ex06.002.numpy.Direct.Integration_simple_w.ipynb', 'ex06.005.numpy.bracket_EI_simple_v.ipynb', 'ch12.004.numpy.Theories.of.Failure_b.Ductile.Material.ipynb', 'ex05.011.sympy.Shear.Bearing.Stress_girder.section_fastener.ipynb', 'ex08.001.sympy.Pressure_vessle.ipynb', 'ex04.006.numpy.area_simple_v.w.ipynb', 'ex05.001.numpy.BendingStress.BMD_rect_simple_w.p.ipynb', 'ex04.002.numpy.simply.supported_m.only.ipynb', 'ex07.001.sympy.Double.Integral_fix_simple_w.ipynb', 'ex10.001.sympy.Column.W.Section.ipynb', 'ch06.000.sympy.Dirac.delta_Step.ipynb', 'ex08.008.sympy.Abs.Max.Tau_3D.ipynb', 'ex05.004.numpy_sympy.BendingStress.W200.section_cantilever_m.ipynb', 'ex07.003.numpy.Double.Integral_bracket_fix_simple_v.ipynb', 'ex05.003.numpy_sympy.BendingStress.rect.two.h_cantilever_v.ipynb', 'pr05.062.numpy_sympy.ShearStress.H.beam.ipynb', 'ex07.008.sympy.Superposition_fix_simple_w.ipynb', 'ex03.007.numpy_sympy.thin.wall.tube.ipynb', 'ch08.010.sympy.Strain.Rosette.ipynb', 'ex04.005.numpy.area_simple_v.m.ipynb', 'ch08.005.numpy_sympy.2D.Stress.Transform.ipynb', 'ex03.000.numpy.radian.degree.ipynb', 'ex06.001.sympy.W200_cantilever_w.ipynb', 'ch05.004.sympy.ShearStressBeam.ipynb', 'ch05.002.numpy.BendingStress.ipynb', 'ex06.011.sympy.Method.of.Superposition_simple_p.ipynb', 'ex03.006.sympy.thin.wall.tube.ipynb', 'ex08.004.sympy.Stress_Transform.ipynb', 'ch08.009.Strain.Transform.ipynb', 'ex07.005.sympy.Moment.Area_fix_simple_w.ipynb', 'ex04.001.numpy.simply.supported_v_numerical.arrows.ipynb', 'ex02.011.eq.thermal.stress.ipynb', 'ex05.010.numpy.Bending.Shear.Stress_box.section_overhang_v.ipynb', 'ex05.006.numpy_sympy.ShearStress.rect.section_simple_w.ipynb', 'ex02.007.numpy.reinforced.concrete.column.ipynb', 'ex04.003.numpy.simply.supported_v.w.ipynb', 'ch04.004.sympy.SFD.BMD.area.ipynb', 'ex03.002.numpy_sympy.statically.indeterminate.ipynb', 'ex07.003.sympy.Superposition_bracket_fix_simple_v.ipynb', 'ex08.007.numpy_sympy.Mohr.Circle.ipynb', 'ex07.004.numpy_sympy.Double.Integral_bracket_fix_fix_w.ipynb', 'ch10.002.numpy_sympy.Euler.Equation_for_a.Column.ipynb', 'ch05.000.sympy.Second.Moment.Of.Inertia.ipynb', 'ex05.009.sympy.Bending.Shear.Stress_max.length_rect_simple_w.ipynb'}

        for file_name in ipynb_set:
            self.assertTrue(nbutils.is_ipynb(file_name), msg=f"arg = {file_name}")

        other_set = {'find_in_notebook_files.py', 'environment.3.5.yml', 'README.md', 'environment.nightly.yml', 'tests/', '__pycache__/', 'nbutils/', 'test_nb.py', 'bending_stress_05_002.png', 'environment.3.6.yml', '__init__.py', 'draw_diagrams.py', 'recursively_convert_units.py', 'numpy_sympy.py'}

        for file_name in other_set:
            self.assertFalse(nbutils.is_ipynb(file_name), msg=f"arg = {file_name}")


if __name__ == '__main__':
    unittest.main()
    # finished running
