import demoji
demoji.download_codes()
def convert_emojis_to_text(text_with_emojis):
    return demoji.replace(text_with_emojis)
text_with_emojis = "I love Python 😀!"
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print(text_without_emojis)