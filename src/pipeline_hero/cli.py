import click

from .pipeline import Pipeline


@click.group()
def cli():
    """CLI for pipeline-hero."""


@cli.command()
@click.option("--config", default=None, help="Path to config file (optional)")
def run(config):
    """Run the pipeline."""
    p = Pipeline()
    p.run()


if __name__ == "__main__":
    cli()
