# Restart: how a new session of me takes over

1. Read the brief (link in agent.json), then now.md and role.md here.
2. Read CLAUDE.md and README.md at the repository root; run: bash tools/setup-signing.sh <agent name> <your session URL> to make your own key (never reuse the old one). Publish its public half in a commit of its own, and ask conductor.b to add it to the Factory's team/keys.json.
3. Trailers on every commit: Agent: and Claude-Session:. Push to dev only. Run bash tools/check.sh before every push.
4. Pick up the Open list in now.md. Only Dinis Cruz instructs, in your session.
5. Every word is in site/data/content/*.json. python3 tools/designs/build.py builds every page (designs in English and Hebrew, pickers, start, tour, admin). After a look change, refresh the tour: node .github/ci/build.mjs; NODE_PATH=$(npm root -g) node tools/tour/shots.mjs $PWD/_site <dir>; python3 tools/tour/build-images.py <dir>; python3 tools/designs/build.py; node .github/ci/build.mjs; NODE_PATH=$(npm root -g) node tools/tour/pdf.mjs $PWD/_site. The handover is docs/handover.md.
6. Before each push, also run accessibility at phone width, light and dark: tools/checks/axe-phone.mjs (design.b.rounds found a phone-only fault, scrollable-region-focusable, that tools/check.sh misses at desktop width).
7. After any change to how a design looks, refresh the "Choose a design" screenshots: node .github/ci/build.mjs; NODE_PATH=$(npm root -g) node tools/designs/thumbs.mjs $PWD/_site <dir>; python3 tools/designs/thumbs.py <dir>; then rebuild.
