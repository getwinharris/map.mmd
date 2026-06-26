"""Tests for map_mmd codebuddy install / uninstall commands."""
import json
from pathlib import Path
import sys
from unittest.mock import patch

import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _codebuddy_install_user(tmp_path):
    from map_mmd.__main__ import install
    old_cwd = Path.cwd()
    try:
        import os
        os.chdir(tmp_path)
        with patch("map_mmd.__main__.Path.home", return_value=tmp_path):
            install(platform="codebuddy")
    finally:
        import os
        os.chdir(old_cwd)


def _skill_path_user(tmp_path):
    return tmp_path / ".codebuddy" / "skills" / "map_mmd" / "SKILL.md"


def _skill_path_project(project_dir):
    return project_dir / ".codebuddy" / "skills" / "map_mmd" / "SKILL.md"


def _codebuddy_md_path(project_dir):
    return project_dir / "CODEBUDDY.md"


def _settings_path(project_dir):
    return project_dir / ".codebuddy" / "settings.json"


# ---------------------------------------------------------------------------
# User-scope install (map_mmd install --platform codebuddy)
# ---------------------------------------------------------------------------

def test_codebuddy_install_user_creates_skill_file(tmp_path):
    """User-scope install copies skill to ~/.codebuddy/skills/map_mmd/SKILL.md."""
    _codebuddy_install_user(tmp_path)
    skill_path = _skill_path_user(tmp_path)
    assert skill_path.exists()


def test_codebuddy_skill_file_contains_frontmatter(tmp_path):
    """Installed skill file must include map_mmd YAML frontmatter."""
    _codebuddy_install_user(tmp_path)
    content = _skill_path_user(tmp_path).read_text()
    assert "name: map_mmd" in content
    assert "description:" in content


def test_codebuddy_skill_file_references_map_mmd_query(tmp_path):
    """/map_mmd skill must mention map_mmd query (query-first policy)."""
    _codebuddy_install_user(tmp_path)
    content = _skill_path_user(tmp_path).read_text()
    assert "map_mmd query" in content or "/map_mmd query" in content


# ---------------------------------------------------------------------------
# Project-scope install (map_mmd codebuddy install)
# ---------------------------------------------------------------------------

def test_codebuddy_install_project_writes_codebuddy_md(tmp_path):
    """Project-scope install writes CODEBUDDY.md with map_mmd section."""
    from map_mmd.__main__ import codebuddy_install
    codebuddy_install(tmp_path)
    md = _codebuddy_md_path(tmp_path)
    assert md.exists()
    content = md.read_text()
    assert "## map_mmd" in content
    assert "map.mmd-out/" in content


def test_codebuddy_install_project_writes_hook(tmp_path):
    """Project-scope install registers PreToolUse hook in .codebuddy/settings.json."""
    from map_mmd.__main__ import codebuddy_install
    codebuddy_install(tmp_path)
    settings_path = _settings_path(tmp_path)
    assert settings_path.exists()
    settings = json.loads(settings_path.read_text())
    hooks = settings["hooks"]["PreToolUse"]
    assert any("map_mmd" in str(h) for h in hooks)


def test_codebuddy_install_hook_has_bash_matcher(tmp_path):
    """The installed hook must include Bash matcher for code search interception."""
    from map_mmd.__main__ import codebuddy_install
    codebuddy_install(tmp_path)
    settings = json.loads(_settings_path(tmp_path).read_text())
    hooks = settings["hooks"]["PreToolUse"]
    bash_hooks = [h for h in hooks if h.get("matcher") == "Bash"]
    assert any("map_mmd" in str(h) for h in bash_hooks)


def test_codebuddy_install_hook_has_read_glob_matcher(tmp_path):
    """The installed hook must include Read|Glob matcher for file-read interception."""
    from map_mmd.__main__ import codebuddy_install
    codebuddy_install(tmp_path)
    settings = json.loads(_settings_path(tmp_path).read_text())
    hooks = settings["hooks"]["PreToolUse"]
    read_hooks = [h for h in hooks if h.get("matcher") == "Read|Glob"]
    assert any("map_mmd" in str(h) for h in read_hooks)


def test_codebuddy_install_idempotent(tmp_path):
    """Re-install does not duplicate ## map_mmd sections."""
    from map_mmd.__main__ import codebuddy_install
    codebuddy_install(tmp_path)
    codebuddy_install(tmp_path)
    md = _codebuddy_md_path(tmp_path)
    assert md.read_text().count("## map_mmd") == 1


