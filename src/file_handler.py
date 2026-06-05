# file_handler.py

def read_document(file_path):
    """
    Reads text from a file.

    Args:
        file_path (str): Path to text file

    Returns:
        str: Document content
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
        return ""

    except Exception as error:
        print(f"Error reading file: {error}")
        return ""