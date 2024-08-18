from pypdf import PageObject, PaperSize, PdfReader, PdfWriter, Transformation

from bookpdf.coordinates import Coordinates
from bookpdf.pagination import Pagination


class BookFormat:
	def __init__(self, coordinate: Coordinates, pagination: Pagination, input) -> None:
		self.cd = coordinate
		self.pg = pagination
		self.wr = PdfWriter()
		self.rd = PdfReader(input)

	def create(self):
		self.pg.process(len(self.rd.pages))
		self.pg.make_pagination()
		for pg_arr in self.pg.arr:
			ext_pag = self.wr.add_blank_page(PaperSize.A4.width, PaperSize.A4.height)
			int_pag = self.wr.add_blank_page(PaperSize.A4.width, PaperSize.A4.height)

			# Lista de paginas en orden descendente visualmente
			self.cd.list_of_4pages = pg_arr
			print(f"Process pages {[None if i is None else i + 1 for i in pg_arr]}")

			# Iteracion por cada una de las 4 paginas
			for pg_num in pg_arr:
				if pg_num is None:
					continue

				page = self.rd.pages[pg_num]
				page.scale_by(self.cd.get_gro(page.mediabox.height))

				self.cd.actual = pg_num
				self.cd.actual_width = page.mediabox.width

				if self.cd.is_ext():
					self.trans(ext_pag, page)
				else:
					self.trans(int_pag, page)

	def trans(self, base:PageObject, page:PageObject):
		base.merge_transformed_page(page,
			Transformation().rotate(self.cd.get_rt()).translate(self.cd.get_trh(), self.cd.get_trv()),
		)


	def save(self, output):
		self.wr.write(output)
		# with open(self.output_name, "wb") as fp:
		    # self.wr.write(fp)
