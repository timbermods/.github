#!/usr/bin/env python3
"""What a timbermods mod repo does when a release becomes GitHub's **Latest**: fixed, mechanical updates only.

1. Release notes: append the standard footer once (install line, website and install-guide links, the zip's SHA-256).
   Parts your notes already have are left out (an Install heading, the checksum).
2. Website: set the release.js fallback text (`data-release="version|tag|asset-name"`) in <site-dir>/**/*.html to
   the new release. Empty fallbacks stay empty. Prose and `data-release-pinned` blocks are never touched.
3. README.md: on lines that end with `<!-- latest -->`, replace the previous Latest version with the new one.
4. If anything changed: run the site checks (local links resolve, site scripts parse, the repo's own test command).
   Pass: commit to the default branch and ask Pages to rebuild. Fail: change nothing, open an issue, exit 1.

Pre-releases, drafts and a release that isn't GitHub's Latest do nothing. Run by the shared workflow
.github/workflows/latest-release.yml; for a local dry run:

    python latest_release.py --repo timbermods/MixedStorage --site-url https://timbermods.github.io/MixedStorage/ \\
        --asset-pattern '^MixedStorage-v[\\d.]+\\.zip$' --dry-run            (needs the gh CLI, signed in)
"""
import argparse, hashlib, json, os, pathlib, re, shutil, subprocess, sys, tempfile

FOOTER_MARK = "<!-- timbermods:release-footer -->"
README_MARK = "<!-- latest -->"


def run(cmd, check=True, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)
    if check and r.returncode:
        raise RuntimeError(f"{' '.join(cmd)} failed:\n{r.stdout}\n{r.stderr}")
    return r


def api(path, method="GET", body=None):
    cmd = ["gh", "api", path, "-H", "Accept: application/vnd.github+json"]
    if method != "GET":
        cmd += ["-X", method]
    if body is not None:
        cmd += ["--input", "-"]
    r = run(cmd, input=json.dumps(body) if body is not None else None)
    return json.loads(r.stdout) if r.stdout.strip() else None


def read(path):
    """The file as it is, line endings included (CRLF files stay CRLF)."""
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def version_of(tag):
    return tag[1:] if re.match(r"v\d", tag) else tag


# ---------------------------------------------------------------- 1. the release-notes footer
def footer(release, asset, sha, site_url, install_url):
    body = release.get("body") or ""
    if FOOTER_MARK in body:
        return None
    lines = ["", "---", FOOTER_MARK]
    if not re.search(r"(?im)^#+\s*install", body):
        name = f"`{asset['name']}`" if asset else "the mod's zip"
        lines.append(f"**Install:** download {name} below (under Assets, not \"Source code\"), close Timberborn, extract it into "
                     f"`Documents\\Timberborn\\Mods`, then enable the mod in the game's mod manager. "
                     f"Step by step: [install guide]({install_url}).")
        lines.append("")
    links = f"**Website:** {site_url}"
    if asset and sha and sha.lower() not in body.lower():
        links += f" · **SHA-256** of `{asset['name']}`: `{sha}`"
    lines.append(links)
    return body.rstrip() + "\n" + "\n".join(lines) + "\n"


