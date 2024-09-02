from pypdf import PaperSize


class Coordinates:
	def __init__(self, separation_space, growth) -> None:
		self.actual_width = 0
		self.actual = -1
		self.list_of_4pages = []
		self.sep = separation_space
		self.gro = growth

	def get_gro(self, page_h: float):
		return (PaperSize.A4.width + self.gro * 2) / page_h

	def get_rt(self):
		"""Rotacion para externos e internos"""
		if self.is_ext():
			return 90
		return -90

	def get_trh(self):
		"""Posicionamiento en horizontal, en perspectiva del documento original"""
		if self.list_of_4pages.index(self.actual) == 0:
			return PaperSize.A4.width + self.gro
		elif self.list_of_4pages.index(self.actual) == 1:
			return PaperSize.A4.width + self.gro
		elif self.list_of_4pages.index(self.actual) == 2:
			return 0 - self.gro
		else:
			return 0 - self.gro

	def get_trv(self):
		"""Posicionamiento en vertical, en perspectiva del documento original"""
		if self.list_of_4pages.index(self.actual) == 0:
			return PaperSize.A4.height / 2 + self.sep
		elif self.list_of_4pages.index(self.actual) == 1:
			return PaperSize.A4.height / 2 - self.actual_width - self.sep
		elif self.list_of_4pages.index(self.actual) == 2:
			return (PaperSize.A4.height + 2 * self.actual_width) / 2 + self.sep
		else:
			return PaperSize.A4.height / 2 - self.sep

	def is_ext(self):
		if self.list_of_4pages.index(self.actual) < 2:
			return True
		return False
