import math

class Pagination:
	def __init__(self, ranges, include_pages = None, exclude_pages = None, booklet = None) -> None:
		self.arr = []
		self.book = []
		self.ranges = ranges
		self.booklet = booklet
		self.inp = include_pages
		self.exp = exclude_pages if exclude_pages != None else []

	def process(self, nro):
		if len(self.ranges) == 0:
			self.ranges = [(1, nro)]

		for r in self.ranges:
			self.book.extend(list(range(r[0], r[1] + 1)))

		if self.inp != None:
			self.book.extend(self.inp)

		self.book = list(set(self.book))
		self.book.sort()

		for p in self.exp:
			if p in self.book:
				self.book.remove(p)

	def make_separation(self):
		book_len = len(self.book)
		nro4 = book_len if book_len %4 == 0 else book_len +4 - (book_len %4)
		if self.booklet is not None:
			nro_booklets = math.ceil(book_len / (self.booklet *40))
			for i in range(0, nro_booklets, self.booklet * 4):
				self.make_pagination(i, self.booklet *4)
		pass

	def make_pagination(self, ini = 0, end = 0):
		nro = len(self.book)
		end = nro if nro %4 == 0 else nro +4 - (nro %4)
		for i in range(ini, int(end / 2), 2):
			self.arr.append((self.gb(i), self.gb(end -i -1), self.gb(i +1), self.gb(end -i -2)))

	def gb(self, ind):
		return self.book[ind] - 1 if ind < len(self.book) else None
