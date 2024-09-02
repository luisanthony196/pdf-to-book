import click

from pdftobook.coordinates import Coordinates
from pdftobook.pagination import Pagination
from pdftobook.pdf import BookFormat


@click.command()
@click.argument("input", type=click.File("rb"))
@click.argument("output", type=click.File("wb"))
@click.option("-s", "--separation", default=0, type=int, help="Separacion entre dos paginas")
@click.option("-g", "--growth", default=0, type=int, help="Variacion del tamanio de las paginas")
@click.option("-r", "--ranges", nargs=2, multiple=True, type=click.Tuple([int, int]), help="Rangos que seran usados")
@click.option("-ip", "--include-pages", type=str, help="Lista de numeros a incluir")
@click.option("-ep", "--exclude-pages", type=str, help="Lista de numeros a excluir")
@click.option("-n", "--nro-pages", type=int, help="Nro de hojas para dividir")
def cli(input, output, separation, growth, ranges, include_pages, exclude_pages, nro_pages):
	pgn = Pagination(ranges, to_list(include_pages), to_list(exclude_pages), nro_pages)
	cod = Coordinates(separation, growth)
	pdf = BookFormat(cod, pgn, input)
	pdf.create()
	pdf.save(output)
	print(len(pgn.book), "paginas procesadas")


def to_list(pages: str):
	if pages != None:
		return [int(i) for i in pages.split(",")]
	return None
