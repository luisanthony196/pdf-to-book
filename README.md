# PDF To Book

Advanced converter from standard PDF to brochure mode

## Installation

Install via pipx or Rye on MacOS, Linux, and Windows:

```bash
  pipx install pdfbook
  cd my-project
```

## Features

- Command line program
- Easy pagination, ranges, include pages and exclude pages
- Size modification
- Internal space modification
- Paginated by fragments

## Usage/Examples

Once installed, you can run PDFBook by typing tjournal in your terminal:
```
pdfbook input.pdf output.pdf
```

To view the available arguments and commands, you can use the --help or -h flag:

```javascript
pdfbook --help
Usage: book [OPTIONS] INPUT OUTPUT

Options:
  -s, --separation INTEGER        Separacion entre dos paginas
  -g, --growth INTEGER            Variacion del tamanio de las paginas
  -r, --ranges <INTEGER INTEGER>...
                                  Rangos que seran usados
  -ip, --include-pages TEXT       Lista de numeros a incluir
  -ep, --exclude-pages TEXT       Lista de numeros a excluir
  -n, --nro-pages INTEGER         Nro de hojas para dividir
  --help                          Show this message and exit.
```
