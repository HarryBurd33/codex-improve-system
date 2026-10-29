"""Static distribution checks; these do not establish model behavior."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'improve-system'

class PackageTests(unittest.TestCase):
    def test_manifest_discovery_fields(self):
        text = (SKILL / 'SKILL.md').read_text()
        self.assertTrue(text.startswith('---\n'))
        front = text.split('---', 2)[1]
        name = re.search(r'^name:\s*[\"\']?([a-z0-9-]+)', front, re.M).group(1)
        self.assertEqual(name, SKILL.name)
        self.assertLessEqual(len(name), 64)
        description = re.search(r'^description:\s*(.+)', front, re.M).group(1)
        self.assertTrue(1 <= len(description) <= 1024)

    def test_relative_links_resolve_within_distribution(self):
        for file in ROOT.rglob('*.md'):
            if any(p.startswith('.') for p in file.relative_to(ROOT).parts):
                continue
            for link in re.findall(r'\]\(([^)]+)\)', file.read_text()):
                if '://' in link or link.startswith('#'):
                    continue
                path = (file.parent / link.split('#')[0]).resolve()
                self.assertTrue(path.is_relative_to(ROOT), (file, link))
                self.assertTrue(path.exists(), (file, link))

    def test_skill_has_no_builder_dependency_or_personal_absolute_path(self):
        for file in SKILL.rglob('*'):
            if file.is_file():
                content = file.read_text()
                self.assertNotRegex(content, r'/Users/[^/\s]+|[A-Z]:\\Users\\')
                self.assertNotIn('/.agents/skills/skill-forge', content)

    def test_no_private_or_generated_artifacts_in_public_tree(self):
        bad = {'.env', '.DS_Store', 'auth.json', 'credentials.json', 'session.json', 'input.json', 'automatic-stop.json'}
        for file in ROOT.rglob('*'):
            rel = file.relative_to(ROOT)
            if any(p in {'.git', '.checkpoint', '__pycache__', '.private', 'dist'} for p in rel.parts):
                continue
            self.assertFalse(file.is_symlink(), rel)
            self.assertNotIn(file.name, bad)
            self.assertNotIn('transcripts', rel.parts)

    def test_case_contract_is_well_formed_and_discriminating(self):
        data = json.loads((ROOT / 'tests/cases.json').read_text())
        cases = data['cases']
        ids = [x['id'] for x in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(x['input'] and x['expected'] for x in cases))
        self.assertTrue(set('S%02d' % x for x in range(1, 10)).issubset(ids))
        self.assertGreaterEqual(len(data['critical_failures']), 4)

    def test_record_template_is_valid_json(self):
        value = json.loads((SKILL / 'templates/record.json').read_text())
        self.assertIsInstance(value, dict)
        self.assertTrue(value)

if __name__ == '__main__':
    unittest.main()
