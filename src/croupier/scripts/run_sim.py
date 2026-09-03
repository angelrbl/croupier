import click
import pandas as pd
from pathlib import Path

from croupier.strats import BasicStrategy
from croupier.simulation import run_simulation

@click.command()
@click.option('--iterations', '-i', default=10000, help="Number of games to simulate", type=int)
@click.option('--dealer-threshold', '-t', default=17, help="Score at which the dealer stops hitting", type=int)
@click.option('--output', '-o', default='data/simulation_results.csv', help="Path to save the CSV at", type=str)
def run_sim(iterations, dealer_threshold, output):
    click.echo(f"Starting simulation of {iterations} games...")

    strategy = BasicStrategy()

    df = run_simulation(
        iterations=iterations,
        strategy=strategy,
        dealer_stand_threshold=dealer_threshold,
    )

    output_path = Path(output)
    output_path.parent.mkdir(exist_ok=True, parents=True)

    df.to_csv(output_path, index=False)
    click.secho(f"Simulation completed! Data saved at: {output_path}", fg="green")

if __name__ == "__main__":
    run_sim()