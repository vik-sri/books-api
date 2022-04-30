from books_api.defines import api_defines as api_def
from books_api.internal_functions.internal_create_book import get_book_data


def external_create_book(kwargs):
    function_name = "external_create_book"
    try:
        api_response = {
            api_def.STATUS: api_def.ERROR,
            api_def.MESSAGE: api_def.ERROR_UNKNOWN
        }
        book_id = kwargs["book_id"]

        # Get book data from gutenberg
        book_response = get_book_data(book_id=book_id)

    except Exception as e:
        print(e)
