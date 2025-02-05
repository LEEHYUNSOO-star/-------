def count_words_in_file(file_path): # 텍스트 파일에서 단어 수를 세는 함수
   
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        words = text.split()
        return len(words)
    except FileNotFoundError:
        print(f"파일 {file_path}을(를) 찾을 수 없습니다.")
        return 0
    except Exception as e:
        print(f"오류 발생: {e}")
        return 0
