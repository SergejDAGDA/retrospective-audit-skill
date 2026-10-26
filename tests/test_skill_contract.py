"""Focused contract checks for the retrospective audit Skill ID migration."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "retrospective-audit"


class RetrospectiveAuditIdentityTests(unittest.TestCase):
    def test_canonical_id_and_directory(self):
        self.assertTrue((SKILL / "SKILL.md").is_file())
        self.assertEqual((SKILL / "VERSION").read_text(encoding="utf-8").strip(), "0.2.0")
        self.assertFalse((ROOT / "skills" / "retrospective-skill-audit").exists())
        source = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(source.startswith("---\nname: retrospective-audit\n"))
        self.assertIn("Work read-only until the user explicitly approves edits", source)
        self.assertIn("Do not apply it", source)

    def test_entrypoint_and_usage_are_consistent(self):
        metadata = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Retrospective Audit"', metadata)
        self.assertIn("Use $retrospective-audit", metadata)
        for filename in ("README.md", "README.ru.md"):
            readme = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("$retrospective-audit", readme)
            self.assertIn("retrospective-audit-skill", readme)
        self.assertTrue((SKILL / "references" / "report-template.md").is_file())


if __name__ == "__main__":
    unittest.main()
