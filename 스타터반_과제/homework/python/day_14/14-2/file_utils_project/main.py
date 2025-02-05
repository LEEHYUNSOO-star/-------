from networkx import is_path
from file_utils.text_processor import count_words_in_file

path = 'sample.txt' # 파일 경로 지정


word_count = count_words_in_file(path) # 단어 수 계산 


if word_count > 0:
    print(f"파일 '{path}'의 단어 수는 {word_count}개입니다.") # 결과 출력
 