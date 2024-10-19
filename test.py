from src.utils import markdonify_and_escape_special_char

html_content = "<h1>Title</h1><p>This is {a} <strong>paragraph</strong>.</p>"
markdown = markdonify_and_escape_special_char(html_content)
print(markdown)