def sha256_of(repo, tag, asset):
    d = tempfile.mkdtemp()
    try:
        run(["gh", "release", "download", tag, "-R", repo, "-p", asset["name"], "-D", d])
        h = hashlib.sha256()
        with open(os.path.join(d, asset["name"]), "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        return h.hexdigest()
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ---------------------------------------------------------------- 2. the site's release.js fallbacks
FALLBACK = re.compile(r'(<[^>]*\bdata-release="(version|tag|asset-name)"[^>]*>)([^<]*)(<)')


def bump_site(site_dir, tag, asset):
    new = {"version": version_of(tag), "tag": tag, "asset-name": asset["name"] if asset else None}
    changed = []
    for f in sorted(pathlib.Path(site_dir).rglob("*.html")):
        text = read(f)

        def sub(m):
            value = new[m.group(2)]
            if not m.group(3).strip() or value is None:   # an empty fallback is deliberate: release.js alone fills it
                return m.group(0)
            return m.group(1) + value + m.group(4)

        out = FALLBACK.sub(sub, text)
        if out != text:
            write(f, out)
            changed.append(str(f))
    return changed


# ---------------------------------------------------------------- 3. README lines marked <!-- latest -->
def bump_readme(prev_tag, tag):
    p = pathlib.Path("README.md")
    if not p.exists() or not prev_tag or prev_tag == tag:
        return [], []
    old_v, new_v = version_of(prev_tag), version_of(tag)
    word = re.compile(r"(?<![\d.])" + re.escape(old_v) + r"(?![\w]|\.\d)")
    text = read(p)
    lines, missed = [], []
    for i, line in enumerate(text.split("\n")):
        if README_MARK in line:
            new_line = word.sub(new_v, line)
            if new_line == line:
                missed.append(i + 1)
            line = new_line
        lines.append(line)
    out = "\n".join(lines)
    if out != text:
        write(p, out)
        return ["README.md"], missed
    return [], missed


# ---------------------------------------------------------------- 4. checks
def check_site(site_dir, repo, test_command):
    problems = []
    root = pathlib.Path(site_dir)
    prefix = "/" + repo.split("/")[1] + "/"
    for f in root.rglob("*.html"):
        for ref in re.findall(r'(?<![\w-])(?:href|src)="([^"]+)"', f.read_text(encoding="utf-8")):
            if re.match(r"[a-z][a-z0-9+.-]*:|#|//", ref, re.I):
                continue
            path = ref.split("#")[0].split("?")[0]
            if not path:
                continue
            if path.startswith(prefix):
                target = root / path[len(prefix):]
            elif path.startswith("/"):
                continue
            else:
                target = f.parent / path
            if path.endswith("/"):
                target = target / "index.html"
            if not target.exists():
                problems.append(f"{f}: {ref} does not exist")
    if shutil.which("node"):
        for js in root.rglob("*.js"):
            r = run(["node", "--check", str(js)], check=False)
            if r.returncode:
                problems.append(f"{js} does not parse:\n{r.stderr.strip()}")
    if test_command:
        r = run(["bash", "-c", test_command], check=False)
        if r.returncode:
            problems.append(f"`{test_command}` failed:\n{(r.stdout + r.stderr).strip()[-3000:]}")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--tag", default="", help="the release just published; empty = GitHub's current Latest")
    ap.add_argument("--site-dir", default="docs")
    ap.add_argument("--site-url", required=True)
    ap.add_argument("--install-page", default="install.html")
    ap.add_argument("--asset-pattern", required=True)
    ap.add_argument("--test-command", default="")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    try:
        latest = api(f"repos/{a.repo}/releases/latest")["tag_name"]
    except RuntimeError:
        print("This repository has no Latest release (only pre-releases or drafts). Nothing to do.")
        return 0
    tag = a.tag or latest
    if tag != latest:
        print(f"{tag} is not GitHub's Latest release ({latest} is). Nothing to do.")
        return 0

    release = api(f"repos/{a.repo}/releases/tags/{tag}")
    pattern = re.compile(a.asset_pattern)
    asset = next((x for x in release.get("assets", []) if pattern.search(x["name"])), None)
    others = [r for r in api(f"repos/{a.repo}/releases?per_page=50")
              if not r["draft"] and not r["prerelease"] and r["tag_name"] != tag and r.get("published_at")]
    prev_tag = max(others, key=lambda r: r["published_at"])["tag_name"] if others else None
    site_url = a.site_url if a.site_url.endswith("/") else a.site_url + "/"
    install_url = site_url + a.install_page if a.install_page else site_url
    print(f"Latest release {tag} (previous Latest: {prev_tag or 'none'}); zip: {asset['name'] if asset else 'none found'}")

    # 1. release notes
    sha = sha256_of(a.repo, tag, asset) if asset else None
    new_body = footer(release, asset, sha, site_url, install_url)
    if new_body is None:
        print("Release notes already carry the footer.")
    elif a.dry_run:
        print("Would append to the release notes:\n" + new_body[len((release.get('body') or '').rstrip()):])
    else:
        api(f"repos/{a.repo}/releases/{release['id']}", "PATCH", {"body": new_body})
        print("Appended the footer to the release notes.")

    # 2 and 3. site and README
    changed = bump_site(a.site_dir, tag, asset) if os.path.isdir(a.site_dir) else []
    readme, missed = bump_readme(prev_tag, tag)
    changed += readme
    if missed:
        print(f"README lines marked {README_MARK} without {prev_tag} in them (left as they are): {missed}")
    if not changed:
        print("The site and README already show this release.")
        return 0
    print("Updated: " + ", ".join(changed))
    print(run(["git", "diff", "--stat"]).stdout)

    # 4. checks, then commit
    problems = check_site(a.site_dir, a.repo, a.test_command) if os.path.isdir(a.site_dir) else []
    if problems:
        report = "\n\n".join(problems)
        print("Checks failed; nothing is committed.\n" + report)
        if not a.dry_run:
            run(["git", "checkout", "--", "."])
            run(["gh", "issue", "create", "-R", a.repo, "--title", f"Latest release {tag}: the site's version update failed its checks",
                 "--body", f"The Latest-release workflow tried to update the version text for {tag} and the checks failed, so nothing was "
                           f"committed. Update it by hand (see CLAUDE.md), or fix the checks and re-run the workflow.\n\n```\n{report[:60000]}\n```"])
        return 1
    if a.dry_run:
        print(run(["git", "diff"]).stdout)
        run(["git", "checkout", "--", "."])
        print("Dry run: nothing committed.")
        return 0
    run(["git", "config", "user.name", "github-actions[bot]"])
    run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
    run(["git", "add", "--", *changed])
    run(["git", "commit", "-m", f"Latest release {tag}: version text on the site and README\n\nUpdated by the Latest-release workflow."])
    run(["git", "push"])
    print(f"Committed and pushed: {', '.join(changed)}")
    run(["gh", "api", "-X", "POST", f"repos/{a.repo}/pages/builds"], check=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
