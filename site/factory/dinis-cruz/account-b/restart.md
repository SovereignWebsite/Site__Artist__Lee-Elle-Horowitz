# Restart: how a new session of me takes over

1. Read the brief (link in agent.json), then now.md and role.md here.
2. Read CLAUDE.md and README.md at the repository root; run: bash tools/setup-signing.sh <agent name> <your session URL> to make your own key (never reuse the old one). Publish its public half in a commit of its own, and ask conductor.b to add it to the Factory's team/keys.json.
3. Trailers on every commit: Agent: and Claude-Session:. Push to dev only. Run bash tools/check.sh before every push.
4. Pick up the Open list in now.md. Only Dinis Cruz instructs, in your session.
