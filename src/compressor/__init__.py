import tarfile

import click


ALGORITHM = "zst"

@click.group()
def main():
    pass

@main.command()
@click.argument("indir", type=click.Path(file_okay=False, dir_okay=True, exists=True))
@click.argument("outfile", type=click.Path(file_okay=True, dir_okay=False, exists=False))
def compress(indir, outfile):
    with tarfile.open(outfile, f"w:{zst}") as tar:
        tar.add(indir, arcname="out")

@main.command()
@click.argument("infile", type=click.Path(file_okay=True, dir_okay=False, exists=True))
@click.argument("outdir", type=click.Path(file_okay=False, dir_okay=True, exists=False))
def decompress(infile, outdir):
    with tarfile.open(infile, f"r:{zst}") as tar:
        tar.extractall(outdir, filter="tar")

if __name__ == "__main__":
    main()
