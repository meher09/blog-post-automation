import html.entities
import mammoth
import codecs


def word_to_html(wordfile):
    custom_styles = """
                    b => strong
                    table => table.table.table-hover.table-responsive
                    u => em
                    """
    with open(wordfile, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file, style_map=custom_styles)
        text = result.value
        text = text.replace("<td><p>", "<td>").replace("</p></td>", "</td>").replace('<td><strong>', '<td>').replace(
            '</strong></td>', '</td>')
        for i, char in enumerate(text):
            if ord(char) >= 128:
                entity = html.entities.html5.get(char)
                if entity is not None:
                    text = text[:i] + entity + text[i + 1:]

        return text


# Enter File name
word = input('Enter Word File Name: ').strip()
description = word_to_html(word)
with codecs.open("output.txt", "w", "utf-8") as file:
    file.write(description)


print("HTML has been saved to output.txt in UTF-8 encoding.")
