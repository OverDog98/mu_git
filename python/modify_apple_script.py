# applescript 수정하는 코드
# 3/12 현재 applescripts/get_project_info_aif.applescript 의 내용을 바꿔주는 시퀀스가 있음
## (applescripts/get_project_info_aif.applescript : lpx 프로그램에서 abcd.logicx 음원정보 가져와서, abcd.txt로 만들어주는 역할)
## encoding 문제때문에 crud할때는 encoding='ISO-8859-1'로,

def modify_apple_script(apple_script_path, YOUR_TXT_PATH, new_txt_path):
    # 파일을 읽기 모드로 열기
    with open(apple_script_path, 'r', encoding='ISO-8859-1') as file:
        script_content = file.read()

    # 특정 내용을 새로운 내용으로 교체
    script_content = script_content.replace(YOUR_TXT_PATH, new_txt_path)
    print(script_content)
    # 파일을 쓰기 모드로 열어 내용을 덮어쓰기
    with open(apple_script_path, 'w', encoding='ISO-8859-1') as file:
        file.write(script_content)
