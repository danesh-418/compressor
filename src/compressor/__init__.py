import tarfile

import click


algorithm = ""
ALGORITHMS = ("zst",
    "xz",
    "bz2",
    "gz"
)

@click.group()
@click.option("-a", "--algorithm", type=click.Choice(HashType, case_sensitive=False), default=ALGORITHMS[0])
def main(alg):
    global algorithm
    algorithm = alg

@main.command()
@click.argument("indir", type=click.Path(file_okay=False, dir_okay=True, exists=True))
@click.argument("outfile", type=click.Path(file_okay=True, dir_okay=False, exists=False))
def compress(indir, outfile):
    global algorithm
    with tarfile.open(outfile, f"w:{algorithm}") as tar:
        tar.add(indir, arcname="out")

@main.command()
@click.argument("infile", type=click.Path(file_okay=True, dir_okay=False, exists=True))
@click.argument("outdir", type=click.Path(file_okay=False, dir_okay=True, exists=False))
def decompress(infile, outdir):
    global algorithm
    with tarfile.open(infile, f"r:{algorithm}") as tar:
        tar.extractall(outdir, filter="tar")

if __name__ == "__main__":
    main()
