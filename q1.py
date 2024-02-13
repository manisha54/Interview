# You are given a paragraph and a width n, where n represents the maximum number of characters
# that can be displayed on a single line of a screen.
#  Write a function formatParagraph(paragraph: str, width: int) -> str to
# format the paragraph such that it fits within the given width constraint.
# The function should return the formatted paragraph as a single string, with
# each line not exceeding the width n. Words in the paragraph should not be split,
# and the paragraph should be formatted for optimal readability.


def test(paragraph, width):
    words = paragraph.split()
    lines =[]
    current_line=""

    for word in words:
        if len(word) > width:
            if current_line:
                lines.append(current_line.rstrip())
                current_line = ""
            lines.append(word[:width])
            remaining_chars = len(word) - width
            while remaining_chars > width:
                lines.append(word[width: width +width])
                remaining_chars -= width
            current_line = word[-remaining_chars] + " "
        elif len(current_line) + len(word) <= width:
            current_line += word + " "
        else:
            lines.append(current_line.rstrip())
            current_line = word + " "
    lines.append(current_line.rstrip())
    test = "\n".join(lines)

    return test



