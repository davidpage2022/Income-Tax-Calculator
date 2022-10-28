"""Personal tool for getting total gross and net payments from .PDF payslips."""
from os import listdir
from PyPDF4.pdf import PdfFileReader

ROOT_PATH = "Data/"
GROSS_SEARCH_STRING = """GROSS 
PAY:
$"""
NET_SEARCH_STRING = """NET 
PAY:
$"""


def main():
    """Get total gross and net payments from .PDF payslips"""
    total_gross = 0
    total_net = 0

    for filename in listdir(ROOT_PATH):
        filepath = "".join((ROOT_PATH, filename))
        with open(filepath, "rb") as in_file:
            reader = PdfFileReader(in_file)
            page = reader.getPage(0)
            text = page.extractText()

            gross = read_currency(extract_label_value(text, GROSS_SEARCH_STRING))
            net = read_currency(extract_label_value(text, NET_SEARCH_STRING))

            print(f"{filename:40} Gross: {gross:10.2f}, Net: {net:10.2f}")

            total_gross += gross
            total_net += net

    print("=" * 80)
    print(f"{'':40} Gross: {total_gross:10.2f}, Net: {total_net:10.2f}")


def extract_label_value(text, label):
    """Search for the label string in text, then return the value (string) that follows it.
    The value ends when a newline is reached."""
    value_index = text.index(label) + len(label)
    return text[value_index: text.find("\n", value_index)]


def read_currency(string):
    """Attempts to convert string to a decimal number, assuming it is currency."""
    return float(string.strip().replace(",", ""))


if __name__ == '__main__':
    main()
