from langchain_core.documents import Document

documents = [
    Document(
        page_content = 'Books are the best friend of a man , he should never forget them',
        metadata = {'source' : 'books-info-doc'}
    ),
    Document(
        page_content='This is just some gibberish text about AI and Fighter Engines',
        metadata = {'source' : 'Nabin-love-for-docs'}
    )
]