"""Execute Git's documented inverse three-way merge on synthetic files.

This checks the rollback primitive, not an agent's compliance or a transaction engine.
"""
import shutil
import subprocess
import tempfile
from pathlib import Path
import unittest

@unittest.skipUnless(shutil.which('git'), 'optional Git merge primitive unavailable')
class RollbackPrimitiveTests(unittest.TestCase):
    def merge(self, before, applied, current):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            for name, content in [('before', before), ('applied', applied), ('current', current)]:
                (p / name).write_text(content)
            result = subprocess.run(['git', 'merge-file', '-p', str(p/'current'), str(p/'applied'), str(p/'before')], capture_output=True, text=True)
            self.assertEqual((p/'current').read_text(), current, 'Preview must not overwrite current file')
            return result

    def test_inverse_merge_preserves_unrelated_edit(self):
        before = '# Instructions\n\nUse existing checks.\n\n## Notes\nOriginal note.\n'
        applied = before.replace('Use existing checks.', 'Run export verification before delivery.')
        current = applied.replace('Original note.', 'User added a separate note.')
        result = self.merge(before, applied, current)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, before.replace('Original note.', 'User added a separate note.'))

    def test_same_line_conflict_is_not_success(self):
        result = self.merge('Use checks.\n', 'Run export checks.\n', 'User replaced this line independently.\n')
        self.assertEqual(result.returncode, 1)
        self.assertIn('<<<<<<<', result.stdout)

if __name__ == '__main__':
    unittest.main()