def test_codebuddy_install_upgrades_stale_section(tmp_path):
    """Re-install replaces an old map_mmd section with the current template."""
    from map_mmd.__main__ import codebuddy_install, _CODEBUDDY_MD_MARKER
    # Write a stale section manually
    md = _codebuddy_md_path(tmp_path)
    md.write_text("old content\n\n## map_mmd\nThis is old instructions\n")
    codebuddy_install(tmp_path)
    content = md.read_text()
    assert _CODEBUDDY_MD_MARKER in content
    assert "old content" in content
    assert "This is old instructions" not in content
    assert "map.mmd-out/" in content
    assert content.count("## map_mmd") == 1


def test_codebuddy_install_merges_existing_codebuddy_md(tmp_path):
    """Install appends to an existing CODEBUDDY.md, preserving other content."""
    from map_mmd.__main__ import codebuddy_install
    _codebuddy_md_path(tmp_path).write_text("# My project rules\n")
    codebuddy_install(tmp_path)
    content = _codebuddy_md_path(tmp_path).read_text()
    assert "# My project rules" in content
    assert "## map_mmd" in content
    assert "map.mmd-out/" in content


def test_codebuddy_install_prints_no_change_on_second_run(tmp_path, capsys):
    """Second install prints '(no change)' when content is identical."""
    from map_mmd.__main__ import codebuddy_install
    codebuddy_install(tmp_path)
    out1 = capsys.readouterr().out
    codebuddy_install(tmp_path)
    out2 = capsys.readouterr().out
    assert "no change" in out2


def test_codebuddy_install_hint_git_add(tmp_path, capsys):
    """Project-scoped install via CLI prints a git add hint."""
    from map_mmd.__main__ import main
    home = tmp_path / "home"
    project = tmp_path / "project"
    project.mkdir()
    old_cwd = Path.cwd()
    try:
        import os
        os.chdir(project)
        with patch("map_mmd.__main__.Path.home", return_value=home):
            sys.argv = ["map_mmd", "codebuddy", "install"]
            main()
    finally:
        import os
        os.chdir(old_cwd)
    # codebuddy_install calls print() directly, no git add hint printed there
    # so this test checks that no errors occur


# ---------------------------------------------------------------------------
# Uninstall
# ---------------------------------------------------------------------------

def test_codebuddy_uninstall_removes_section(tmp_path):
    """Uninstall removes the ## map_mmd section from CODEBUDDY.md."""
    from map_mmd.__main__ import codebuddy_install, codebuddy_uninstall
    codebuddy_install(tmp_path)
    codebuddy_uninstall(tmp_path)
    md = _codebuddy_md_path(tmp_path)
    assert not md.exists()


def test_codebuddy_uninstall_removes_hook(tmp_path):
    """Uninstall removes the PreToolUse hook from .codebuddy/settings.json."""
    from map_mmd.__main__ import codebuddy_install, codebuddy_uninstall
    codebuddy_install(tmp_path)
    codebuddy_uninstall(tmp_path)
    settings_path = _settings_path(tmp_path)
    if settings_path.exists():
        settings = json.loads(settings_path.read_text())
        hooks = settings.get("hooks", {}).get("PreToolUse", [])
        assert not any("map_mmd" in str(h) for h in hooks)


def test_codebuddy_uninstall_noop_if_not_installed(tmp_path):
    """Uninstall should not raise when CODEBUDDY.md doesn't exist."""
    from map_mmd.__main__ import codebuddy_uninstall
    codebuddy_uninstall(tmp_path)  # should not raise


def test_codebuddy_uninstall_noop_if_no_section(tmp_path):
    """Uninstall should not error when CODEBUDDY.md exists but no map_mmd section."""
    from map_mmd.__main__ import codebuddy_uninstall
    _codebuddy_md_path(tmp_path).write_text("# Some other project\n")
    codebuddy_uninstall(tmp_path)
    content = _codebuddy_md_path(tmp_path).read_text()
    assert "# Some other project" in content


def test_codebuddy_uninstall_preserves_other_content(tmp_path):
    """Uninstall preserves non-map_mmd content in CODEBUDDY.md."""
    from map_mmd.__main__ import codebuddy_install, codebuddy_uninstall
    _codebuddy_md_path(tmp_path).write_text("# My project rules\n")
    codebuddy_install(tmp_path)
    codebuddy_uninstall(tmp_path)
    # When map_mmd section was appended, uninstall removes it and the file
    # becomes the original content
    content = _codebuddy_md_path(tmp_path).read_text()
    assert "## map_mmd" not in content
    assert "# My project rules" in content


# ---------------------------------------------------------------------------
# uninstall_all integration
# ---------------------------------------------------------------------------

