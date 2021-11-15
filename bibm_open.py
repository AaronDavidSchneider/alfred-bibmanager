import bibmanager.bib_manager as bibm
import bibmanager.pdf_manager as pdf
import sys

if __name__ == "__main__":
    key = sys.argv[1]

    bibm.load()

    try:
        pdf.open(key=key)
    except ValueError:
        bib = bibm.find(key=key)
        if bib is not None and bib.bibcode is not None:
            pdf.fetch(bib.bibcode)
            pdf.open(key=key)