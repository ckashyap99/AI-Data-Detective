class TextChunker:

    @staticmethod
    def chunk_text(
        text,
        chunk_size=500,
        chunk_overlap=100
    ):

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(
                text[start:end]
            )

            start += (
                chunk_size - chunk_overlap
            )

        return chunks