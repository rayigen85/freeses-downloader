"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Freeses Downloader."""


if __name__ == "__main__":
    main(prog_name="freeses-downloader")  # pragma: no cover
