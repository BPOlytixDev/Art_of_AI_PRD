import os
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject


def fitz_document(path):
    import pymupdf as fitz

    return fitz.open(path)


def main():
    command = sys.argv[1]
    path = sys.argv[2]
    if command == "count":
        document = fitz_document(path)
        print(len(document))
        document.close()
    elif command == "text":
        document = fitz_document(path)
        text = "\f".join(page.get_text() or "" for page in document)
        document.close()
        if len(sys.argv) > 3:
            with open(sys.argv[3], "w", encoding="utf-8") as stream:
                stream.write(text)
        else:
            sys.stdout.write(text)
    elif command == "merge":
        import pymupdf as fitz

        writer = fitz.open()
        for input_path in sys.argv[2:-1]:
            source = fitz.open(input_path)
            writer.insert_pdf(source)
            source.close()
        output_path = sys.argv[-1]
        temporary_path = f"{output_path}.tmp"
        writer.save(temporary_path, garbage=4, deflate=True)
        writer.close()
        os.replace(temporary_path, output_path)
    elif command == "resize":
        width = float(sys.argv[3])
        height = float(sys.argv[4])
        output_path = sys.argv[5]
        reader = PdfReader(path)
        writer = PdfWriter()
        for page in reader.pages:
            for box_name in ("mediabox", "cropbox", "bleedbox", "trimbox", "artbox"):
                setattr(page, box_name, RectangleObject((0, 0, width, height)))
            writer.add_page(page)
        with open(output_path, "wb") as stream:
            writer.write(stream)
    else:
        raise SystemExit(f"Unknown PDF command: {command}")


if __name__ == "__main__":
    main()