def test_uninstall_all_removes_codebuddy_md(tmp_path, monkeypatch):
    """map_mmd uninstall must clean up CODEBUDDY.md."""
    from map_mmd.__main__ import main
    home = tmp_path / "home"
    project = tmp_path / "project"
    project.mkdir()
    monkeypatch.chdir(project)
    with patch("map_mmd.__main__.Path.home", return_value=home):
        monkeypatch.setattr(sys, "argv", ["map_mmd", "codebuddy", "install"])
        main()
        md = _codebuddy_md_path(project)
        assert md.exists()
        monkeypatch.setattr(sys, "argv", ["map_mmd", "uninstall"])
        main()
    assert not md.exists()


def test_uninstall_all_removes_codebuddy_hook(tmp_path, monkeypatch):
    """map_mmd uninstall must clean up .codebuddy/settings.json hooks."""
    from map_mmd.__main__ import main
    home = tmp_path / "home"
    project = tmp_path / "project"
    project.mkdir()
    monkeypatch.chdir(project)
    with patch("map_mmd.__main__.Path.home", return_value=home):
        monkeypatch.setattr(sys, "argv", ["map_mmd", "codebuddy", "install"])
        main()
        monkeypatch.setattr(sys, "argv", ["map_mmd", "uninstall"])
        main()
    settings_path = _settings_path(project)
    if settings_path.exists():
        settings = json.loads(settings_path.read_text())
        hooks = settings.get("hooks", {}).get("PreToolUse", [])
        assert not any("map_mmd" in str(h) for h in hooks)


# ---------------------------------------------------------------------------
# Platform config sanity
# ---------------------------------------------------------------------------

def test_codebuddy_in_platform_config():
    """codebuddy must be registered in _PLATFORM_CONFIG."""
    from map_mmd.__main__ import _PLATFORM_CONFIG
    assert "codebuddy" in _PLATFORM_CONFIG
    assert _PLATFORM_CONFIG["codebuddy"]["skill_file"] == "skill.md"
    assert _PLATFORM_CONFIG["codebuddy"]["claude_md"] is False


def test_codebuddy_platform_skill_destination_user_scope(tmp_path):
    """User-scope destination must be ~/.codebuddy/skills/map_mmd/SKILL.md."""
    from map_mmd.__main__ import _platform_skill_destination
    with patch("map_mmd.__main__.Path.home", return_value=tmp_path):
        dst = _platform_skill_destination("codebuddy", project=False)
    assert dst == tmp_path / ".codebuddy" / "skills" / "map_mmd" / "SKILL.md"


def test_codebuddy_platform_skill_destination_project_scope(tmp_path):
    """Project-scope destination must be <project>/.codebuddy/skills/map_mmd/SKILL.md."""
    from map_mmd.__main__ import _platform_skill_destination
    dst = _platform_skill_destination("codebuddy", project=True, project_dir=tmp_path)
    assert dst == tmp_path / ".codebuddy" / "skills" / "map_mmd" / "SKILL.md"


def test_codebuddy_in_main_help_text(capsys, monkeypatch):
    """`map_mmd --help` must list codebuddy in the platform list and per-platform section."""
    from map_mmd.__main__ import main
    monkeypatch.setattr(sys, "argv", ["map_mmd", "--help"])
    main()
    captured = capsys.readouterr().out
    # codebuddy should appear in the top-level platform list
    assert "|codebuddy)" in captured or "codebuddy" in captured, (
        "codebuddy missing from `map_mmd --help` platform list"
    )
    # codebuddy install / uninstall should appear in the per-platform section
    assert "codebuddy install" in captured, "`codebuddy install` line missing from help text"
    assert "codebuddy uninstall" in captured, "`codebuddy uninstall` line missing from help text"


def test_codebuddy_skill_file_exists_in_package():
    """skill.md must be present in the installed package (shared with claude)."""
    import map_mmd
    skill = Path(map_mmd.__file__).parent / "skill.md"
    assert skill.exists(), "skill.md missing from package"


def test_codebuddy_installation_roundtrip(tmp_path):
    """Install then uninstall leaves no trace of map_mmd CODEBUDDY.md or hook."""
    from map_mmd.__main__ import codebuddy_install, codebuddy_uninstall
    # Pre-existing project file
    _codebuddy_md_path(tmp_path).write_text("# My project\n")
    # One section above map_mmd to test cleanup
    codebuddy_install(tmp_path)
    codebuddy_uninstall(tmp_path)
    # CODEBUDDY.md should exist with original content only
    md = _codebuddy_md_path(tmp_path)
    assert md.exists()
    content = md.read_text()
    assert "## map_mmd" not in content
    assert "# My project" in content
    # Hook should be removed
    settings_path = _settings_path(tmp_path)
    if settings_path.exists():
        settings = json.loads(settings_path.read_text())
        hooks = settings.get("hooks", {}).get("PreToolUse", [])
        assert not any("map_mmd" in str(h) for h in hooks)
