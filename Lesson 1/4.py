words = ['разработка', 'администрирование', 'protocol']

for word in words:
    encoded_word = word.encode('utf-8')
    print(f'Байтовое: {encoded_word}')
    decoded_word = encoded_word.decode('utf-8')
    print(f'Преобрзованное байтовое: {decoded_word}')
