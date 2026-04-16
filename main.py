import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Smart Intrusion Detection System"
    )
    parser.add_argument("--scenario", choices=["railway", "home"],
                        default="railway",
                        help="Which scenario to run (default: railway)")
    args = parser.parse_args()

    if args.scenario == "railway":
        from scenarios.railway_station import run
    else:
        from scenarios.home_intrusion import run

    print(f"[MAIN] Starting scenario: {args.scenario.upper()}")
    run()

if __name__ == "__main__":
    main()