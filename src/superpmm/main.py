"""SuperPMM — CLI entry point."""

from .agents.orchestrator import SuperPMMOrchestrator


def main():
    orchestrator = SuperPMMOrchestrator()
    orchestrator.run()


if __name__ == "__main__":
    main()
